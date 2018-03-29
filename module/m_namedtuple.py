#!/usr/bin/env python3
from collections import namedtuple

Point=namedtuple('Point',['x','y','z'])
p=Point(10,20,40)
print(p)
print(p.x)
print(p.y)
print(p.z)