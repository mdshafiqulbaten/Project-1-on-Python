import paramiko

def run_command(ip, username, password, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command)
        print(f"Output from {ip}:")
        print(stdout.read().decode())
        ssh.close()
    except Exception as e:
        print(f"Connection to {ip} failed: {e}")

if __name__ == "__main__":
    devices = ["192.168.1.10", "192.168.1.20"]
    user = input("Username: ")
    pwd = input("Password: ")
    cmd = input("Command: ")

    for device in devices:
        run_command(device, user, pwd, cmd)
