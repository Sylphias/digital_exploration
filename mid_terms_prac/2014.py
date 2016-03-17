# Timed run
def stc(s1,s2):
  return abs(len(s1)-len(s2))

# s1='Japan'
# s2='Singapore'

# print stc(s1,s2)

def sumVal(d):
  if not d: return None
  total = 0
  for key,value in d.iteritems():
    if key < 3:
      total += value
  return total
# d = {4: -7,8: 4,2: 10,1: -2}
# print sumVal(d)
# d= {}
# print sumVal(d)

def count(a,b,c):
  return len([x for x in range(a,b)]) > len([y for y in range(b,c)])

# print count(2,4,7)
# print count(3,7,1)

def getMRT(f):
  lines = f.readlines()
  mrts = {}
  for x in lines:
    info = x.strip().split(',')
    mrts[info[0]] = [ info[y] for y in range(len(info)) if y!=0 ]
  return mrts
# print getMRT(f)


def distance(d,s):
  if not s : return -2
  mrtz = s.split(',')
  if len(mrtz) <2:return -1
  mrt1 = mrtz[0]
  mrt2 = mrtz[1]
  count = 0
  #find where mrt1 lies
  for values in d.values():
    if mrt1 in values:
      if mrt2 in values:
        start_counting = False   
        other_mrt = ""
        for x in values:
          #inefficient, refactor later
          if start_counting: count += 1
          if x == other_mrt:
            return count
          if x == mrt2:
            start_counting =True
            other_mrt = mrt1
          if x == mrt1:
            start_counting =True
            other_mrt = mrt2
      else:
        return -1



def test(): 
  f =open("mrt.txt", "r") 
  d = getMRT(f)
  done=False
  while not done:
    s=raw_input("Two stations please:") 
    dist= distance(d,s)
    if dist != -2:
      print dist 
    else:
      done=True
  print "Bye!" 
  f.close()


# test


class Matrix:
  def __init__(self,m,s="Matrix A",f="%6.2f"):
    self.m = m
    self.s = s
    self.f = f
  def __str__(self):
    matrix = "%s: Rows:%2d Columns:%2d\n" %(self.s,len(self.m),len(self.m))
    for row in self.m:
      for element in row:
        matrix += self.f %element
      matrix +="\n"
    return matrix
  def diag(self):
    for x in range(len(self.m)):
      if self.m[x][x] == 0: return False
    return  True
  #Read instructions wrongly XD
  def upperDiag(self):
    for x in range(len(self.m)):
      if x!=0:
        if self.m[x-1][x]==0: return False
    return  True

  def lowerDiag(self):
    for x in range(len(self.m)):
      if x!=len(self.m)-1:
        if self.m[x+1][x]==0: return False
    return  True

  def triDiag(self):
    for x in range(len(self.m)):
      if self.m[x][x] == 0: return False
      if x!=len(self.m)-1:
        if self.m[x+1][x]==0: return False
      if x!=0:
        if self.m[x-1][x]==0: return False
    return  True


m1=[[1,4,0,0],[3, 4, 1, 0], [0, 2, 3, 4], [0,0,1,3]]
a=Matrix(m1)
print a.triDiag()
print a

m2=[[1,0,0,0], [3, 4, 1, 0], [0, 2, 3, 4], [0,0,1,3]]
a=Matrix(m2)
print a.lowerDiag()
print a.upperDiag()

m3=[[1,4,0,0], [3, 0, 1, 0], [0, 2, 3, 4], [0,0,1,3]]
a=Matrix(m3, "DW Matrix", "%6.1f")
print a













