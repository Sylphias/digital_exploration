import math 

class Triangle:

  def __init__(self,color="green",filled=True,side1=1.0,side2=1.0,side3=1.0):
    self.color = color
    self.filled = filled
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3
  def isFilled(self):
    return self.filled
  def setFilled(self,fill):
    self.filled = fill
  def getSide1(self):
    return self.side1
  def getSide2(self):
    return self.side2
  def getSide3(self):
    return self.side3
  def getArea(self):
    s = (self.side1+self.side2+self.side3)/2
    return math.sqrt(s*(s-self.side1)*(s-self.side2)*(s-self.side3))

t= Triangle()
print t.isFilled()
t = Triangle()
t.setFilled(False)
print t.isFilled()
t=Triangle()
print (t.isFilled(),t.getSide1(),t.getSide2(),t.getSide3())
t=Triangle('red',False,4.0,3.0,5.0)
print (t.color,t.isFilled(),t.getSide1(),t.getSide2(),t.getSide3())
t = Triangle(side1=4.0,side2=3.0,side3=5.0)
print t.getArea()
