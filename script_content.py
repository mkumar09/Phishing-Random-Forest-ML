import re
import os
import csv

srcdir = r'C:\Users\Megha Agrawal\Desktop\project\codes\preprocessing_dataset\preprocess_2\easy_ham\html_part'
dstdir = r'C:\Users\Megha Agrawal\Desktop\project\codes\attributes\script_containt\easy_ham.csv'
fp1=open(dstdir,'w')
files = os.listdir(srcdir)
pstart = re.compile(r'<script>', re.I | re.S)
pstart1 = re.compile(r'<script ', re.I | re.S)
pend = re.compile(r'</script>', re.I | re.S)
for file in files:
    srcpath = os.path.join(srcdir, file)
    #srcpath1 = os.path.join(srcdir1, file)
    fp=open(srcpath)
    msg=fp.read()
    fp.close()
    r=0
    if re.search(pstart, msg) != None or re.search(pstart1, msg) != None:
        if re.search(pend,msg) != None:
            r=1
    a=str(r)
    fp1.write(str(a))
    fp1.write('\n')
fp1.close()
        
