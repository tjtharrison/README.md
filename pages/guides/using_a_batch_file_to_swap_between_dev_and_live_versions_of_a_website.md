# Using a Batch file to swap between dev and live versions of a Website

This was required for one of my Customers who required being able to swap between the dev version and live version of their site from Windows – While the licensing for their site required the URL to be the same.

```
@echo off

SET NEWLINE=^& echo.

FIND /C /I "www.shop4dinosaurs.co.uk" %WINDIR%\system32\drivers\etc\hosts
IF %ERRORLEVEL% NEQ 0 ECHO %NEWLINE%^192.168.1.10 www.example.co.uk>>%WINDIR%\System32\drivers\etc\hosts

start "" http://www.example.co.uk


@ECHO off
SETLOCAL
SET "HOSTS=%WinDir%\System32\drivers\etc\hosts"
SET "TEMP_HOSTS=%TEMP%\%RANDOM%__hosts"
FINDSTR /V "192.168.1.10" "%HOSTS%" > "%TEMP_HOSTS%"
COPY /b/v/y "%TEMP_HOSTS%" "%HOSTS%"
EXIT /B

start "" http://www.example.co.uk
```