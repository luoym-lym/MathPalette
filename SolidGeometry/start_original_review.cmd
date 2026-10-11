@echo off
setlocal
chcp 65001 >nul
cd /d "%~dp0.."
if defined MATHPALETTE_PYTHON (
  "%MATHPALETTE_PYTHON%" -X utf8 -B "SolidGeometry\original_review\launch_workbench.py" %*
  goto finished
)
if exist ".venv\Scripts\python.exe" (
  ".venv\Scripts\python.exe" -X utf8 -B "SolidGeometry\original_review\launch_workbench.py" %*
  goto finished
)
where py >nul 2>nul
if not errorlevel 1 (
  py -3 -X utf8 -B "SolidGeometry\original_review\launch_workbench.py" %*
  goto finished
)
where python >nul 2>nul
if not errorlevel 1 (
  python -X utf8 -B "SolidGeometry\original_review\launch_workbench.py" %*
  goto finished
)
echo 未找到 Python。请先安装 Python 3.13.9，再按照 SolidGeometry\original_review\README.md 准备依赖。
pause
exit /b 1
:finished
if errorlevel 1 (
  echo.
  echo 原题审核启动失败。请查看上方原因及 SolidGeometry\original_review\README.md。
  pause
  exit /b 1
)
endlocal
