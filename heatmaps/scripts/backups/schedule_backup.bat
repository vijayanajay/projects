@echo off
ECHO Setting up scheduled backup task for Stock Heatmap database...
ECHO.

SET TASKNAME=StockHeatmapDatabaseBackup
SET XMLFILE="%~dp0schedule_backup_task.xml"

ECHO Task Name: %TASKNAME%
ECHO XML File: %XMLFILE%
ECHO.

ECHO Attempting to create scheduled task...
schtasks /create /tn %TASKNAME% /xml %XMLFILE%

IF %ERRORLEVEL% NEQ 0 (
    ECHO.
    ECHO Failed to create task. Error code: %ERRORLEVEL%
    ECHO.
    ECHO You may need to run this script as administrator.
    ECHO Alternatively, you can import the XML file manually:
    ECHO 1. Open Task Scheduler (taskschd.msc)
    ECHO 2. Right-click "Task Scheduler Library" and select "Import Task..."
    ECHO 3. Browse to %XMLFILE% and import it
) ELSE (
    ECHO.
    ECHO Task created successfully!
    ECHO The backup will run daily at 2:00 AM.
    ECHO You can view or modify the task in Task Scheduler.
)

ECHO.
PAUSE
