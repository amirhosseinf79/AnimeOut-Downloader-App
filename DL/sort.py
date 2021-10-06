import os
import re

files = os.listdir()

# try:
#     os.mkdir("Remake our Life")
#     os.mkdir("Remake our Life/S1 2021")
# except:
#     pass

for file in files:
    if file != "sort.py":
        tmp_name = file
        #(Hi10)_Bokutachi_no_Remake_-_OP01_(720p)_(Subsplease)_(E2902FD9).mkv
        file = re.sub("\[[Aa]nime[Oo]ut\] ","",file)
        file = re.sub("_"," ",file)
        file = re.sub("( 720p(.*))|( 1080p(.*))",".mkv",file)
        print(file)
        os.rename(tmp_name,file)