import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname="server.example.com",
    username="admin",
    key_filename="~/.ssh/id_rsa"
)
stdin, stdout, stderr = ssh.exec_command("uptime")
print(stdout.read().decode())

ssh.close()