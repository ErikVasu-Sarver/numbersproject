#Fibonacci Sequence - Enter a number and have the program generate the Fibonacci
#sequence to that number or to the Nth number.

#step 1, create formula that calculates the Fibonacci sequence

#I found this side that details how the Fibonacci Sequence works.
#https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence-in-python
#I used this formula from the site:
from math import sqrt
from datetime import datetime

n = input ("Enter a whole  number:")
def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


print datetime.now().time()

#Step 2, list the numbers involved in that sequence
