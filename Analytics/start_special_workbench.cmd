@echo off
setlocal
cd /d "%~dp0workbench"
python -B launch_workbench.py %*
if errorlevel 1 pause
