#!/usr/bin/env python3 
from collections import OrderedDict 
import json

d=OrderedDict()
d['apple']=1
d['google']=2
d['facebook']=3
d['baidu']=4

print(d)

for key in d:
    print(key,d[key])


print(json.dumps(d))


