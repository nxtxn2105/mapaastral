@echo off
cd /d "%~dp0"
cls
echo ================================================================
echo   PUBLICANDO NA VERCEL...
echo ================================================================
echo.
call vercel.cmd
echo.
pause
