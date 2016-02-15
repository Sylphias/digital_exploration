#Q1
def check2(n1,n2,n3,x):
  if x > n1 and x > n2 and x < n3:
    return True
  return False

# print '''Test case 1: check2(1,4,8,7)''' 
# print '''ans = True''' 
# ans=check2(1,4,8,7)
# print ans
# print '''Test case 2: check2(10,4,8,7)''' 
# print '''ans = False''' 
# ans=check2(10,4,8,7)
# print ans
# print '''Test case 3: check2(1,10,8,7)''' 
# print '''ans = False''' 
# ans=check2(1,10,8,7)
# print ans
# print '''Test case 4: check2(1,4,5,7)''' 
# print '''ans = False''' 
# ans=check2(1,4,5,7)
# print ans


#Q2
def cToF(C):
  return C*1.8+32.0
def fToC(temp):
  return (temp-32)/1.8
def tempConvert(units, temp):
  if units == 'C':
    return fToC(temp)
  elif units == 'F':
    return cToF(temp)
  else:
    return "None"
# print '''Test case 1: F = 32''' 
# ans=tempConvert('F', 32)
# print ans
# print '''Test case 2: F = -40''' 
# ans=tempConvert('F', -40)
# print ans
# print '''Test case 3: F= 212''' 
# ans=tempConvert('F', 212)
# print ans
# print '''Test case 4: C = 0''' 
# ans=tempConvert('C', 0)
# print ans
# print '''Test case 5: C = -40''' 
# ans=tempConvert('C', -40)
# print ans
# print '''Test case 6: C = 100''' 
# ans=tempConvert('C', 100)
# print ans
# print '''Test case 7: Neither 'C' nor 'F''' 
# ans=tempConvert('', 0)
# print ans
# print '''Test case 8: Neither 'C' nor 'F''' 
# ans=tempConvert('A', 0)
# print ans

#Q3
def getEvenNumber(numbers):
  even_numbers = []
  for n in numbers:
    if n%2 == 0 :
      even_numbers += [n]
  return even_numbers


# print 'getEvenNumber([1,2,3,4,5])' 
# ans=getEvenNumber([1,2,3,4,5]) 
# print ans
# print 'getEvenNumber([11,22,33,44,55])' 
# ans=getEvenNumber([11,22,33,44,55]) 
# print ans
# print 'getEvenNumber([10,20,30,40,50])' 
# ans=getEvenNumber([10,20,30,40,50]) 
# print ans
# print 'getEvenNumber([11,21,31,41,51])' 
# ans=getEvenNumber([11,21,31,41,51]) 
# print ans

#Q4 - There are two ways to do this... one is to compare against a set of known primes.... the other is to write out the algorithm for the AKS primality test
# # This is the AKS algorithm written by somone else
# def isPrime(n):
#     if n == 2:
#       return True
#     if n == 3:
#       return True
#     if n % 2 == 0:
#       return False
#     if n % 3 == 0:
#       return False
#     i = 5
#     w = 2
#     while i * i <= n:
#       if n % i == 0:
#         return False
#       i += w
#       w = 6-w
#     return True

# https://en.wikipedia.org/wiki/Primality_test
# Based on the division test I wrote this algo
def isPrime(n):
  if n == 2: return True
  if n == 3: return True
  for i in range(1,int(n/2)):
    if n==(6*i+1) or n==(6*i-1):
      return True
  return False


# print 'isPrime(2)' 
# ans=isPrime(2) 
# print ans
# print 'isPrime(3)' 
# ans=isPrime(3) 
# print ans
# print 'isPrime(7)' 
# ans=isPrime(7) 
# print ans
# print 'isPrime(9)' 
# ans=isPrime(9) 
# print ans
# print 'isPrime(21)'
# ans=isPrime(21) 
# # print ans
# print isPrime(1231)
# print isPrime(3499)
# print isPrime(1)
# print isPrime(0)
#Q5 - This methond has some very peculiar behaviour, ask teacher
from math import e
def approx_ode(t,h):
  y = 1
  x = 0
  while(x < t): #This while loop only overshots on the last run.... ask why
    y += (3+e**(-x)-(0.5*y))*h
    x += h
    print x
  return round(y,3)
# from math import exp
# def approx_ode(t,h):
#   y = 1
#   x = 0
#   for n in range(int(t/h)):
#     y += (3+exp(-x)-(0.5*y))*h
#     x += h
#   return round(y,3)
print approx_ode(3,0.1)
print approx_ode(4,0.1)
print approx_ode(5,0.1)
###### This is the code for tutor....####
# import math
# def approx_ode(h,t0,y0,tn):
######### h - step size
######### t0 - initial t value (at step 0)
######### y0 - initial y value (at step 0)
######### tn - t value at step n

######### Add you code below this line
######### Return your answer correct to 3 decimal places
  # x = t0
  # for n in range(int(tn/h)):
  #   y0 += (3+math.e**(-x)-(0.5*y0))*h
  #   x += h
  # return round(y0,3)


######### Ignore code below this line ######################################

# def f(t, y):
#     return 3.0+math.exp(-t)-0.5*y


