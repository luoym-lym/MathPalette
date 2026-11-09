#!/bin/sh
set -eu

branch_dir=$1
shift
project_dir=$(CDPATH= cd -P -- "$branch_dir/.." && pwd -P)

# Frozen MathVision renderers compare temporary paths after resolving them.
# Use a canonical location inside the project's runtime directory on macOS.
runtime_dir="$project_dir/.runtime/macos"
mkdir -p "$runtime_dir/tmp"
export TMPDIR="$(CDPATH= cd -P -- "$runtime_dir/tmp" && pwd -P)"
export MPLCONFIGDIR="${MPLCONFIGDIR:-$runtime_dir/matplotlib}"
export MATHPALETTE_MACOS=1

if [ -n "${MATHPALETTE_PYTHON:-}" ]; then
    python="$MATHPALETTE_PYTHON"
elif [ -x "$project_dir/.venv/bin/python" ]; then
    python="$project_dir/.venv/bin/python"
elif [ -x "$project_dir/venv/bin/python" ]; then
    python="$project_dir/venv/bin/python"
else
    python=$(command -v python3) || {
        printf '%s\n' '需要 Python 3。请按根目录 README 配置 .venv。' >&2
        exit 1
    }
fi

exec "$python" -X utf8 -B "$branch_dir/workbench/launch_workbench.py" "$@"
