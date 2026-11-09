#!/bin/sh
set -eu

branch_dir=$(CDPATH= cd -P -- "$(dirname -- "$0")" && pwd -P)
exec /bin/sh "$branch_dir/../dataset_tools/start_workbench_macos.sh" "$branch_dir" "$@"
