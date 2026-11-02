param([Parameter(ValueFromRemainingArguments=$true)][string[]]$Arguments)
$own=Split-Path -Parent $MyInvocation.MyCommand.Path
$env:OPENBLAS_NUM_THREADS='1'
$env:OMP_NUM_THREADS='1'
$env:MKL_NUM_THREADS='1'
$env:NUMEXPR_NUM_THREADS='1'
$env:TEMP=Join-Path $own 'tmp'
$env:TMP=Join-Path $own 'tmp'
$env:MPLCONFIGDIR=Join-Path $own 'mpl_cache'
$env:XDG_CACHE_HOME=Join-Path $own 'cache'
& python -X utf8 -B @Arguments
exit $LASTEXITCODE