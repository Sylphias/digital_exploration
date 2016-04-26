import math
class Point2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __str__(self):
    return 'Point2D('+ str(self.x) + ',' + str(self.y)+')'
  def add(self, vector):
    return Point2D(self.x + vector.dx, self.y + vector.dy)

class Vector2D:
  def __init__(self,dx,dy):
    self.dx = dx
    self.dy = dy
  def length(self):
    return math.sqrt(self.dx**2 + self.dy**2)

class Polyline2D:
  def __init__(self,startPoint,vectors):
    self.startPoint = startPoint
    self.vectors = vectors

  def addSegment(self, newVector):
    self.vectors += [newVector]

  def length(self):
    return sum([x.length() for x in self.vectors])

  def vertex(self,polyVert):
    if polyVert == 0: return self.startPoint
    point = self.startPoint
    for x in range(polyVert):
      point = point.add(self.vectors[x])
    return point
# p = Point2D(1,2)
# v = Vector2D(3,1)
# q = p.add(v)

# print q
# pline = Polyline2D(Point2D(1,2), [Vector2D(3,1)])
# pline.addSegment(Vector2D(1,0))
# pline.addSegment(Vector2D(0,2))
# print pline.length()
# print pline.vertex(0)
# print pline.vertex(1)
# print pline.vertex(2)
# print pline.vertex(3)

class ClosedPolyline2D(Polyline2D):
  def length(self):
    numOfVec = len(self.vectors)
    self.vectors += [Vector2D(self.startPoint.x - self.vertex(numOfVec).x,self.startPoint.y - self.vertex(numOfVec).y)]
    return sum([x.length() for x in self.vectors])

# cpline = ClosedPolyline2D(Point2D(1,2), [Vector2D(3,1)])
# cpline.addSegment(Vector2D(1,0))
# cpline.addSegment(Vector2D(0,2))
# print cpline.length()
