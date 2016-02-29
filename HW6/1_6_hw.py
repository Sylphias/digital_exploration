def reverse(s):
  r = ''
  for x in s:
    r = x+r
  return r
# print reverse('rawr')
#Find out how to do this in regex?
def isValidPassword(password):
  if len(password) < 8 or not password.isalnum() or sum(c.isdigit() for c in password) < 2: return False
  return True
# print "isValidPassword('test')" 
# print isValidPassword('test') 
# print "isValidPassword('testtest')" 
# print isValidPassword('testtest') 
# print "isValidPassword('testt22')" 
# print isValidPassword('testt22') 
# print "isValidPassword('testte22')" 
# print isValidPassword('testte22')   

def prefix(s1,s2):
  prefix = ''
  for x in range(min(len(s1),len(s2))):
    if s1[x] == s2[x]:
      prefix+=s1[x]
    else:
      return prefix
  return prefix   
# print "prefix('distance','disinfection')" 
# print prefix('distance','disinfection')
# print "prefix('testing','technical')" 
# print prefix('testing','technical')
# print "prefix('drinking','drinker')" 
# print prefix('drinking','drinker')
# print "prefix('rosses','crosses')" 
# print prefix('rosses','crosses')
# print "prefix('distancetion','distance')" 
# print prefix('distancetion','distance')

class Coordinate:
    x=0
    y=0


def read2columns(f):
  coordinates = []
  for x in f.readlines():
    point = Coordinate()
    split_line = x.strip().split()
    point.x = float(split_line[0])
    point.y = float(split_line[1])
    coordinates += [point]
  magnitude = [(pt.x**2 + pt.y**2)**0.5 for pt in coordinates]
  return coordinates[magnitude.index(max(magnitude))],coordinates[magnitude.index(min(magnitude))]
      
# f=open('xy.dat','r') 
# pmax,pmin=read2columns(f)
# print 'max: (%f, %f)'%(pmax.x,pmax.y) 
# print 'min: (%f, %f)'%(pmin.x,pmin.y)

f=open('replace.txt')
def replace(f, oldS, newS):
  text = ""
  for x in f.readlines():
    text += x.replace(oldS,newS)
  return text

print replace(f,"The","www")