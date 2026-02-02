#access.log 相当（IISログ）
$Log = "access.log"
$Threshold = 100

Get-Count $Log |
ForEach-Object {
    ($_ -split " ")[0]
} |
Group-Object |
Sort-Object Count -Descending |
Where-Object { $._Count -gt $Threshold } |
ForEach-Object {
    Write-Host "[ALERT]" $_.Name "アクセス数:" $_.Count
}
