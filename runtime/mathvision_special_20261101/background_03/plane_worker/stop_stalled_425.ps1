param([Parameter(Mandatory=$true)][ValidateSet('paired_endpoint_links','single_endpoint_radius_trap')][string]$Variant)
$ErrorActionPreference = 'Stop'
$ownedDirectory = (Resolve-Path -LiteralPath $PSScriptRoot).Path
if ($Variant -eq 'paired_endpoint_links') { $ownedProcessId=41568; $expected='B' }
else { $ownedProcessId=3204; $expected='D' }
$testsDirectory = Join-Path $ownedDirectory ('Plane425/' + $Variant + '/tests')
$invocations = @(Get-ChildItem -LiteralPath $testsDirectory -Directory)
if ($invocations.Count -ne 1) { throw 'Expected exactly one immutable invocation; no retries.' }
$evidenceDirectory = $invocations[0].FullName
$runIndex = 1
if (Test-Path -LiteralPath (Join-Path $evidenceDirectory 'run_01.json')) { $runIndex=2 }
$runName = 'run_{0:d2}' -f $runIndex
$startedPath = Join-Path $evidenceDirectory ($runName + '_started.json')
$finishedPath = Join-Path $evidenceDirectory ($runName + '.json')
if (Test-Path -LiteralPath $finishedPath) { Write-Output 'Response completed; no process stopped.'; exit 0 }
if (-not (Test-Path -LiteralPath $startedPath)) { Write-Output 'No pending started request; no process stopped.'; exit 0 }
$started = Get-Content -LiteralPath $startedPath -Raw -Encoding utf8 | ConvertFrom-Json
$elapsed = ([DateTimeOffset]::UtcNow - [DateTimeOffset]::Parse($started.started_at)).TotalSeconds
if ($elapsed -le 300) { throw 'Request has not stalled for more than five minutes.' }
$ownedProcess = Get-CimInstance Win32_Process -Filter ('ProcessId=' + $ownedProcessId)
if ($null -eq $ownedProcess) { Write-Output 'Owned process already exited; no process stopped.'; exit 0 }
$requiredCommand = '*background_03/plane_worker/test_new.py Plane425/' + $Variant + '*'
if ($ownedProcess.Name -notlike 'python*' -or $ownedProcess.CommandLine -notlike $requiredCommand) { throw 'PID command line no longer matches this worker request.' }
$aborted = [ordered]@{status='aborted';run_index=$runIndex;verified_pid=$ownedProcess.ProcessId;verified_command_line=$ownedProcess.CommandLine;recorded_at=[DateTimeOffset]::UtcNow.ToString('o');elapsed_seconds=$elapsed;reason='No response after more than five minutes; abandoned for finite checkpoint. Not completed; no retry.';started_evidence=$startedPath;expected_wrong_answer=$expected;request_body_sha256=$started.request_body_sha256;image_sha256=$started.image_sha256;design_sha256=$started.design_sha256;count_as_valid_test=$false;retry_performed=$false}
$abortPath = Join-Path $evidenceDirectory ($runName + '_aborted_by_worker.json')
if (Test-Path -LiteralPath $abortPath) { throw 'Abort evidence exists; refusing overwrite.' }
$aborted | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $abortPath -Encoding utf8
Stop-Process -Id $ownedProcess.ProcessId -Force
$remaining = Get-CimInstance Win32_Process -Filter ('ProcessId=' + $ownedProcessId)
if ($null -ne $remaining -and $remaining.CommandLine -eq $ownedProcess.CommandLine) { throw 'Owned stalled process still alive.' }
Write-Output ('Verified own stalled Plane425/' + $Variant + ' process stopped; immutable abort evidence preserved.')
