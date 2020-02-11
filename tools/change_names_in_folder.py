import os
import sys
import shutil

if __name__ == "__main__":
    path_src = sys.argv[1]
    print(path_src)
    
    if os.path.isdir(path_src):
        os.chdir(path_src)
        files = os.listdir(path_src)
        for i, filename in enumerate(files):
            print("process {}, {} / {}".format(filename, i+1, len(files)))
            index = filename.rfind("_")
            newfilename = filename[:index] + '_' +filename[index:]
            print(newfilename)
            shutil.move(filename, newfilename)


            
   
