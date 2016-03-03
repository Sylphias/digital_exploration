card_prefix = (4,5,37,6)
def isValid(number):
  if not len(str(number)) > 13 and not len(str(number)) <16: return False
  isValid = False
  for x in card_prefix:
    if prefixMatched(getPrefix(number,len(str(x))), x): 
      isValid=True
  if (sumOfDoubleEvenPlace(number)+ sumOfOddPlace(number))%10 == 0 and isValid: 
    return True
  else: 
    return False



def prefixMatched(number, d):
  return str(number)[:len(str(d))]==str(d)

def getSize(d):
  return len(str(d))

def getPrefix(number,k):
  return str(number)[:k]

# Get the result from Step 2.
def sumOfDoubleEvenPlace(number):
    sumDE=0
    while number!=0:
        number/=10
        digit=number%10
        double=digit*2
        digitSum=getDigit(double)
        sumDE+=digitSum
        number/=10
    return sumDE

# Return this number if it is a single digit, othewise, return the sum of the two digits.
def getDigit(number):
    if number<10:
        return number
    else:
        return (number/10+number%10)

# Return sum of odd place digits in number. Assume given.
def sumOfOddPlace(number):
    sumDE=0
    while number!=0:
        digit=number%10
        sumDE+=digit
        number/=100
    return sumDE

print getSize(4)
print getSize(37)
print getPrefix(4388576018402626,1)
print getPrefix(4388576018402626,2)
print prefixMatched(4388576018402626,4)
print prefixMatched(4388576018402626,5)
print prefixMatched(4388576018402626,43)
print isValid(4388576018402626)
print isValid(4388576018410707)
print isValid(371826291433349)
print isValid(5411045872559122)
print isValid(6011432717792989)
print isValid(6011432717)

