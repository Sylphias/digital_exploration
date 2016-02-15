import math
def trapezoidal(a,b):
  return round((b-a)*(math.sin(b)+math.sin(a))/2,2)

print trapezoidal(6,5)
print trapezoidal(5,5)
print trapezoidal(2,5)
print trapezoidal(3,2)