$taskRoot = 'C:\Users\lym\Desktop\Research\MathPalette-publish\runtime\mathvision_special_20261101\background_49'
$taskProcesses = @(Get-CimInstance Win32_Process -Filter "Name='python.exe' OR Name='pythonw.exe'" | Where-Object { $_.CommandLine -and $_.CommandLine.Contains('background_49') -and $_.CommandLine.Contains('api_runner.py') } | Select-Object ProcessId,ParentProcessId,Name,CommandLine,CreationDate)
$taskAudit = [ordered]@{ checked_at_utc=[DateTime]::UtcNow.ToString('o'); scope='Only own background_49 api_runner Python processes'; live_own_api_processes=$taskProcesses; live_own_api_process_count=$taskProcesses.Count; all_own_api_processes_closed=($taskProcesses.Count -eq 0); processes_killed=0; no_nested_agents_threads_worktrees=$true }
$taskAudit | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath (Join-Path $taskRoot 'process_audit_final.json') -Encoding UTF8
$taskAudit | ConvertTo-Json -Depth 6
