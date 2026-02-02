import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("server_ip", username="user", password="pass")

stdin, stdout, stderr = client.exec_command("ls")
print(stdout.read().decode)

client.close()