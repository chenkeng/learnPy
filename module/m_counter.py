#!/usr/bin/env python3
from collections import Counter
c=Counter('http://www.alipay.com')

print(c)

for key in c:
    print(key,c[key])

# the most common letter

print(c.most_common(3))