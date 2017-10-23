#Find PI to the Nth Digit - Enter a number and have the program generate
#PI up to that many decimal places.
#Keep a limit to how far the program will go.

#Step 1, print pi

from math import pi
from datetime import datetime

hoss = float(pi)

print hoss

# Step 2, create function that limits decimal places

a = input("Enter a whole number between 0 and 11: ")

print ("%s" % round(pi, a))

print datetime.now().time()
