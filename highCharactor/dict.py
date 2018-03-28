#!/usr/bin/env python3
import os
import json

d={'a':1,'b':2,'c':3,'d':4}

obj={k:v*v for k,v in d.items()}
print(obj)
print(json.dumps(obj))


