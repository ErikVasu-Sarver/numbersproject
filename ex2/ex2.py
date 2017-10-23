#Find e to the Nth Digit - Just like the previous problem, but with e instead of
#PI. Enter a number and have the program generate e up to that many decimal
#places. Keep a limit to how far the program will go.

from math import e
from datetime import datetime

#step 1, print e

hoss = float(e)
print hoss


#step 2, print e but with a limit on decimal places

a = input("Enter a whole number between 1 and 11:")

print ("%s" % round(e, a))

print datetime.now().time()
