#!/usr/bin/env python
"""
Database restore script for the Indian Stock Market Heatmap application.
This script restores a PostgreSQL database from a backup file created by backup_db.py.
"""

import os
import sys
import subprocess
import logging
import argparse
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(
            os.path.join(os.path.dirname(__file__), "restore.log")
        ),
    ],
)
logger = logging.getLogger("db_restore")

# Get the project root directory (3 levels up from this script)
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Load environment variables from .env file for database credentials
def load_env():
    """Load environment variables from .env file."""
    env_vars = {}
    try:
        with open(os.path.join(BASE_DIR, ".env"), "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                key, value = line.split("=", 1)
                env_vars[key.strip()] = value.strip()
        return env_vars
    except Exception as e:
        logger.error(f"Error loading .env file: {e}")
        sys.exit(1)


def list_available_backups(backup_dir):
    """List available backup files."""
    try:
        backups = [f for f in os.listdir(backup_dir) if f.endswith(".backup")]
        backups.sort(reverse=True)  # Sort by newest first
        return backups
    except Exception as e:
        logger.error(f"Error listing backup files: {e}")
        return []


def run_pg_restore(
    db_name, db_user, db_password, db_host, db_port, backup_file
):
    """Run pg_restore to restore a database from backup."""
    try:
        # Set environment variables for pg_restore
        env = os.environ.copy()
        env["PGPASSWORD"] = db_password

        # Run pg_restore command
        command = [
            "pg_restore",
            "--clean",
            "--no-owner",
            "--no-privileges",
            f"--dbname=postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}",
            backup_file,
        ]

        logger.info(f"Restoring database {db_name} from {backup_file}")
        result = subprocess.run(
            command, env=env, capture_output=True, text=True
        )

        if result.returncode != 0:
            # pg_restore often returns non-zero even on success due to minor errors
            logger.warning(
                f"pg_restore completed with warnings or errors: {result.stderr}"
            )

        logger.info(f"Restore completed from: {backup_file}")
        return True
    except Exception as e:
        logger.error(f"Error restoring database: {e}")
        return False


def main():
    """Main function to perform database restore."""
    parser = argparse.ArgumentParser(
        description="PostgreSQL Database Restore Script"
    )
    parser.add_argument(
        "--backup-dir",
        help="Directory containing backups",
        default=os.path.join(BASE_DIR, "backups"),
    )
    parser.add_argument(
        "--backup-file", help="Specific backup file to restore (optional)"
    )
    parser.add_argument(
        "--env",
        choices=["dev", "prod"],
        help="Environment to restore to",
        default="dev",
    )
    args = parser.parse_args()

    # Ensure backup directory exists
    if not os.path.exists(args.backup_dir):
        logger.error(f"Backup directory does not exist: {args.backup_dir}")
        sys.exit(1)

    # Load environment variables
    env_vars = load_env()

    # Get database credentials based on environment
    prefix = "" if args.env == "prod" else f"{args.env.upper()}_"
    db_name = (
        env_vars.get(f"DB_NAME_{args.env.upper()}")
        if args.env != "prod"
        else env_vars.get("DB_NAME")
    )
    db_user = (
        env_vars.get(f"DB_USER_{args.env.upper()}")
        if args.env != "prod"
        else env_vars.get("DB_USER")
    )
    db_password = (
        env_vars.get(f"DB_PASSWORD_{args.env.upper()}")
        if args.env != "prod"
        else env_vars.get("DB_PASSWORD")
    )
    db_host = (
        env_vars.get(f"DB_HOST_{args.env.upper()}")
        if args.env != "prod"
        else env_vars.get("DB_HOST")
    )
    db_port = (
        env_vars.get(f"DB_PORT_{args.env.upper()}")
        if args.env != "prod"
        else env_vars.get("DB_PORT")
    )

    # Get backup file to restore
    backup_file = args.backup_file
    if not backup_file:
        # If no specific file provided, list available backups and use the most recent
        backups = list_available_backups(args.backup_dir)
        if not backups:
            logger.error("No backup files found.")
            sys.exit(1)

        # Print available backups
        print("Available backups:")
        for i, backup in enumerate(backups):
            print(f"{i+1}. {backup}")

        # Ask user to choose a backup
        choice = input(
            "Enter number of backup to restore (or press Enter for most recent): "
        )
        if choice.strip():
            try:
                idx = int(choice.strip()) - 1
                if 0 <= idx < len(backups):
                    backup_file = os.path.join(args.backup_dir, backups[idx])
                else:
                    logger.error("Invalid backup number.")
                    sys.exit(1)
            except ValueError:
                logger.error("Invalid input. Please enter a number.")
                sys.exit(1)
        else:
            # Use the most recent backup
            backup_file = os.path.join(args.backup_dir, backups[0])
    else:
        # Use the provided backup file path
        if not os.path.exists(backup_file):
            # Try with backup directory prefix
            backup_file = os.path.join(args.backup_dir, backup_file)
            if not os.path.exists(backup_file):
                logger.error(f"Backup file does not exist: {backup_file}")
                sys.exit(1)

    # Confirm restore action
    confirm = input(
        f"Are you sure you want to restore database {db_name} from {os.path.basename(backup_file)}? [y/N]: "
    )
    if confirm.lower() != "y":
        logger.info("Restore cancelled.")
        sys.exit(0)

    # Run pg_restore
    success = run_pg_restore(
        db_name, db_user, db_password, db_host, db_port, backup_file
    )

    if success:
        logger.info("Restore process completed.")
    else:
        logger.error("Restore process failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
