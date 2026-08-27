@echo off
title Servidor Local - Funil Mahila Luz
echo ========================================================
echo   Iniciando Servidor Local do Funil e Mapa Astral
echo ========================================================
echo.
echo Abrindo em http://localhost:8080/index.html?debug=1 ...
echo.
start http://localhost:8080/index.html?debug=1
python -m http.server 8080
pause
