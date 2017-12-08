age=28
if age>=18:
    print ("your age is ",age)
    print ("adult")

age=3
if age>=18:
    print('your age is ', age)
    print ('adult')
elif age>=6:
    print ('teenager')
else:
    print('your age is ',age)
    print ('kid')



birth =int(input ('birth:'))
if birth<2000:
    print('00qian')
else:
    print('00hou')


height=1.75
weight=80.5
ibm=weight*weight/(height*height)
if ibm<18.5:
    print("too low")
if ibm<25:
    print ("normal")
if ibm <28:
    print ('overweight')
if ibm <32:
    print('too fat')
if ibm>32:
    print('serious fat')
