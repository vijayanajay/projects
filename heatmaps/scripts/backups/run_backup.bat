@echo off
ECHO Running database backup...
cd %~dp0..\..\
python scripts/backups/backup_db.py %*
IF %ERRORLEVEL% NEQ 0 (
    ECHO Backup failed with error code %ERRORLEVEL%
    EXIT /B %ERRORLEVEL%
)
ECHO Backup completed successfully!
EXIT /B 0
