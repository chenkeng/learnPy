def add(a,b):
    print "adding %d + %d" %(a,b)
    return a+b

def subtract(a,b):
    print "subtracting %d - %d" %(a,b)
    return a-b

def multiply(a,b):
    print "multiplying %d * %d" %(a,b)
    return a*b

def divide(a,b):
    print "dividing %d / %d" %(a,b)
    return a/b

print "let's do some math with just function !"

age =add (28,3)
height=subtract(182,10)
weight=multiply(140,2)
iq=divide(200,3)

print "Age: %d, height :%d , weight : %d , iq %d " %(age,height,weight,iq)


print "here is a puzzle ."

what =add (age, subtract(height,multiply(weight,divide(iq,2))))


print "that becomes:",what,"can you do it by hand ?"

