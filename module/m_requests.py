#!/usr/bin/env python3
import  requests
site=requests.get('https://www.shiyanlou.com')
print(site.status_code)
print(site.headers)

print("*******")
print(site.text)

sitejson=requests.get('https://api.github.com')
print(sitejson.json())