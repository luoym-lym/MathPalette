param([Parameter(Mandatory=$true)][string]$Script, [Parameter(ValueFromRemainingArguments=$true)][string[]]$ScriptArgs)
$ErrorActionPreference = 'Stop'
$taskRoot = $PSScriptRoot
foreach ($folder in @('tmp','mpl_cache','cache')) {
    New-Item -ItemType Directory -Path (Join-Path $taskRoot $folder) -Force | Out-Null
}
$env:OPENBLAS_NUM_THREADS = '1'
$env:OMP_NUM_THREADS = '1'
$env:MKL_NUM_THREADS = '1'
$env:NUMEXPR_NUM_THREADS = '1'
$env:TEMP = Join-Path $taskRoot 'tmp'
$env:TMP = Join-Path $taskRoot 'tmp'
$env:MPLCONFIGDIR = Join-Path $taskRoot 'mpl_cache'
$env:XDG_CACHE_HOME = Join-Path $taskRoot 'cache'
& python -X utf8 -B (Join-Path $taskRoot $Script) @ScriptArgs
exit $LASTEXITCODE
