import shutil
import os

def main():
    # os.system('scp "D:\LFJ\TEST AUTOMATION INTERNSHIP\Tasks\Test1.txt" dms@192.168.229.130:/home/dms/TestsFolder/') # копиіюємо лише 1 файл
    # os.system('scp -r "D:\LFJ\TEST AUTOMATION INTERNSHIP\Tasks" dms@192.168.229.130:/home/dms/TestsFolder/') # копіюємо папку
    print("Enter file(s) or directory which you want to copy into VM")
    command = 'scp -r '
    source = input("objects to move: ")
    command += source
    destination = input("where to move: ")
    command += ' ' + destination

    os.system(command)




if __name__ == "__main__":
    main()




# destination = os.path.join(destination, os.path.basename(source)) # копіює одразу папку

# dest = shutil.copytree(source,destination,dirs_exist_ok=True) #копіює файл

# scp "D:\LFJ\TEST AUTOMATION INTERNSHIP\Tasks\Test1.txt" dms@192.168.229.130:/home/dms/


#"D:\LFJ\TEST AUTOMATION INTERNSHIP\Tasks\Test1.txt"
#D:\LFJ\TEST AUTOMATION INTERNSHIP\Test_folder\Test1.txt
#dms@192.168.229.130:/home/dms/TestsFolder/