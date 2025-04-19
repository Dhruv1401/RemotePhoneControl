## controller.py
import paramiko
from config import PHONE_IP, PORT, USERNAME, PASSWORD, COMMANDS

def run_command(command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(PHONE_IP, PORT, USERNAME, PASSWORD)
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode()
    error = stderr.read().decode()
    ssh.close()
    return output if output else error

if __name__ == "__main__":
    for name, cmd in COMMANDS.items():
        print(f"\n>>> {name.upper()}:")
        print(run_command(cmd))