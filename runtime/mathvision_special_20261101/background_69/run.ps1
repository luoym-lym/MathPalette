param([Parameter(ValueFromRemainingArguments=$true)][string[]]$TaskArgs)
$unitRoot=$PSScriptRoot
$env:OPENBLAS_NUM_THREADS='1'
$env:OMP_NUM_THREADS='1'
$env:MKL_NUM_THREADS='1'
$env:NUMEXPR_NUM_THREADS='1'
$env:TEMP=Join-Path $unitRoot 'temp'
$env:TMP=Join-Path $unitRoot 'temp'
$env:MPLCONFIGDIR=Join-Path $unitRoot 'mpl'
$env:XDG_CACHE_HOME=Join-Path $unitRoot 'cache'
& python -X utf8 -B @TaskArgs
exit $LASTEXITCODE
