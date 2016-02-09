# 1a)
#   Case 1 : print x
#   Case 2 : Print y
#   Case 3 : print x+y
# 1b)
#   case 1:  print x+y
#   case 2: Print  y + if statement
#   case 3: print x

def letterGrade(mark):
  if(mark < 0 or mark> 100):
    return "None"
  if(mark >=90 ):
    return "A"
  elif(mark >= 80):
    return "B"
  elif(mark >= 70 ):
    return "C"
  elif(mark >= 60):
    return "D"
  else: 
    return "E"


# print letterGrade(102) 
# print letterGrade(100) 
# print letterGrade(80) 
# print letterGrade(70) 
# print letterGrade(60) 
# print letterGrade(52) 
# print letterGrade(-2) 

def check1(n1,n2):
  return n1>n2


# print check1(2,-1)
# print check1(-1,2)
# print check1(2,2)

def listSum(a):
  total = 0
  for l in a:
    total += l
  return round(total,1)

# print ("Test case 1: [4.25,5.0,10.75]") 
# ans=listSum([4.25,5.0,10.75])
# print ans
# print ("Test case 2: [5.0]") 
# ans=listSum([5.0])
# print ans
# print ("Test case 3: []") 
# ans=listSum([])
# print ans

# def maxList(listValues):
#   if len(listValues)== 0 :
#     return "None", "None" 
#   max_value = listValues[0]
#   min_value = listValues[0]
#   for n in listValues:
#     max_value = max(max_value,n)
#     min_value = min(min_value,n)
#   return max_value, min_value

#Alternative max list without using built in functions

def maxList(listValues):
  if len(listValues)== 0 :
    return None, None 
  max_value = listValues[0]
  min_value = listValues[0]
  for n in listValues:
    if max_value < n :
      max_value = n   
    if min_value > n :
      min_value = n 
  return min_value, max_value

# print ("Test case 1: [1,2,3,4,5]")
# ans=maxList([1,2,3,4,5])
# print ans
# print ("Test case 2: [1,1,3,0]") 
# ans=maxList([1,1,3,0])
# print ans
# print ("Test case 3: ")
# ans=maxList([3,2,1]) 
# print ans
# print ("Test case 4: ")
# ans=maxList([0,10]) 
# print ans
# print ("Test case 5: [1]") 
# ans=maxList([1])
# print ans
# print ("Test case 6: []") 
# ans=maxList([])
# print ans
# print ("Test case 7: [1,1,1,1,1]") 
# ans=maxList([1,1,1,1,1])
# print ans


def isPalindrome(number):
  num_str = str(number)
  input_length = len(num_str)
  for n in range(input_length/2):
    if num_str[n] != num_str[(input_length-1)-n]:
      return False
  return True

# print ("Test case 1: 1") 
# ans=isPalindrome(1) 
# print ans
# print ("Test case 2: 22") 
# ans=isPalindrome(22) 
# print ans
# print ("Test case 3: 12321") 
# ans=isPalindrome(12321) 
# print ans
# print ("Test case 4: 441232144") 
# ans=isPalindrome(441232144) 
# print ans
# print ("Test case 5: 441231144") 
# ans=isPalindrome(441231144) 
# print ans
# print ("Test case 6: 144") 
# ans=isPalindrome(144) 
# print ans
# print ("Test case 7: 12") 
# ans=isPalindrome(12) 
# print ans

