#What is the exponent of the largest power of two whose base seven representation doesn't contain three zeros in a row?  

from decimal import *
import cmath
#use psyco to speed this script up
# http://psyco.sourceforge.net/
try:
	import psyco
	psyco.full()
except ImportError:
    pass


#from http://code.activestate.com/recipes/65212/
def baseconvert(n, base):
	"""convert positive decimal integer n to equivalent in another base (2-36)"""

	digits = "0123456789abcdefghijklmnopqrstuvwxyz"

	try:
	    n = int(n)
	    base = int(base)
	except:
	    return ""

	if n < 0 or base < 2 or base > 36:
	    return ""

	s = ""
	while 1:
	    r = n % base
	    s = digits[r] + s
	    n = n / base
	    if n == 0:
	        break

	return s

#WE FOUND A WINNER 37022

i = 1
while i < 99999999999:
	a = pow(2,i)
	b = baseconvert(a,7)
	if str(a).find("000") == -1:
		print "Highest power of 2 in base 7 without substring of 000: ",
		print i
	i = i + 1
	


