#!/usr/bin/python
# FileName: Subsampling.py
# Version 1.0 by Tao Ban, 2010.5.26
# This function extract all the contents, ie subject and first part from the .eml file
# and store it in a new file with the same name in the dst dir.

import email.parser
import os
import re
import urllib2
#from urlextract import URLExtract
import sys
import stat
import shutil
import pyzmail


def ExtractSubPayload(filename):
    ''' Extract the subject and payload from the .eml file.

    '''
    if not os.path.exists(filename):  # dest path doesnot exist
        print("ERROR: input file does not exist:" + filename)
        os.exit(1)
    fp = open(filename)
    msg=fp.read()
    
    #regex = re.compile(r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))""", re.IGNORECASE)
    #s=re.findall(regex,msg)
    #for st in s:
    #    st=st.replace('\n',' ')
    #str1 = '\n'.join(s)

    extractor = URLExtract()
    urls = extractor.find_urls(msg)  #"Text with URLs. Let's have URL janlipovsky.cz as an example."
    str1 = '\n'.join(urls)
    return  str1


def ExtractBodyFromDir(srcdir, dstdir):
    '''Extract the body information from all .eml files in the srcdir and 

    save the file to the dstdir with the same name.'''
    if not os.path.exists(dstdir):  # dest path doesnot exist
        os.makedirs(dstdir)
    files = os.listdir(srcdir)
    for file in files:
        srcpath = os.path.join(srcdir, file)
        dstpath = os.path.join(dstdir, file)
        src_info = os.stat(srcpath)
        if stat.S_ISDIR(src_info.st_mode):  # for subfolders, recurse
            ExtractBodyFromDir(srcpath, dstpath)
        else:  # copy the file
            body = ExtractSubPayload(srcpath)
            dstfile = open(dstpath, 'w')
            dstfile.write(body)
            dstfile.close()


###################################################################
# main function start here
# srcdir is the directory where the .eml are stored
print('Input source directory: ')  # ask for source and dest dirs
srcdir = input()
if not os.path.exists(srcdir):
    print('The source directory %s does not exist, exit...' % (srcdir))
    sys.exit()
# dstdir is the directory where the content .eml are stored
print('Input destination directory: ')  # ask for source and dest dirs
dstdir = input()
if not os.path.exists(dstdir):
    print('The destination directory is newly created.')
    os.makedirs(dstdir)

###################################################################
ExtractBodyFromDir(srcdir, dstdir)
