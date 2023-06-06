@echo off
setlocal

REM Set the target folder path on the Desktop
set "targetFolder=%USERPROFILE%\Desktop\Data Extract"

REM Check if the target folder already exists
if not exist "%targetFolder%" (
    echo Creating target folder...
    mkdir "%targetFolder%"
)

REM Copy the contents of the current folder to the target folder (including hidden files and folders)
xcopy /s /y /q /i /h "%~dp0*" "%targetFolder%"

REM Prompt the user to update if the target folder already exists
if exist "%targetFolder%\*" (
    echo.
    set /p "choice=Do you want to update the program? (Y/N): "
    if /i "%choice%"=="Y" (
        echo Updating program...
        xcopy /s /y /q /i /h "%~dp0*" "%targetFolder%"
    ) else (
        echo Program installation canceled.
    )
)

endlocal
