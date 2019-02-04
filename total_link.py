import re
import os
import csv

srcdir = r'C:\Users\Megha Agrawal\Desktop\project\codes\preprocessing_dataset\preprocess_3\easy_ham\acc_url'
#srcdir1 = r'C:\Users\Megha Agrawal\Desktop\project\codes\preprocessing_dataset\preprocess_3\easy_ham_2\url_html'
dstdir = r'C:\Users\Megha Agrawal\Desktop\project\codes\attributes\total_link\easy_ham.csv'
fp1=open(dstdir,'w')
files = os.listdir(srcdir)
for file in files:
    srcpath = os.path.join(srcdir, file)
    #srcpath1 = os.path.join(srcdir1, file)
    fp=open(srcpath)
    msg=fp.read()
    fp.close()
    arr=msg.split('\n')
    a=len(arr)
    #fp=open(srcpath1)
    #msg=fp.read()
    #fp.close()
    #arr=msg.split('\n')
    #z=a+len(arr)
    fp1.write(str(a))
    fp1.write('\n')
fp1.close()
        
