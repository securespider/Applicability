import sys
import Mac
import Windows
import Linux

OS = ["mac", "windows", "linux"]

def main():
    operating_system = input("what is your operating system[mac, windows, linux]: ")
    while operating_system not in OS:
        operating_system = input("what is your operating system[mac, windows, linux]: ")
    if operating_system == "mac":
        Mac.execute()
    elif operating_system == "windows":
        Windows.execute()
    else:
        Linux.execute()

if __name__ == '__main__':
    main()


