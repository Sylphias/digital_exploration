import math

class Coordinate:
  def __init__(self,x=0,y=0):
    self.x= x
    self.y= y
  def setXY(self,x,y):
    self.x = x
    self.y = y
  def getX(self):
    return self.x
  def getY(self):
    return self.y
  def getXY(self):
    return (self.x,self.y)
  def getMagnitude(self):
    return math.sqrt(self.x**2+self.y**2)


# p=Coordinate()
# print p.getXY()
# print (p.getX(),p.getY())
# q=Coordinate(-1.4,7.1)
# print q.getMagnitude() 


class Square:
  def __init__(self,length =0):
    self.length = length
    self.area = length**2
  def getArea(self):
    return float(self.area)
  def setArea(self,area):
    self.area =float(area)
    self.length = float(area**0.5)
  def __str__(self):
    return "Square of height and width "+ str(self.length)+ "."
# s = Square (6)
# print s.getArea()
# s.setArea(100)
# s1 = Square (10)
# print s1.getArea()
# s2 = Square(100)
# print s2.getArea()
# print s1 # Print object s1 using __str__. Square of height and width 10.
# s=Square(7)
# s.setArea(100)
# print (s.getArea(), str(s))
import time

class StopWatch:
  def __init__(self,startTime=time.time(),endTime=-1):
    self.startTime = startTime
    self.endTime = endTime
  def start(self):
    self.startTime = time.time()
    self.endTime = -1
  def stop(self):
    self.endTime=time.time()
  def getStartTime(self):
    return self.startTime
  def getEndTime(self):
    return self.endTime
  def getElapsedTime(self):
    return int((self.endTime-self.startTime)*1000) if self.endTime != -1 else None

# sw1=StopWatch()
# print sw1.getElapsedTime()
# print sw1.getEndTime()

# sw1=StopWatch()
# time.sleep(2)
# sw1.start()
# time.sleep(3)
# sw1.stop()
# print sw1.getElapsedTime()


########## Define your class Line below this line ###########
class Line:
  def __init__(self,c0=0,c1=0):
    self.c0 = c0
    self.c1 = c1
  def __call__(self,x):
    return round(self.c0 +self.c1*x,2)
  def table(self,L,R,N):
    row = ""
    x=float(L)
    if L!=R:
      for n in range(N-1):
        row += '%10.2f%10.2f\n' %(x,self(x))  
        x += (R-L)/float(N-1)
    row+= '%10.2f%10.2f\n' %(R,self(R)) 
    return row if N !=0 else "Error in printing table"
########## Ignore the code below this line ##################

def testLine(c0,c1,x,L,R,N):
    line=Line(c0,c1)
    return line(x),line.table(L,R,N)

print testLine(1,2,2,1,5,4)
print testLine(3,4,2,1,1,15)