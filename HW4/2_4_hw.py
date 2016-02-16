def getConversionTable():
  ######Enter your code below ########
  faren = [0,10,20,30,40,50,60,70,80,90,100]
  celc = list()
  est = list()
  for x in faren:
    celc += [round((x-32.0)/1.8,1)]
    est += [round((x-30)/2,1)]
  conversion= [faren,celc,est]    #this is the table mentioned in the questions
  
  ######Ignore code below ############

  return conversion
# print getConversionTable()

def maxList(inp):
  greatest = list()
  for x in inp:
    old = x[0]
    for y in x:
      if y > old: old = y
    greatest += [old]
  return greatest
# inp = [[100],[1,7],[-8,-2,-1],[2]]
# print maxList(inp)

def nBynMultiplicationTable(N):
  if N<2 : return None
  table = list()
  for x in range(1,N+1):
    row = list()
    for y in range(1,N+1):
      row += [x*y]
    table += [row]
  return table
# print nBynMultiplicationTable(7)
import operator
def mostFrequent(numList):
  num_dict = dict()
  for x in numList:
    if x in num_dict: num_dict[x] +=1
    else: num_dict[x] = 0 #initialize the dictionary
  # This uses the operator.itemgetter method, interesting.
  # return max(num_dict.iteritems(), key=operator.itemgetter(1))
  greatest = num_dict[numList[0]] #assign default value
  g_list = list()
  for key,count in num_dict.iteritems():
    if greatest < count:
      greatest = count
      g_list = [count]
    elif greatest == count :
      g_list += [key]
  return g_list

# rawr=[2,3,40,3,5,4,-3,3,3,2,0]
# print mostFrequent(rawr)
# rawr=[9,30,3,9,3,2,4]
# print mostFrequent(rawr)

def diff(p):
  differential = dict()
  for key,count in p.iteritems():
    if key != 0: differential[key-1] = count*key
  return differential

p={0:-3, 3:2, 5:-1} 
print diff(p)
p={1:-3, 3:2, 5:-1, 6:2} 
print diff(p)
p={0:-3, 3:2, 8:2} 
print diff(p)
p={0:-4, 2:12, 3:-2, 4:3, 8:2} 
print diff(p)
p={0:-3, 1:12, 2:-2, 3:2, 10:2} 
print diff(p)


