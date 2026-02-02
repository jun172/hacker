#変数
$log = "access.log"
$threshold = 100
#ファイル読む
Get-Conect error.log | Select-Object -First 10
#grep相当
Select-String "ERROR" error.log
#sort + uniq -c 相当
Get-Conect error.log | 
    Group-Object |
    Select-Object Count -Descending
#error.log から同一エラーを多い順
Get-Conect error.log | 
    Group-Object | 
    sort-object Count -Descending |
    Select-Object -First 10
#PowerShell で IDS 風（DoS兆候検知）
$log = "access.log"
$threshold = 100

Get-Conect $log | 
    ForEach-object { ($_ -split "" )[0] } |
    Group-Object |
    Where-Object { $_ -split -gt $threshold } |
    ForEach-object {
        "[ALERT] $($_.Name)から $($_.Count) 回アクセス"
    }
#