tenthings=" apples oranges crows telephone light sugar"
print "wait there's not 10 things in that list, let's fix that."
stuff=tenthings.split(' ')
morestuff=['day','night','song','frisbee','corn','banana','girl','boy']

while len(stuff)!=10:
    nextone=morestuff.pop()
    print "adding:",nextone
    stuff.append(nextone)
    print "there's %d items now." %len(stuff)

print "there we go :", stuff
print "let's do some things with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print " ".join(stuff)  # 相当于 js 里 arr.join(' ')


print "#".join(stuff[3:5])  # arr.join("#")


