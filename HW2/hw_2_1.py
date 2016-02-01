def fToC(temp):
  return (temp-32)/1.8
print fToC(32)
print fToC(-40)
print fToC(212)


def yearsDays(minutes):
  days = minutes/1440
  years = days/365
  remainderDays = (days%365)
  return years,remainderDays

print yearsDays(1000000000)
print yearsDays(2000000000)

def posVel(v,t):
  g = 9.81
  vel = v*t-0.5*g*t**2
  accel = v-1*g*t
  return round(vel,2),round(accel,2)

print posVel(5.0, 10.0)
print posVel(5.0, 0.0)
print posVel(0.0, 5.0)

class Coordinate:
  x=0
  y=0

def areaTriangle(p1,p2,p3):
  side1 = abs(((p1.x-p2.x)**2+(p1.y-p2.y)**2)**(0.5))
  side2 = abs(((p1.x-p3.x)**2+(p1.y-p3.y)**2)**(0.5))
  side3 = abs(((p2.x-p3.x)**2+(p2.y-p3.y)**2)**(0.5))
  s = (side1 + side2 + side3)/2.0
  area = (s*(s-side1)*(s-side2)*(s-side3))**(0.5)

  return round(area,2)
# p1 = Coordinate()
# p2 = Coordinate()
# p3 = Coordinate()
# print "Enter x coordinate of the first point of a triangle:"
# p1.x = float(raw_input())
# print "Enter y coordinate of the first point of a triangle:"
# p1.y = float(raw_input())
# print "Enter x coordinate of the second point of a triangle:"
# p2.x = float(raw_input())
# print "Enter y coordinate of the second point of a triangle:"
# p2.y = float(raw_input())
# print "Enter x coordinate of the third point of a triangle:"
# p3.x = float(raw_input())
# print "Enter y coordinate of the third point of a triangle:"
# p3.y = float(raw_input())
# print "The area of the triangle is: " 
# print areaTriangle(p1,p2,p3)

print "Test Case 1"
p1=Coordinate() 
p1.x=1.5
p1.y=-3.4 
p2=Coordinate() 
p2.x=4.6
p2.y=5 
p3=Coordinate() 
p3.x=9.5 
p3.y=-3.4

print areaTriangle(p1,p2,p3)

print "Test Case 2" 
p1=Coordinate()
p1.x=2.0
p1.y=-3.4 
p2=Coordinate() 
p2.x=4.6
p2.y=5 
p3=Coordinate() 
p3.x=9.5 
p3.y=-1.4
ans=areaTriangle(p1,p2,p3) 
print ans

print "Enter the monthly saving amount: "
s = float(raw_input())
print "Annual interest rate: "
r = float(raw_input())

def compoundInterest(saving,rate):
  final_amount = saving*(1+rate/12)

  for n in range(0,5):
    final_amount=(saving+final_amount)*(1+rate/12)
  return final_amount
print compoundInterest(s,r)