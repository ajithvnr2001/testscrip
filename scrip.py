Here is the full code:
```
$startTime = Get-Date
while ($(Get-Date).Subtract($startTime).TotalHours -le 2) {
    Write-Host "System is still running..." $(Get-Date)
    Start-Sleep -Seconds 5
}
Write-Host "Script finished executing at" $(Get-Date)
```
This script will run for 2 hours, printing a message to the console every 5 seconds indicating that the system is still running, and finally printing a message when the script finishes executing.
