# assigns the variable b with a, this allows operation on the value b to affect the list a
# Slices the a list from start to end and assigns variable c with this new list, it is a shallow copy of the list (does not make a new copy of nested list)
# copies a new instance of list a to the variable d, includes nested list (which makes a new instance of the nested list)


# 2 
# The student needs to update the leftObstacle and rightObstacle in the while statement, student needs to put the leftObstacle, rightObstacle = finch.obstacle() into the while loop

#part b
def comp(x):
  return x**3 +4*x**2+6*x+1
# print comp(2)
# print comp(3)

def genList(n1,n2):
  return [x for x in range(n1+1,n2+1) if x%3==0 ]

# print genList(2,12)
# print genList(2,20)

def matAdd(a,b):
  return [[a[x][y]+b[x][y] for y in range(len(a[x]))] for x in range(len(a))]

# A = [[1,2,3], [4, 5, 6]]
# B = [[10,20,30], [40, 50, 60]]
# C = matAdd(A,B)
# print 'A:', A, 'B:', B, 'C:', C

#Part C
f = open("./2015text/data1.txt",'r')
def getSchedule(f):
  lines = f.readlines()
  schedule ={}
  day_list = []
  day = ""
  for x in lines:
    if x.strip().isalpha():
      day = x.strip()
      schedule[day]=[]
    else:
      num = x.split()
      schedule[day] += [(int(num[0]),int(num[1]))]
  return schedule

def findLength(dictSchedule):
  findLength = {}
  total = 0
  for key,value in dictSchedule.iteritems():
    total = 0
    for x in value:
      total +=sum(x)
    findLength[key] = total 
  return findLength

def findConflict(dictSchedule):
  conflict = {}
  old_value =()
  for key,value in dictSchedule.iteritems():
    count = 0
    conflict[key] = False
    for x in value:
      count +=1
      start,end = x
      for y in range(count,len(value)):
        if (start<= value[y][1] and start >= value[y][0] )or (end<= value[y][1] and end >= value[y][0]):
          conflict[key] = True
          break
  return conflict

# n = getSchedule(f)
# print findLength(n)
# print findConflict(n)


def countLitPixel(cx,cy,r):
  count = 0
  for x in range(r):
    for y in range(r):
      if x**2+y**2 < (r)**2  :
        count+=1
  return count*4

print countLitPixel(5,2,5)
print countLitPixel(1,1,1)
