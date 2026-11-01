$ErrorActionPreference = 'Stop'
$ownedDirectory = (Resolve-Path -LiteralPath $PSScriptRoot).Path
$evidenceDirectory = Join-Path $ownedDirectory 'Plane313/false_hole_clock_correspondence/tests/quicktest3_20261101T114445_9c4a050193b4'
$startedPath = Join-Path $evidenceDirectory 'run_02_started.json'
$finishedPath = Join-Path $evidenceDirectory 'run_02.json'
if (Test-Path -LiteralPath $finishedPath) { Write-Output 'Response completed; no process stopped.'; exit 0 }
$started = Get-Content -LiteralPath $startedPath -Raw -Encoding utf8 | ConvertFrom-Json
$elapsed = ([DateTimeOffset]::UtcNow - [DateTimeOffset]::Parse($started.started_at)).TotalSeconds
if ($elapsed -le 300) { throw 'Request has not stalled for more than five minutes.' }
$ownedProcess = Get-CimInstance Win32_Process -Filter 'ProcessId=9432'
if ($null -eq $ownedProcess) { Write-Output 'Owned process already exited; no process stopped.'; exit 0 }
if ($ownedProcess.Name -notlike 'python*' -or $ownedProcess.CommandLine -notlike '*background_03/plane_worker/test_new.py Plane313/false_hole_clock_correspondence*') { throw 'PID command line no longer matches this worker request.' }
$aborted = [ordered]@{status='aborted';run_index=2;verified_pid=$ownedProcess.ProcessId;verified_command_line=$ownedProcess.CommandLine;recorded_at=[DateTimeOffset]::UtcNow.ToString('o');elapsed_seconds=$elapsed;reason='No response after more than five minutes; abandoned for finite checkpoint. This is not a completed test and will not be retried.';started_evidence=$startedPath;expected_wrong_answer='C';request_body_sha256=$started.request_body_sha256;image_sha256=$started.image_sha256;design_sha256=$started.design_sha256;count_as_valid_test=$false;retry_performed=$false}
$abortPath = Join-Path $evidenceDirectory 'run_02_aborted_by_worker.json'
if (Test-Path -LiteralPath $abortPath) { throw 'Abort evidence exists; refusing overwrite.' }
$aborted | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $abortPath -Encoding utf8
Stop-Process -Id $ownedProcess.ProcessId -Force
$remaining = Get-CimInstance Win32_Process -Filter 'ProcessId=9432'
if ($null -ne $remaining -and $remaining.CommandLine -eq $ownedProcess.CommandLine) { throw 'Owned stalled process still alive.' }
Write-Output 'Verified own stalled Plane313 process stopped; immutable abort evidence preserved.'
