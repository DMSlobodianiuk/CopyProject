import shutil
import os

def main():
    # os.system('scp "D:\LFJ\TEST AUTOMATION INTERNSHIP\Tasks\Test1.txt" dms@192.168.229.130:/home/dms/TestsFolder/')
    command = 'scp '
    source = input("file to move: ")
    command += source
    destination = input("where to move: ")
    command += ' ' + destination

    os.system(command)


    # destination = os.path.join(destination, os.path.basename(source)) # копіює одразу папку

    # dest = shutil.copytree(source,destination,dirs_exist_ok=True) #копіює файл


if __name__ == "__main__":
    main()

C


# scp "D:\LFJ\TEST AUTOMATION INTERNSHIP\Tasks\Test1.txt" dms@192.168.229.130:/home/dms/


#"D:\LFJ\TEST AUTOMATION INTERNSHIP\Tasks\Test1.txt"
#D:\LFJ\TEST AUTOMATION INTERNSHIP\Test_folder\Test1.txt
#dms@192.168.229.130:/home/dms/TestsFolder/