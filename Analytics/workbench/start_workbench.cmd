@echo off
setlocal
if not defined MATHPALETTE_PYTHON if exist "%USERPROFILE%\Desktop\PythonEnvs\mathpalette-analytics\Scripts\python.exe" set "MATHPALETTE_PYTHON=%USERPROFILE%\Desktop\PythonEnvs\mathpalette-analytics\Scripts\python.exe"
cd /d "%~dp0"
echo MathPalette fine-grained C workbench - http://127.0.0.1:8767
python -X utf8 -B launch_workbench.py %*
if errorlevel 1 pause
