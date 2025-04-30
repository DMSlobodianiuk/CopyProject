import shutil
import os

def main():
    print("Enter file(s) or directory that you want to copy into VM")
    command = 'scp -r '
    source = input("objects to move: ")
    command += source
    destination = input("where to move: ")
    command += ' ' + destination

    os.system(command)




if __name__ == "__main__":
    main()




