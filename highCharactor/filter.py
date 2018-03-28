#!/usr/bin/env python3
import json
num=[1,2,3,4,5,6,7,8,9]

f=filter(lambda x:x%2==1,num)
print(f)
#print(json.dumps(f))

for i in f:
    print(i)

