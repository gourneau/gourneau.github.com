from operator import itemgetter

#thanks http://mail.python.org/pipermail/tutor/2002-May/014665.html
#and http://code.activestate.com/recipes/304440/

arr = []
inp = open ("phones.txt","r")
#read line into array 
for line in inp.readlines():
    # loop over the elemets, split by whitespace
    for i in line.split():
        # convert to integer and append to the list
        arr.append((i))

count = {}
for i in arr:
    if count.has_key(i):
        count[i] = count[i] + 1
    else:
        count[i] = 1

a =  sorted(count.items(), key=itemgetter(1), reverse=True)
for i in a:
    print i[0],
    print "-",
    print i[1]
