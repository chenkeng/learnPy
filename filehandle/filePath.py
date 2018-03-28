#!/usr/bin/env  python3
import os 

filename='/home/shiyanlou/learnPy/test.txt'

abspath=os.path.abspath(filename)

basename=os.path.basename(filename)

dirname=os.path.dirname(filename)

isfile=os.path.isfile(filename)

isdir=os.path.isdir(filename)

exists=os.path.exists(filename)

joinpath=os.path.join('/home/shiyanlou','learnPy/help')

filelist=[abspath,basename,dirname,isfile,isdir,exists,joinpath]

for item in filelist:
    print(item)


