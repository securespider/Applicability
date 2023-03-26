import subprocess
from subprocess import PIPE
import powertop
import json

import getpass
from time import sleep

INIT_PRINT = "Here is all your processes, please input the pid of the specific process"
# powertop = powertop.Powertop()
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
    measures = powertop.Powertop().get_measures(time=1)

    print(json.dumps(measures['Device Power Report'], indent=4))

    # stdout, stderr = powertop.communicate()
    # while stdout:
    #     print(stdout.decode())
    #     stdout = powertop.communicate()
    #
    # sleep(3)

if __name__ == '__main__':
    execute()