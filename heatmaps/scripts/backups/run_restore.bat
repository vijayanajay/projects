@echo off
ECHO Running database restore...
cd %~dp0..\..\
python scripts/backups/restore_db.py %*
IF %ERRORLEVEL% NEQ 0 (
    ECHO Restore failed with error code %ERRORLEVEL%
    EXIT /B %ERRORLEVEL%
)
ECHO Restore completed successfully!
EXIT /B 0
