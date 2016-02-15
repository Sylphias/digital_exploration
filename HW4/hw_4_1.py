# 1a) 0
# 1b) a
# 1c) 1
# 1d) 0, 0 ,0 , 1
# 1e) 1, 0, 0 , 1
# 1f) error, [1,0], error, [1,0]

def compoundVal6Months(monthlyAmt, annualRate, months):
  compounded = 0
  for n in range(months):
    compounded = (monthlyAmt+compounded)*(1+(annualRate/12))
  return round(compounded,2)

# ans=compoundVal6Months(100,0.05,6) 
# print ans
# ans=compoundVal6Months(100,0.03,7) 
# print ans
# ans=compoundVal6Months(200,0.05,8) 
# print ans
# ans=compoundVal6Months(200,0.03,1) 
# print ans
####### Your function should return a tuple containing a list of average #####
####### and the overall average, e.g., ([3.5,6.0,1.4], 3.625) ################  

def findAverage(listOfLists):
  sum_list = list()
  total = 0.0
  length = 0.0
  for n in listOfLists:
    if len(n) != 0:
      sum_list += [sum(n)/float(len(n))]
      total+= sum(n)
      length +=len(n)
    else:
      sum_list +=[0.0]
  return sum_list,total/length



# ans=findAverage([[3,4],[5,6,7],[-1,2,8]]) 
# print ans

# ans=findAverage([[13.13,1.1,1.1],[],[1,1,0.67]]) 
# print ans

# ans=findAverage([[3.6],[1,2,3],[1,1,1]]) 
# print ans
def transposeMatrix(a):
  transposed = [[1 for i in range(len(a))] for j in range(len(a[0]))]
  for x in range(len(a)):
    for y in range(len(a[x])):
      transposed[y][x]= a[x][y]
  return transposed
# a = [[1,2,3], [4,5,6], [7,8,9]]
# print transposeMatrix(a)
# a = [[-11,12,3], [4,-5,6]]
# print transposeMatrix(a)
# a = [[1,2], [10,5], [0,0]]
# print transposeMatrix(a)

phonebook=[{'name':'Andrew', 'mobile_phone':9477865, ' office_phone':6612345, 'email':'andrew@sutd.edu.sg'},{'name':'Bobby','mobile_phone':8123498, 'office_phone':6654321, 'email': ' bobby@sutd.edu.sg'}]

def getDetails(name, key, phonebook):
  for n in phonebook:
    if n['name'] == name:
      return n[key]
  return None


# print getDetails('Andrew', 'mobile_phone', phonebook)
# print getDetails('Andrew', 'email', phonebook)
# print getDetails('Bobby', 'office_phone', phonebook)
# print getDetails ('Chokey', 'office_phone', phonebook)

def getBaseCounts(dna):
  counts = {'A':0,'C':0,'G':0,'T':0}
  dna_final = {}
  for n in dna:
    if n == 'A': counts['A'] +=1
    elif n == 'C': counts['C'] +=1
    elif n == 'G': counts['G'] +=1
    elif n == 'T': counts['T'] +=1
    else :
      return "The input DNA string is invalid"
  for x in counts:
    if counts[x] != 0: dna_final[x] = counts[x]
  return dna_final

print getBaseCounts('AACCGT')
print getBaseCounts('AAB')
print getBaseCounts('AaCaGT')
print getBaseCounts('A')

