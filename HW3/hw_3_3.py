def mayIgnore(n):
  if type(n) is int: return n+1
  return None
# print mayIgnore(1)
# print mayIgnore(1.0)
# print mayIgnore('hello')
def myReverse(myList):
  reversed_list = range(len(myList))
  for idx, n in enumerate(myList,start=1):
   reversed_list[idx*-1] = n
  return reversed_list

# print myReverse([1,2,3,4,9])
from math import factorial
def piR(n):
  pi = 0
  for k in range(n+1):
    pi += (factorial(4.0*k)*(1103.0+26390.0*k))/((factorial(k)**4)*(396**(4*k)))
  return 1.0/((2*2**0.5)/9801.0*pi)
# print piR(2)

# def getGCD(a,b):
#   x = max(a,b)
#   remainder = min(a,b)
#   gcd = min(a,b)
#   while (remainder != 0):
#     remainder= x%remainder
#     if remainder!=0: gcd = 
#     x=remainder
#   return gcd


def getGCD(a,b):
  if a%b == 0: return min(a,b)
  return getGCD(b,a%b)

# print getGCD(1,2)
# print getGCD(2,1)
# print getGCD(55,144)
# print getGCD(10,20)
# print getGCD(42,30)


######### Ignore code below this line ######################################
def f1(x):
    return x**2

def f2(x):
    return math.sin(x)

def f3(x):
    return math.exp(-x)
import math
def simpsonsRule(f, n, a, b):
  n = float(n)
  a = float(a)
  b = float(b)
  h = (b-a)/n
  fx = 0
  fy = 0
  for j in range(1,int((n/2.0))):
    fx+=f(a+(2*j)*h)
  fx *=2
  for i in range(1,int(n/2.0+1)):
    fy+=f(a+(i*2-1)*h)
  fy*=4
  return (h/3.0)*(f(a)+fx+fy+f(b))
# print simpsonsRule(f1,1000,1,3)
# print simpsonsRule(f2,1000,0,math.pi)
# print simpsonsRule(f3,1000,-1,1)