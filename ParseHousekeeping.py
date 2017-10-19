import glob
import os

def FindFile():
    list_of_files =  glob.glob('/Users/cdrunnion/Documents/UNITE_Enviro_Test/*.log')
    recent_file = max(list_of_files, key=os.path.getctime)
    return recent_file 
def BuildList():
    file_Path = FindFile();
    with open(file_Path) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content
def main():

   theList = BuildList();
   print(theList)


if __name__ == "__main__":
    main()

