import subprocess
from subprocess import PIPE
import powertop
import getpass
from time import sleep

INIT_PRINT = "Here is all your processes, please input the pid of the specific process"

"""
Function that runs the Powertop command and extracts information from it for a specific application
"""
def execute():
    print(INIT_PRINT)
    processes = subprocess.run("ps -A".split(), stdout=PIPE)
    print(processes.stdout.decode())
    # number = input("PID: ")
    number = "1"
    while not number.isdigit():
        number = input("PID: ")
    number = int(number)
    # password = getpass.getpass("Sudo password: ")
    password = "I!l2m3t4"
    powertop = subprocess.Popen("sudo -S powertop".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    print(password)
    powertop.communicate(password.encode())
    print(powertop.communicate())
    while True:
        sleep(5)
        print(powertop.communicate())

    # stdout, stderr = powertop.communicate()
    # while stdout:
    #     print(stdout.decode())
    #     stdout = powertop.communicate()
    #
    # sleep(3)

if __name__ == '__main__':
    execute()