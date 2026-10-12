@echo off
setlocal
chcp 65001 >nul
cd /d "%~dp0"
set PYTHONDONTWRITEBYTECODE=1
set MPLBACKEND=Agg
if exist ".venv\Scripts\python.exe" (
  ".venv\Scripts\python.exe" -X utf8 -B review_workbench\launch_workbench.py %*
) else (
  python -X utf8 -B review_workbench\launch_workbench.py %*
)
if errorlevel 1 (
  echo.
  echo Workbench stopped with an error. See review_workbench\README.md.
  pause
)
endlocal
