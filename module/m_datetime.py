#!/usr/bin/env  python3
from datetime import date,datetime,timedelta

t_now=date.today()
print(t_now)

utcnow=datetime.utcnow()
print(utcnow)

t=datetime.now()
print(t)

print(t.day)
print(t.year)
print(t.minute)

#------------------------------

# to        string 
ttt=datetime.strftime(t,'%Y-%m-%d %H:%M:%S')
print(ttt)
# to  datetime 

mmm=datetime.strptime('2017-10-01 00:00:00','%Y-%m-%d %H:%M:%S')
print(mmm)





