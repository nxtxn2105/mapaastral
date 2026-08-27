@echo off
cd /d "%~dp0"
cls
echo ================================================================
echo   ENVIANDO ARQUIVOS PARA O GITHUB (nxtxn2105/mapaastral)...
echo ================================================================
echo.
git push -u origin main --force
echo.
echo ================================================================
echo   CONCLUIDO! Verifique em:
echo   https://github.com/nxtxn2105/mapaastral
echo ================================================================
pause
