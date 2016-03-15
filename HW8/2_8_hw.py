class Time:
  def __init__(self,hour,minute,second):
    self.hour = hour
    self.minute = minute
    self.second = second
  def getHour(self):
    return self.hour
  def getMinute(self):
    return self.minute
  def getSecond(self):
    return self.second
  def setTime(self,elapseTime):
    if elapseTime > (12*60*60):elapseTime = elapseTime%(12*60*60)
    self.second = elapseTime%60
    self.minute = ((elapseTime-self.second)/60)%60
    self.hour = ((((elapseTime-self.second)/60)-self.minute)/60)


# t=Time(5,30,23)
# t.setTime(555550)
# ans=(t.getHour(), t.getMinute(), t.getSecond())
# print ans


class Account:    
  def __init__(self,name,acc_num,balance):
    self.name = name
    self.acc_num = acc_num
    self.balance = balance
  def deposit(self,amount):
    self.balance += amount  
  def withdraw(self,amount):
    self.balance -= amount
  def __str__(self):
    return str(self.name)+", "+ str(self.acc_num)+", "+"balance: "+str(self.balance)  

# a1 = Account('John Olsson', '19371554951', 20000)
# a2 = Account('Liz Olsson', '19371564761', 20000)
# a1.deposit(1000)
# a1.withdraw(4000)
# a2.withdraw(10500)
# a1.withdraw(3500)
# print a1
# print a2

from math import *
#return only the derivative value without rounding
#your return value is a float, which is the approximate value of the derivative
#Tutor will compute the approximate error based on your return value

class Diff:
  def __init__(self,f,h=0):
    self.f = f
    self.h = h
  def __call__(self,x):
    return (self.f(x + self.h) - self.f(x))/self.h



# def f(x):
#   return 0.25*x**4
# df = Diff(f)
# # df(x) computes the derivative of f(x) approximately:
# for x in (1, 5, 10):
#   df_value = df(x) # approx value of derivative of f at point x exact = x**3 # exact value of derivative
#   exact = x**3 # exact value of derivative
# print "f'(%d)=%g (error=%.2E)" % (x, df_value, exact-df_value)


#For Test case 2: return a tuple with coeff list and evaluated value

class Polynomial:
  def __init__(self,coeff):
    self.coeff = coeff
  
  def __getitem__(self,x):
    return self.coeff[x]

  def __add__(self,poly):
    larger_list = max(poly.coeff,self.coeff, key=len)[:]
    smaller_list = min(poly.coeff,self.coeff,key=len)[:]
    for x in range(len(smaller_list)):
      larger_list[x] += smaller_list[x]
    return Polynomial(larger_list) 

  def __len__(self):
    length = 0
    for x in self.coeff:
      length += 1 
    return length

  def __sub__(self,poly): 
    negative_list = [x*-1 for x in poly.coeff]
    return self+Polynomial(negative_list)

  def __call__(self,x):
    total = 0
    for i in range(len(self.coeff)):
      total += self.coeff[i]*x**i 
    return total

  def __mul__(self,poly):
    largest_coeff = (len(poly.coeff)) + (len(self.coeff))
    new_poly = [0 for x in range(largest_coeff-1)]
    for r in range(len(self.coeff)):
      for s in range(len(poly.coeff)):
        pos = r+s
        new_poly[pos]+= self.coeff[r]*poly.coeff[s]
    return Polynomial(new_poly) 

  def differentiate(self):
    self.coeff =[ i*self.coeff[i] for i in range(1,len(self.coeff))]
  def derivative(self):
    return Polynomial([ i*self.coeff[i] for i in range(1,len(self.coeff))])





p1 = Polynomial([1, -1])
p2 = Polynomial([0, 1, 0, 0, -6, -1]) 
p3 = p1 + p2
print p3.coeff
print p1.coeff
print p2.coeff
p4 = p1 * p2
print p4.coeff
p5 = p2.derivative()
print p5.coeff
p = Polynomial([1, 2, 3])
q = Polynomial([2, 3])
r=p-q
print r.coeff
r=q-p
print r.coeff

rawr = Polynomial([1, 3, 5, 7, 9])
rawr.differentiate()
print rawr.coeff
m = Polynomial([2, 4, 6, 8, 10])
print rawr.derivative().coeff

x = Polynomial([0, 1, 0, 0, -6, -1])
y = Polynomial([1, 1])
z= y-x
print z.coeff, z(3)
