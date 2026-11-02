param([Parameter(Mandatory=$true)][string]$Script,[Parameter(ValueFromRemainingArguments=$true)][string[]]$ScriptArgs)
$ErrorActionPreference='Stop'
$ownRoot=$PSScriptRoot
foreach($key in @('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS')) { [Environment]::SetEnvironmentVariable($key,'1','Process') }
foreach($entry in @{TEMP='tmp';TMP='tmp';MPLCONFIGDIR='mpl_cache';XDG_CACHE_HOME='cache'}.GetEnumerator()) {
    $dir=Join-Path $ownRoot $entry.Value
    New-Item -ItemType Directory -Path $dir -Force | Out-Null
    [Environment]::SetEnvironmentVariable($entry.Key,$dir,'Process')
}
python -X utf8 -B (Join-Path $ownRoot $Script) @ScriptArgs
exit $LASTEXITCODE
