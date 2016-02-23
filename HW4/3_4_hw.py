def interlock(word1, word2, word3):
  if len(word1) ==0 or len(word2)==0 or len(word3) == 0: return False  #ensures that the words are not blank
  word2_position = 0
  word1_position = 0
  joined_word = ""
  for letter_position in range (len(word1+word2)):
    if letter_position%2 == 0 : #This if will allow me to alternate the characters
      joined_word += word1[word1_position] #Add the letter at the current word 1 position to the joined word
      word1_position += 1 #update word 1 counter position
    else:
      joined_word+= word2[word2_position]#Add the letter at the current word 2 position to the joined word
      word2_position +=1 #update the word 2 counter position

  return joined_word == word3 #this statement will do a comparison and return true/false

#print interlock('shoe','cold','schooled')

import random
import time
random.seed(round(time.time()/3,-1))   #do not seed elsewhere in your code

def throwNdice(n, nExp):
  rolled_six_counter = 0 # This is to count the number of successful experiments
  for y in range(nExp): # This is to run y number of experiments
    probability= False # Reset the probablility to default state every time you finish one experiment
    for x in range (n): # This is to run x number of rolls
      if random.randrange(1,7) == 6: probability = True #if any instance of an experiment rolls a 6, we immediately take it as a successful experiment
    if probability == True : rolled_six_counter +=1 #add to the counter

  return round(float(rolled_six_counter)/float(nExp),2) #we divide the number of successful experiments with the total number of experiments to get probablility

# print throwNdice(1, 100000) #0.17
# print throwNdice(1, 200000) #0.17
# print throwNdice(1, 300000) #0.17
# print throwNdice(2, 500000) #0.31
# print throwNdice(2, 600000) #0.31

import math
import random
import time
random.seed(round(time.time()/3,-1)) #do not seed elsewhere in your code

def piApproxByMonteCarlo(numThrows):
  #okay through research basically its just a ratio of how often you hit the circle inside a square of the with length/height of 2*radius
  r = 1 #radius
  successful_throws = 0
  for x in range(numThrows):
    #define an x,y coordinate system with random
    x = random.random()
    y = random.random()
    if x**2+y**2 < r**2:
      successful_throws+=1
  return round(4*(float(successful_throws)/float(numThrows)),2)
# print piApproxByMonteCarlo(100)
# print piApproxByMonteCarlo(100000)
# print piApproxByMonteCarlo(10000000)


#### name your function game
import math
import random
import time
random.seed(round(time.time()/3,-1)) #do not seed elsewhere in your code

def game(r, N):
  cash = 0
  for x in range(N):
    #for readability reasons, I wont squeeze this
    cash -=1 #You pay a dorrah to play this round
    dice1 = random.randrange(1,7)
    dice2 = random.randrange(1,7)
    dice3 = random.randrange(1,7)
    dice4 = random.randrange(1,7)
    if dice1+dice2+dice3+dice4 < 9:
      cash += r #You won r dorrahs!
  return (True if cash > 0 else False)

# print game(2,1000)
# print game(9,1000)
# print game(8,1000)
# print game(50,1000)











