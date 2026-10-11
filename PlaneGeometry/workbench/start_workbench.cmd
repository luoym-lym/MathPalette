@echo off
setlocal
cd /d "%~dp0"
echo MathPalette PlaneGeometry Special workbench - http://127.0.0.1:8768
python -X utf8 -B launch_workbench.py %*
if errorlevel 1 pause
