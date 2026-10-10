@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
set "PYTHONIOENCODING=utf-8"
set "WORKBENCH_PYTHON=python"
python -c "import sys; assert sys.version_info >= (3,12)" >nul 2>&1
if errorlevel 1 goto failed
python -c "import matplotlib,numpy,PIL; assert (matplotlib.__version__,numpy.__version__,PIL.__version__)==('3.11.2','2.5.3','12.3.0')" >nul 2>&1
if errorlevel 1 (
    if not exist ".venv\Scripts\python.exe" (
        echo 正在建立本地 Python 环境...
        python -m venv .venv
        if errorlevel 1 goto failed
    )
    ".venv\Scripts\python.exe" -m pip install -r requirements.txt
    if errorlevel 1 goto failed
    set "WORKBENCH_PYTHON=%~dp0.venv\Scripts\python.exe"
)
"%WORKBENCH_PYTHON%" -B server.py --open-browser
if errorlevel 1 goto failed
exit /b 0
:failed
echo.
echo 启动未完成，请查看以上提示。需要 Python 3.12 或更新版本。
pause
exit /b 1
