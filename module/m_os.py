#!/usr/bin/env python3

import os
pwd =os.getcwd()
print(pwd)

# generate n bite date

nbit=os.urandom(10)
print(nbit)

# create a dir
os.mkdir('newdir')

# create a file
os.mknod(os.getcwd()+ '/app.py')
