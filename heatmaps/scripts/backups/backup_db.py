#!/usr/bin/env python
"""
Database backup script for the Indian Stock Market Heatmap application.
This script creates backups of the PostgreSQL database using pg_dump.
"""

import os
import sys
import subprocess
import datetime
import shutil
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
            os.path.join(os.path.dirname(__file__), "backup.log")
        ),
    ],
)
logger = logging.getLogger("db_backup")

# Get the project root directory (3 levels up from this script)
BASE_DIR = Path(__file__).resolve().parent.parent.parent
print(f"Base directory: {BASE_DIR}")


# Load environment variables from .env file for database credentials
def load_env():
    """Load environment variables from .env file."""
    env_vars = {}
    env_file = os.path.join(BASE_DIR, ".env")
    print(f"Loading environment from: {env_file}")
    try:
        with open(env_file, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                key, value = line.split("=", 1)
                env_vars[key.strip()] = value.strip()
        print(f"Loaded {len(env_vars)} environment variables")
        return env_vars
    except Exception as e:
        logger.error(f"Error loading .env file: {e}")
        sys.exit(1)


def create_backup_directory(backup_dir):
    """Create backup directory if it doesn't exist."""
    try:
        os.makedirs(backup_dir, exist_ok=True)
        logger.info(f"Backup directory created/verified: {backup_dir}")
    except Exception as e:
        logger.error(f"Error creating backup directory: {e}")
        sys.exit(1)


def run_pg_dump(db_name, db_user, db_password, db_host, db_port, backup_file):
    """Run pg_dump to create a database backup."""
    print(f"Attempting to backup database: {db_name}")
    print(f"Database connection: {db_user}@{db_host}:{db_port}/{db_name}")

    try:
        # Set environment variables for pg_dump
        env = os.environ.copy()
        env["PGPASSWORD"] = db_password

        # Check if pg_dump is available
        try:
            pg_dump_version = subprocess.run(
                ["pg_dump", "--version"],
                env=env,
                capture_output=True,
                text=True,
            )
            print(f"pg_dump version: {pg_dump_version.stdout}")
        except FileNotFoundError:
            logger.error(
                "pg_dump command not found. Please ensure PostgreSQL client tools are installed."
            )
            return False

        # Run pg_dump command
        command = [
            "pg_dump",
            f"--dbname=postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}",
            "--format=custom",
            f"--file={backup_file}",
        ]

        print(f"Running pg_dump with command: {' '.join(command)}")
        logger.info(f"Running pg_dump on database {db_name}")
        result = subprocess.run(
            command, env=env, capture_output=True, text=True
        )

        if result.returncode != 0:
            logger.error(f"pg_dump error: {result.stderr}")
            print(f"pg_dump error: {result.stderr}")
            return False

        logger.info(f"Backup created successfully: {backup_file}")
        return True
    except Exception as e:
        logger.error(f"Error creating backup: {e}")
        print(f"Error creating backup: {e}")
        return False


def cleanup_old_backups(backup_dir, keep_days=7):
    """Delete backups older than keep_days."""
    try:
        now = datetime.datetime.now()
        logger.info(f"Cleaning up backups older than {keep_days} days")

        for f in os.listdir(backup_dir):
            if not f.endswith(".backup"):
                continue

            file_path = os.path.join(backup_dir, f)
            file_time = datetime.datetime.fromtimestamp(
                os.path.getmtime(file_path)
            )
            if (now - file_time).days > keep_days:
                os.remove(file_path)
                logger.info(f"Deleted old backup: {f}")
    except Exception as e:
        logger.error(f"Error cleaning up old backups: {e}")


def main():
    """Main function to perform database backup."""
    parser = argparse.ArgumentParser(
        description="PostgreSQL Database Backup Script"
    )
    parser.add_argument(
        "--backup-dir",
        help="Directory to store backups",
        default=os.path.join(BASE_DIR, "backups"),
    )
    parser.add_argument(
        "--keep-days",
        type=int,
        help="Number of days to keep backups",
        default=7,
    )
    parser.add_argument(
        "--env",
        choices=["dev", "prod"],
        help="Environment to backup",
        default="dev",
    )
    parser.add_argument(
        "--debug", action="store_true", help="Enable debug output"
    )
    args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)
        print("Debug mode enabled")

    # Create backup directory
    print(f"Creating backup directory: {args.backup_dir}")
    create_backup_directory(args.backup_dir)

    # Load environment variables
    env_vars = load_env()

    # Get database credentials based on environment
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

    print(
        f"Database info - Name: {db_name}, User: {db_user}, Host: {db_host}, Port: {db_port}"
    )

    # Generate backup filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(
        args.backup_dir, f"{db_name}_{timestamp}.backup"
    )
    print(f"Backup file will be: {backup_file}")

    # Run pg_dump
    success = run_pg_dump(
        db_name, db_user, db_password, db_host, db_port, backup_file
    )

    if success:
        # Clean up old backups
        cleanup_old_backups(args.backup_dir, args.keep_days)
        logger.info("Backup process completed successfully.")
        print("Backup process completed successfully.")
    else:
        logger.error("Backup process failed.")
        print("Backup process failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
