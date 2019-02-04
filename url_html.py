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
#from html.parser import HTMLParser
from HTMLParser import HTMLParser

class URLParser(HTMLParser):
    def __init__(self):
        self.in_link = False
        self.links = []
        self.current_link = ''
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.current_link = self.get_href_from_attrs(attrs)
            self.in_link = True

    def handle_endtag(self, tag):
        if tag == 'a':
            self.links.append(self.current_link)
            self.in_link = False

    def handle_data(self, data):
        if self.in_link:
            self.current_link = '%s - %s' % (self.current_link, data)

    def get_href_from_attrs(self, attrs):
        # The attrs dict is a list of tuples like:
        #  [('href', 'www.google.com'), ('class', 'some-class')]
        for prop, val in attrs:
            if prop == 'href':
                return val
        return ''



def ExtractSubPayload(filename):
    ''' Extract the subject and payload from the .eml file.

    '''
    if not os.path.exists(filename):  # dest path doesnot exist
        print("ERROR: input file does not exist:" + filename)
        exit(1)
    fp = open(filename)
    msg=fp.read()
    fp.close()
    url_parser = URLParser()
    url_parser.feed(msg)

    str1='\n'.join(url_parser.links)

    fp.close()
    return  str1


def ExtractBodyFromDir(srcdir,srcdir2,dstdir):
    '''Extract the body information from all .eml files in the srcdir and 

    save the file to the dstdir with the same name.'''
    if not os.path.exists(dstdir):  # dest path doesnot exist
        os.makedirs(dstdir)
    files = os.listdir(srcdir)
    for file in files:
        print(file)
        x,y=file.split('.')
        y=x+'.txt'
        z=x+'.html'
        srcpath = os.path.join(srcdir, z)
        srcpath2 = os.path.join(srcdir, y)
        dstpath = os.path.join(dstdir, file)
        src_info = os.stat(srcpath)
        src_info2 = os.stat(srcpath2)
        if stat.S_ISDIR(src_info.st_mode):  # for subfolders, recurse
            ExtractBodyFromDir(srcpath,srcdir2,dstdir)
        elif stat.S_ISDIR(src_info2.st_mode):  # for subfolders, recurse
            ExtractBodyFromDir(srcpath,srcdir2,dstdir)
            
        else:  # copy the file
            fp=open(srcpath2)
            msg=fp.read()
            fp.close()

            body = ExtractSubPayload(srcpath)
            bod= msg + body
            dstfile = open(dstpath, 'w')
            dstfile.write(bod)
            dstfile.close()


###################################################################
# main function start here
# srcdir is the directory where the .eml are stored
if __name__ == '__main__':
    print('Input source directory html part: ')  # ask for source and dest dirs
    srcdir = input()
    if not os.path.exists(srcdir):
        print('The source directory %s does not exist, exit...' % (srcdir))
        sys.exit()
    print('Input source directory body part: ')  # ask for source and dest dirs
    srcdir2 = input()
    if not os.path.exists(srcdir):
        print('The source directory %s does not exist, exit...' % (srcdir))
        sys.exit()
    #dstdir is the directory where the content .eml are stored
    print('Input destination directory: ')  # ask for source and dest dirs
    dstdir = input()
    if not os.path.exists(dstdir):
        print('The destination directory is newly created.')
        os.makedirs(dstdir)

    ###################################################################
    ExtractBodyFromDir(srcdir,srcdir2,dstdir)
