class Square():
  def __init__(self,x = 0.0,y = 0.0, sideLength = 1.0):
    self.x = x
    self.y = y
    self.sideLength = sideLength
  def getCenter(self):
    return (self.x,self.y)
  def getSideLength(self):
    return (self.sideLength)
  def getArea(self):
    return self.sideLength**2
  def getPerimeter(self):
    return self.sideLength*4
  def containPoint(self,px,py):
    return True if px >= (self.x-(self.sideLength/2.0)) and px <= (self.x+(self.sideLength/2.0)) and py >= (self.y-(self.sideLength/2.0)) and py <= (self.y+(self.sideLength/2.0)) else False
  def containSquare(self, inSquare):
    return True if (inSquare.x - (inSquare.sideLength/2.0)) >= (self.x-(self.sideLength/2.0)) and (inSquare.x + (inSquare.sideLength/2.0))  <= (self.x+(self.sideLength/2.0)) and (inSquare.y - (inSquare.sideLength/2.0))  >= (self.y-(self.sideLength/2.0)) and (inSquare.x + (inSquare.sideLength/2.0))  <= (self.y+(self.sideLength/2.0)) else False

# s = Square(x=1,y=1, sideLength=2.0)
# print s.getCenter()
# print s.getSideLength()
# print s.getArea()
# print s.getPerimeter()
# print s.containPoint(0,0)
# print s.containPoint(0,-0.5)
# print s.containPoint(1,1.5)
# print s.containSquare( Square(x=1.5, y = 1, sideLength = 1))
# print s.containSquare( Square(x=1.5, y = 1, sideLength = 1.1))
# s2 = Square()
# print s2.getCenter()
# print s2.getSideLength()
# print s2.getPerimeter()

from libdw import sm
class Elevator(sm.SM):
  startState = 'First'
  def getNextValues(self, state, inp):
    if state == 'First':
      nextstate = state
      if inp == 'Up':
        nextstate = 'Second'
        return (nextstate, nextstate)
      return (nextstate, nextstate)

    elif state == 'Second':
      nextstate = state
      if inp == 'Up':
        nextstate = 'Third'
        return (nextstate,nextstate)
      elif inp == 'Down':
        nextstate = 'First'
        return (nextstate,nextstate)
      return (nextstate,nextstate)
    elif state == 'Third':
      nextstate = state
      if inp == 'Down':
        nextstate = 'Second'
        return (nextstate,nextstate)
      return (nextstate,nextstate)


# e = Elevator()
# print e.transduce( ['Up', 'Up', 'Up', 'Up', 'Down', 'Down', 'Down', 'Up'])

def countNumOpenLocker(K):
  lockers = [0 for n in range(K)]
  for passNo in range(1,K+1):
    for x in range(1,len(lockers)+1):
      if x%passNo == 0:
          lockers[x-1] = 0 if lockers[x-1] == 1 else 1
  return len([r for r in lockers if r==1])

# Factors of prime numbers
