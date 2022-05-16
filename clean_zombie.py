import sys
import os
from pathlib import Path

def main(args):
    if(len(args)<2):
        sys.stderr.write("Usage: {} [image folder path] [0:CVAT data|1: unlabel image]\n".format(args[0]))
        sys.exit(1)
    if len(args)== 3:
        user_input = args[2]
        assert os.path.exists(user_input),  "\n" + str(user_input) +", This path does not exist" 
        if args[3] == '0':
            clean_empty_txt(user_input+"/")
        elif args[3] == '1':
            clean_image(user_input+"/")
        else:
            print(" Invalid argument for program \n")
            sys.exit(1)
        
        
    

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
 


if __name__ == '__main__':
    sys.exit(main(sys.argv))

    
