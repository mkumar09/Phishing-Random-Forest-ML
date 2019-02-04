import re
import os
import csv
import tldextract

def f3(seq):
       # Not order preserving
   keys = {}
   for e in seq:
       keys[e] = 1
   return len(keys.keys())

srcdir = r'C:\Users\Megha Agrawal\Desktop\project\codes\preprocessing_dataset\preprocess_3\spam_2\url_text'
srcdir1 = r'C:\Users\Megha Agrawal\Desktop\project\codes\preprocessing_dataset\preprocess_3\spam_2\url_html'
dstdir = r'C:\Users\Megha Agrawal\Desktop\project\codes\attributes\link_diffrent_domains\spam_2.csv'
fp1=open(dstdir,'w')
files = os.listdir(srcdir)
for file in files:
    srcpath = os.path.join(srcdir, file)
    srcpath1 = os.path.join(srcdir1, file)
    fp=open(srcpath)
    msg=fp.read()
    fp.close()
    arr=msg.split('\n')
    arr1=[]
    for r in arr:
        ext = tldextract.extract(r)
        arr1.append(ext.domain)
        #print arr1

    a=f3(arr1)
    
    fp=open(srcpath1)
    msg=fp.read()
    fp.close()
    arr3=msg.split('\n')
    arr2=[]
    for r in arr3:
        ext = tldextract.extract(r)
        arr2.append(ext.domain)
    z=a+f3(arr2)
    fp1.write(str(a))
    fp1.write('\n')
fp1.close()
        
