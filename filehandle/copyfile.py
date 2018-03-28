#!/usr/bin/env python3
import sys

def copy_file(src,dest):
    with open(src,'r') as src_file:
        with open(dest,'w') as dest_file:
           dest_file.write(src_file.read())

if __name__=='__main__':
    if len(sys.argv)==3:
        copy_file(sys.argv[1],sys.argv[2])
        print('copy success !')
    else:
        print('Parameter Error')
        print(sys.argv[0],'need scrfile & destfile')
        sys.exit(-1)
    sys.exit(0)

