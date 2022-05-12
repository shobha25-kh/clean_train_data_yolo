import os
from pathlib import Path
path = "./obj/" #folder path
dir_list = os.listdir(path)

for x in dir_list:
    if x.endswith(".jpg"):
        #print(x)
        y=os.path.splitext(x)[0]
        z = ".txt"
        s = y + z
        k = Path("./obj/" +s)
        #print(k)
        if k.is_file():
            print("txt file present\n", s)
        else:
            print("!!!!!!!!!!!!!!!!removing jpg file!!!!!!!!!!!!\n")
            os.remove("./obj/"+x)
        # Prints only text file present in My Folder
