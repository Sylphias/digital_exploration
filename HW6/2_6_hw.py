def binaryToDecimal(binaryStr):
  return int(binaryStr,2)


# print binaryToDecimal('100')
# print binaryToDecimal('101')
# print binaryToDecimal('10001')
# print binaryToDecimal('10101')

def uncompressed(s):
  uncompressed = ""
  for x in range(len(s)):
    if s[x].isdigit():
      for y in range(int(s[x])):
        uncompressed += s[x+1]
  return uncompressed

# print uncompressed("2a5b1c")

import string
import re
UpperCase = string.ascii_uppercase

def getBaseCounts2(dna):
  dna_dict = {'A':0,'C':0,'G':0,'T':0}
  for x in dna:
    if x.isupper():
      if re.match(r'[ATCG]',x) : dna_dict[x]+=1
    else:
      return "The input DNA string is invalid"
  return dna_dict

# print getBaseCounts2("ATCGGG")
# print getBaseCounts2("ATCGGGIII")
# print getBaseCounts2("Aaaatc")
# print getBaseCounts2("ADLSTTLLD")
# print getBaseCounts2("Aaaatc")
# print getBaseCounts2("Aaaatc")
f=open('constants.txt')
def fundamentalConstants(f):
  constants = [x.split() for x in f.readlines()]
  return {c[0]:float(c[1]) for c in constants[2:]}

print fundamentalConstants(f)
f=open('scores.txt')
def scores(f):
  scores = [float(x.strip()) for x in f.readlines() if x !='\n']
  return sum(scores), sum(scores)/len(scores)

# scores(f)
