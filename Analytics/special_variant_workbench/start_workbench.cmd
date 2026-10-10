@echo off
setlocal
cd /d "%~dp0"
echo MathPalette C workbench - http://127.0.0.1:8766
python -B server.py --open-browser %*
if errorlevel 1 (
  echo Install dependencies with: python -m pip install -r requirements.txt
  pause
)
endlocal
