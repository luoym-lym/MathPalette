@echo off
setlocal
cd /d "%~dp0"
echo MathPalette fine-grained C workbench - http://127.0.0.1:8767
python -B launch_workbench.py %*
if errorlevel 1 pause
