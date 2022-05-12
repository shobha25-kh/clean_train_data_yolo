import os
from pathlib import Path
path = "./obj/" #folder path

def clean_image(path):
    dir_list = os.listdir(path)
    for x in dir_list:
        if x.endswith(".jpg"):
            #print(x)
            y=os.path.splitext(x)[0]
            z = ".txt"
            s = y + z
            k = Path(path+s)
            #print(k)
            if k.is_file():
                print("txt file present\n", s)
            else:
                print("!!!!!!!!!!!!!!!!removing jpg file!!!!!!!!!!!!\n")
                os.remove(path+x)
 
clean_image(path)
def clean_empty_txt(path):
    dir_list = os.listdir(path)
    for txt in dir_list:
        if txt.endswith(".txt"):
            if not os.path.getsize(path+txt):
                print(txt)
                y=os.path.splitext(txt)[0]
                z = ".jpg"
                s = y + z
                k = Path(path+s)
                print("remove respective image\n",s)
                if k.is_file():
                    os.remove(path+s)
                os.remove(path+txt)
                #k = Path(path+s)
            else:
                pass
			
clean_empty_txt(path)

    
