import re
import os
import tldextract
import csv

p = re.compile(r' - ')


srcdir = r'C:\Users\Megha Agrawal\Desktop\project\codes\preprocessing_dataset\preprocess_3\hard_ham\acc_url'
dstdir = r'C:\Users\Megha Agrawal\Desktop\project\codes\attributes\more_dot\hard_ham.csv'
fp1=open(dstdir,'w')
files = os.listdir(srcdir)
for file in files:
    srcpath = os.path.join(srcdir, file)

    fp=open(srcpath)
    msg=fp.read()
    fp.close()
    arr=msg.split('\n')
    flag=0
    for r in arr:
        print r
        a=r.split(' - ')
        b=a[0].split('.')
        if len(b) > 3:
            flag=1
            print(b)
            break
    if flag==1:
        fp1.write('1')
    else:
        fp1.write('0')

    

    fp1.write('\n')
fp1.close()
        
