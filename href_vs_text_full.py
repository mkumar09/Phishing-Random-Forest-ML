import re
import os
import tldextract
import csv

p = re.compile(r' - ')
srcdir = r'C:\Users\Megha Agrawal\Desktop\project\codes\preprocessing_dataset\preprocess_3\spam_2\url_html'
dstdir = r'C:\Users\Megha Agrawal\Desktop\project\codes\attributes\href_vs_text\spam_2.csv'
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
        if re.search(p,r) == None:
            pass
        else:
            a=r.split(' - ')
            ext = tldextract.extract(a[0])
            ext1 = tldextract.extract(a[1])
            ex=ext.domain
            ex1=ext1.domain
            #print ex
            #print ex1
            
            if ex != ex1:
                flag=1
                break
    if flag==1:
        fp1.write('1')
    else:
        fp1.write('0')

    fp1.write('\n')
fp1.close()
        
