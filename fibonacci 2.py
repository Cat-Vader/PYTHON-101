Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # python program to check if x is a perfect square
import math
 
# A utility function that returns true if x is perfect square
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
 
# Returns true if n is a Fibonacci Number, else false
def isFibonacci(n):
 
    # n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perfect square
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
    
# A utility function to test above functions
for i in range(1,11):
     if (isFibonacci(i) == True):
         print i,"is a Fibonacci Number"
     else:
         print i,"is a not Fibonacci Number "