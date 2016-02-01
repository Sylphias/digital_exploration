#Q1
def cToF(C):
  return C*1.8+32.0
#Q2
from math import pi
def areaCylinder(radius, length):
  area = float(radius**2*pi)
  return area, area*length
#Q3
def windChilltemp(ta, v):
  if ta >= (-58.0) and ta <= 41 and v >= 2:
    return 35.74 + 0.6215*ta - 35.75*v**0.16 + 0.4275*ta*v**0.16
#Q4
def bmi(weight,height):
  return (weight*0.45359237)/((height*0.0254)**2)
#Q5
def investmentVal(amount, annualRate, years):
  return round(amount*(1+(annualRate/(12*100)))**(years*12), 2)

print investmentVal(1000,4.25,1)