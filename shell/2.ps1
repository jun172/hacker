$threshold = 5
$FailedLogins = @{}

Get-WinEvent -FilterHashtable @{
    Lognmae = 'Security'
    ID =4625 #ログイン失敗
} | FprEach-Object {

    $ip = $_Properties[19].Value

    if ($ip) {
        if ($FailedLogins.ContainsKey($ip)) {
            $FailedLogins[$ip]++
        } else {
            $FailedLogins[$ip] = 1
        }
    }
}

Write-Host "=== ブルフォース検知 ==="

$FailedLogins.GetEnumerator() |
sort-object Value -Descending |
ForEach-object {
    if ($_.Value -ge $threshold) {
        Write-Host "[ALERT] IP:" $_.key "失敗回数:" $_.Value
    }
}