import sys
import os
from pathlib import Path

user_input = input("Enter the path of your file: ")
assert os.path.exists(user_input),  "\n" + str(user_input) +", This path does not exist"

def clean_empty_txt(path):
    dir_list = os.listdir(path)
    for txt in dir_list:
        if txt.endswith(".txt"):
            if not os.path.getsize(path+txt):
                print(txt)
                y=os.path.splitext(txt)[0]
                s = Path(path+y+".jpg")
                if s.is_file():
                    print("### removing respective image ###\n",s)
                    os.remove(s)
                os.remove(path+txt)
            else:
                continue

def clean_image(path):
    dir_list = os.listdir(path)
    for x in dir_list:
        if x.endswith(".jpg"):
            #print(x)
            y=os.path.splitext(x)[0]
            k = Path(path+y+".txt")
            #print(k)
            if k.is_file():
                print("txt file present\n", s)
            else:
                print("!!!!!!!!!!!!!!!!removing jpg file!!!!!!!!!!!!\n")
                os.remove(path+x)
 
#clean_image(user_input+"/")
clean_empty_txt(user_input+"/")


    
