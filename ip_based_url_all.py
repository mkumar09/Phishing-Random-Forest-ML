import re
import os
import tldextract
import csv

p = re.compile(r' - ')
p1=re.compile(r'([1][0-9][0-9]\.|[2][5][0-5]\.|[2][0-4][0-9]\.|[1][0-9][0-9]\.|[0-9][0-9]\.|[0-9]\.)([1][0-9][0-9]\.|[2][5][0-5]\.|[2][0-4][0-9]\.|[1][0-9][0-9]\.|[0-9][0-9]\.|[0-9]\.)([1][0-9][0-9]\.|[2][5][0-5]\.|[2][0-4][0-9]\.|[1][0-9][0-9]\.|[0-9][0-9]\.|[0-9]\.)([1][0-9][0-9]|[2][5][0-5]|[2][0-4][0-9]|[1][0-9][0-9]|[0-9][0-9]|[0-9])')


srcdir = r'C:\Users\Megha Agrawal\Desktop\project\codes\preprocessing_dataset\preprocess_3\spam_2\url_2'
dstdir = r'C:\Users\Megha Agrawal\Desktop\project\codes\attributes\ip_based_url\spam_2.csv'
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
        a=r.split(' - ')
        msg=a[0]
    
        if re.search(p1, msg) != None:
            print(re.search(p1, msg))
            flag=1
            break
    if flag==1:
        fp1.write('1')
    else:
        fp1.write('0')

    

    fp1.write('\n')
fp1.close()
        
