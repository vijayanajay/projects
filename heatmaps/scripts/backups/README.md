# Database Backup and Restore Scripts

This directory contains scripts for backing up and restoring the PostgreSQL database for the Indian Stock Market Heatmap application.

## Prerequisites

- **PostgreSQL client tools** installed and accessible in your PATH:
  - On Windows: Add `C:\Program Files\PostgreSQL\<version>\bin` to your system PATH
  - On Linux: Install `postgresql-client` package
  - On Mac: Install via Homebrew with `brew install postgresql`
- Python 3.6 or higher
- Database credentials in the .env file at the project root

## Testing the Tools

Before scheduling backups, test that the PostgreSQL tools are working:

```bash
# Test pg_dump availability
pg_dump --version

# Test pg_restore availability
pg_restore --version
```

If these commands fail, ensure PostgreSQL is properly installed and added to your PATH.

## Backup Script

The `backup_db.py` script creates a backup of the database using pg_dump.

### Usage

```bash
# Basic usage (backs up development database)
python scripts/backups/backup_db.py

# Backup production database
python scripts/backups/backup_db.py --env prod

# Specify custom backup directory
python scripts/backups/backup_db.py --backup-dir /path/to/backup/dir

# Keep backups for 30 days instead of default 7
python scripts/backups/backup_db.py --keep-days 30

# Enable debug output
python scripts/backups/backup_db.py --debug
```

## Restore Script

The `restore_db.py` script restores a database from a backup file.

### Usage

```bash
# Basic usage (lists available backups and lets you choose)
python scripts/backups/restore_db.py

# Restore from a specific backup file
python scripts/backups/restore_db.py --backup-file heatmap_20250330_123456.backup

# Restore to production database (be careful!)
python scripts/backups/restore_db.py --env prod
```

## Scheduling Backups

### Windows (Task Scheduler)

1. Open Task Scheduler
2. Create a new task
3. Set the trigger (e.g., daily at 2 AM)
4. Set the action to start a program
   - Program/script: `python`
   - Arguments: `scripts/backups/backup_db.py`
   - Start in: `D:\Code\projects\trendtribes2\app\heatmaps`

### Linux/Mac (Cron)

Add a crontab entry:

```bash
# Run daily at 2 AM
0 2 * * * cd /path/to/project && python scripts/backups/backup_db.py
```

## Best Practices

1. Store backups in a different location than your application
2. Test restores regularly to ensure backups are working
3. Consider encrypting backups that contain sensitive data
4. Monitor the backup process and set up alerts for failures

## Troubleshooting

### Common Issues

1. **pg_dump not found**: Ensure PostgreSQL client tools are installed and in your PATH
2. **Permission denied**: Ensure your database user has sufficient privileges
3. **Connection refused**: Check database host and port settings in .env file
4. **Database does not exist**: Verify database name in .env file
