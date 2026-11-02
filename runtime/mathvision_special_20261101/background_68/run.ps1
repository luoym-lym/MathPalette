param([Parameter(Mandatory=$true)][string]$Script, [Parameter(ValueFromRemainingArguments=$true)][string[]]$ScriptArgs)
$ownRuntime = $PSScriptRoot
$env:OPENBLAS_NUM_THREADS='1'
$env:OMP_NUM_THREADS='1'
$env:MKL_NUM_THREADS='1'
$env:NUMEXPR_NUM_THREADS='1'
foreach ($pair in @(@('TEMP','tmp'),@('TMP','tmp'),@('MPLCONFIGDIR','mpl_cache'),@('XDG_CACHE_HOME','cache'))) {
    $target = Join-Path $ownRuntime $pair[1]
    New-Item -ItemType Directory -Path $target -Force | Out-Null
    [Environment]::SetEnvironmentVariable($pair[0], $target, 'Process')
}
& python -X utf8 -B $Script @ScriptArgs
exit $LASTEXITCODE
