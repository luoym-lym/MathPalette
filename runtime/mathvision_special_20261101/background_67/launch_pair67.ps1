param([Parameter(Mandatory=$true)][ValidateSet('Solid140','Solid219','Solid236')][string]$Question)
$ErrorActionPreference='Stop'
$taskProject=(Get-Location).Path
$taskOwn=Join-Path $taskProject 'runtime\mathvision_special_20261101\background_67'
. (Join-Path $taskOwn 'ps_python_prefix.ps1')
python -X utf8 -B (Join-Path $taskOwn 'call_audit67.py') pre $Question
if($LASTEXITCODE -ne 0){throw 'Precall validation failed; no remote process launched'}
$rows=Get-Content -LiteralPath (Join-Path $taskOwn 'copied_frozen_candidates.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$row=$rows | Where-Object { $_.question_id -eq $Question }
$candidate=$row.directory
$taskArgs=@('-X','utf8','-B',(Join-Path $taskOwn 'harness\quicktest3_isolated.py'),'--branch','SolidGeometry','--question',$Question,'--image',(Join-Path $candidate 'candidate.png'),'--design',(Join-Path $candidate 'design.json'),'--output',(Join-Path $candidate 'tests'),'--runs','2')
$stdout=Join-Path $candidate 'harness_stdout.txt'
$stderr=Join-Path $candidate 'harness_stderr.txt'
if((Test-Path -LiteralPath $stdout) -or (Test-Path -LiteralPath $stderr)){throw 'No repeated launch allowed'}
$taskProc=Start-Process -FilePath (Get-Command python).Source -ArgumentList $taskArgs -WorkingDirectory $taskProject -WindowStyle Hidden -RedirectStandardOutput $stdout -RedirectStandardError $stderr -PassThru
$actual=Get-CimInstance Win32_Process -Filter "ProcessId=$($taskProc.Id)"
if(-not $actual -or $actual.CommandLine -notlike "*$taskOwn\harness\quicktest3_isolated.py*--question $Question *--runs 2*"){throw 'Launched own process command could not be verified'}
$record=@{at=[DateTime]::UtcNow.ToString('o');question_id=$Question;pid=$taskProc.Id;parent_pid=$actual.ParentProcessId;exact_command=$actual.CommandLine;arguments=$taskArgs;window_style='Hidden';stdout=$stdout;stderr=$stderr;profile_overrides=@();remote_runs=2;status='running'}
$record | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $candidate 'API_process_started.json') -Encoding UTF8
Write-Output "$Question own API PID $($taskProc.Id) recorded"
$taskProc.WaitForExit()
$taskProc.Refresh()
$record.status='closed'
$record.finished_at=[DateTime]::UtcNow.ToString('o')
$record.exit_code=$taskProc.ExitCode
$record.live_pid_present=[bool](Get-CimInstance Win32_Process -Filter "ProcessId=$($taskProc.Id)" -ErrorAction SilentlyContinue)
$record | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $candidate 'API_process_closed.json') -Encoding UTF8
Get-Content -LiteralPath $stdout -Raw -Encoding UTF8
if($taskProc.ExitCode -ne 0){throw 'Harness process failed; stop subsequent calls'}
python -X utf8 -B (Join-Path $taskOwn 'call_audit67.py') post $Question
if($LASTEXITCODE -ne 0){throw 'Postcall evidence validation failed; stop subsequent calls'}
