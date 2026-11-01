$ErrorActionPreference = 'Stop'
$taskRoot = Join-Path (Get-Location) 'runtime/mathvision_special_20261101/background_03'
$taskEvidence = Join-Path $taskRoot 'Solid238/subrange_14_binding/tests/quicktest3_20261101T114434_58d20adf0562'
$taskStarted = Get-Content -LiteralPath (Join-Path $taskEvidence 'run_02_started.json') -Encoding utf8 -Raw | ConvertFrom-Json
$taskElapsed = ([DateTimeOffset]::UtcNow - [DateTimeOffset]::Parse($taskStarted.started_at)).TotalSeconds
if (Test-Path -LiteralPath (Join-Path $taskEvidence 'run_02.json')) {
    Write-Output 'Request finished; no stop performed.'
    exit 0
}
if ($taskElapsed -lt 300) {
    Write-Output "Still within observation window ($taskElapsed seconds); no stop performed."
    exit 0
}
$taskProcess = Get-CimInstance Win32_Process -Filter 'ProcessId = 18840'
if ($null -eq $taskProcess) { throw 'Expected process absent; inspect request state before recording any termination.' }
$taskExpected = 'runtime/mathvision_special_20261101/background_03/run_root_test.py Solid238 subrange_14_binding'
if (($taskProcess.Name -notmatch '^python(\.exe)?$') -or (-not $taskProcess.CommandLine.Contains($taskExpected))) {
    throw 'PID/command-line verification failed; refusing to stop.'
}
$taskRecord = [ordered]@{
    question_id='Solid238'; variant_id='subrange_14_binding'; run_index=2;
    status='aborted_after_stall'; reason='No response for more than five minutes; finite checkpoint; no automatic retry.';
    recorded_at=[DateTimeOffset]::UtcNow.ToString('o'); elapsed_seconds_at_abandon=[Math]::Round($taskElapsed,3);
    verified_process_id=$taskProcess.ProcessId; verified_parent_process_id=$taskProcess.ParentProcessId;
    verified_process_created_at=$taskProcess.CreationDate.ToUniversalTime().ToString('o');
    verified_command_line=$taskProcess.CommandLine; run_started_evidence='run_02_started.json';
    request_binding='binding.json'; answer_valid_for_two_hit=$false;
    local_request_timeout_or_profile_changed=$false; automatic_retry=$false
}
$taskRecord | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $taskEvidence 'run_02_aborted.json') -Encoding utf8
Stop-Process -Id $taskProcess.ProcessId -ErrorAction Stop
$taskAfter = Get-CimInstance Win32_Process -Filter 'ProcessId = 18840'
if ($null -ne $taskAfter) { throw 'Stopped process still visible; verify cleanup.' }
[ordered]@{stopped_only_verified_own_process=18840; no_longer_live=$true; recorded_at=[DateTimeOffset]::UtcNow.ToString('o')} |
    ConvertTo-Json | Set-Content -LiteralPath (Join-Path $taskEvidence 'process_cleanup.json') -Encoding utf8
Write-Output 'Verified own Solid238 process 18840 stopped; pending/aborted evidence retained; no retry.'
