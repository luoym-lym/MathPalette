@echo off
setlocal
if not defined MATHPALETTE_PYTHON if exist "%USERPROFILE%\Desktop\PythonEnvs\mathpalette-analytics\Scripts\python.exe" set "MATHPALETTE_PYTHON=%USERPROFILE%\Desktop\PythonEnvs\mathpalette-analytics\Scripts\python.exe"
cd /d "%~dp0workbench"
set "MATHPALETTE_DATA=C:\Users\Kayla\Documents\Codex\mathpalette-plane-recovered\data"
set "MATHPALETTE_OUTPUT=C:\Users\Kayla\Documents\Codex\mathpalette-plane-recovered\output"
if defined MATHPALETTE_PYTHON (
  "%MATHPALETTE_PYTHON%" -X utf8 -B launch_workbench.py --data-dir "%MATHPALETTE_DATA%" --output-dir "%MATHPALETTE_OUTPUT%" %*
) else (
  python -X utf8 -B launch_workbench.py --data-dir "%MATHPALETTE_DATA%" --output-dir "%MATHPALETTE_OUTPUT%" %*
)
if errorlevel 1 pause

