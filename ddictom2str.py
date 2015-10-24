#! /usr/bin/env python3
# # -*- coding: utf-8 -*-

import os
import sys
import argparse

#-------------------------------------------------------------------------------
def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', default="./txtdir", type=str, action='store', dest='dirL', help='folders with txt files')
    parser.add_argument('-r', '--remove', default=False, type=bool, action='store', dest='rmFl', help='input file - remove or not')
    return parser
#-------------------------------------------------------------------------------
def findFiles(catalog, suffix):
    list4files = []
    for root, dirs, files in os.walk(catalog):
        list4files += [os.path.join(root, name) for name in files if name.endswith(suffix) ]
    return list4files
#-------------------------------------------------------------------------------
# mas_text = [line for line in text_file.xreadline()]
# mas_text = [post_condition(line) and line for line in text_file.xreadline()]
def dictom2line(Frx, Ftx):
    buff4File = Frx.readlines()
    g = ""
    for line in buff4File:
        g += line.replace(".", ".\n")
    tmp = ""
    dbf = []
    for line in g.split("\n"):
	    if(0 <= line.find(".")):
	        tmp += line
	        dbf += tmp.strip()+"\n"
	        tmp  = ""
	    else:
	        tmp += line
    Ftx.writelines(dbf)
    return
#-------------------------------------------------------------------------------
def walkAndMKD(directory):
    if os.path.isdir(directory):
        try:
            os.mkdir(directory.replace("/", "/d2l_"), 0755)
        except OSError:
            if os.path.exists(directory.replace("/", "/d2l_")): pass
            else: raise
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isdir(path):
            walkAndMKD(path)
#-------------------------------------------------------------------------------

createParser()
parser   = createParser()
clavname = parser.parse_args(sys.argv[1:])
walkAndMKD(clavname.dirL)

for FN in findFiles(clavname.dirL, ".txt"):
    fr = open(FN,                       'r')
    fw = open(FN.replace("/", "/d2l_"), 'w')
    dictom2line(fr, fw)
    fr.close()
    fw.close()
    if (clavname.rmFl): os.remove(FN)
    d, f = os.path.split(FN.replace("/", "/d2l_"))
    print (f+" naw is OK!")

