from decimal import *
import cmath
import psyco
psyco.full()
psyco.profile(1)

#http://psyco.sourceforge.net/

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

i = 16000
while i < 99999999999:
	a = pow(2,i)
	b = baseconvert(a,7)
	if str(a).find("000") == -1:
		print "WE FOUND A WINNER",
		print i
	i = i + 1
	


