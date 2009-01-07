'''
Joshua Gourneau
This is a simple script for the brunswickcgp.com build a boat options.
It will take some preformated csv data in.  Where the first column is
the option id, and the second indicates if it is standard or not.
It then prints out the sql to be ran on the server
'''

#read the data in
stn = {}
inp = open ("19justiceparts.csv","r")
#read line into array
for line in inp.readlines():
    # loop over the elemets, split by whitespace
    for i in line.split():
        #break the string apart on comma, put in array
        t = line.split(",")
        #trim the trailing \n character from the 2nd column
        t[1] = t[1][:-1]
        #add the values to the dict
        stn[t[0]]=t[1]

#sort the dict by the key
a = sorted(stn.items())

#print out the sql
#base boat id
baseboat = 17
startid = 3711
count = 0
print "INSERT INTO `jos_bb_baseboat_options` (`id` ,`option_id`, `baseboat_id`, `is_std`) VALUES ",
for i in a:
    print '(%s,%s,%s,%s)' % (startid,i[0],baseboat,i[1])
    startid = startid + 1
    count = count + 1
    if count < len(a):
        print ",",

print ";",

