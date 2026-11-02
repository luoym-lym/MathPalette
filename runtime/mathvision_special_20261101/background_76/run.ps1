$ErrorActionPreference='Stop'
$taskRoot=$PSScriptRoot
$env:OPENBLAS_NUM_THREADS='1'
$env:OMP_NUM_THREADS='1'
$env:MKL_NUM_THREADS='1'
$env:NUMEXPR_NUM_THREADS='1'
$env:TEMP=Join-Path $taskRoot 'tmp'
$env:TMP=$env:TEMP
$env:MPLCONFIGDIR=Join-Path $taskRoot 'mpl_cache'
$env:XDG_CACHE_HOME=Join-Path $taskRoot 'cache'
& python -X utf8 -B (Join-Path $taskRoot 'bootstrap.py') @args
exit $LASTEXITCODE
