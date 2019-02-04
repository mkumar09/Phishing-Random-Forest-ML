import re
import os
import csv

srcdir = r'C:\Users\Megha Agrawal\Desktop\project\codes\preprocessing_dataset\preprocess_2\spam_2\html_part'

dstdir = r'C:\Users\Megha Agrawal\Desktop\project\codes\attributes\html_email\spam_2.csv'
fp1=open(dstdir,'w')
files = os.listdir(srcdir)
for file in files:
    srcpath = os.path.join(srcdir, file)
    

    statinfo = os.stat(srcpath)

    if statinfo.st_size > 0:
        fp1.write('1')
    else:
        fp1.write('0')
    
    fp1.write('\n')
        

# print(str)
# print(st)
