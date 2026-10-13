@echo off
setlocal
if not defined MATHPALETTE_PYTHON if exist "%USERPROFILE%\Desktop\PythonEnvs\mathpalette-analytics\Scripts\python.exe" set "MATHPALETTE_PYTHON=%USERPROFILE%\Desktop\PythonEnvs\mathpalette-analytics\Scripts\python.exe"
cd /d "%~dp0workbench"
if defined MATHPALETTE_PYTHON (
  "%MATHPALETTE_PYTHON%" -X utf8 -B launch_workbench.py %*
) else (
  python -X utf8 -B launch_workbench.py %*
)
if errorlevel 1 pause
