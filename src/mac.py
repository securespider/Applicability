import getpass
import subprocess
import time


"""

"""
def main():
    command = 'sudo -S powermetrics --show-process-energy -n1'.split()
    password = getpass.getpass("Please enter your sudo password: ")
    cmd2 = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cmd2.communicate(password.encode())
    stdout, stderr = cmd2.communicate()
    lines = stdout.decode().split("\n")
    for line in lines:
        print(line)
    # for i in range(10):
    #     output = cmd2.stdout.read().decode()
    #     print(output)
    #     time.sleep(1)

if __name__ == '__main__':
    main()
