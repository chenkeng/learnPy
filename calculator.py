#!/usr/bin/env python3

import sys
print(sys.argv)

if(len(sys.argv)!=2):
    print("Parameter Error")
try:
    int(sys.argv[1])
except:
    print("Parameter Error")

salery=int(sys.argv[1])

income=salery-3500


def result(ratio,base):
    tax=(salery-3500)*ratio-base
    tax="{:.2f}".format(tax)
    print(tax)

if income<=1500:
    result(ratio=0.03,base=0)
elif income>1500 &income<=4500:
    result(ratio=0.1,base=105)
elif income>4500 & income<=9000:
    result(ratio=.2,base=555)
elif income>9000 & income<=35000:
    result(ratio=.25,base=1005)
elif income>35000 & income<=55000:
    result(ratio=.3,base=2755)
elif income>55000 & income<=80000:
    result(ratio=.35,base=5505)
elif income>80000:
    result(ratio=.45,base=13505)

