#!/usr/bin/env python3

import sys
if len(sys.argv)!=2:
    print('Parameter Error')
    exit()
try:
    int(sys.argv[1])
except:
    print('Parameter Error')
    exit()


salery=int(sys.argv[1])-3500
if salery>=0:
    salery=salery
else:
    salery=0


if salery<=1500:
    ratio=0.03
    initValue=0
    print("the tax is:",format((salery*ratio-initValue),".2f"))
elif salery>1500 & salery<=4500:
    ratio=0.1
    initValue=105
    print("the tax is:",format((salery*ratio-initValue),".2f"))
elif salery>4500 & salery<=9000:
    ratio=0.2
    initValue=555
    print("the tax is:",format((salery*ratio-initValue),".2f"))
elif salery>9000 & salery<=35000:
    ratio=0.25
    initValue=1005
    print("the tax is:",format((salery*ratio-initValue),".2f"))
elif salery>35000 & salery<=55000:
    ratio=0.3
    initValue=2755
    print("the tax is:",format((salery*ratio-initValue),".2f"))
elif salery>55000 & salery<=8000:
    ratio=0.35
    initValue=5505
    print("the tax is:",format((salery*ratio-initValue),".2f"))
elif salery>80000:
    ratio =0.45
    initValue=13505
    print("the tax is:",format((salery*ratio-initValue),".2f"))

   
 

