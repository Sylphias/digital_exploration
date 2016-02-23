#I did this while sleep deprived..... less comments for now
# Not optimized, refactor when have time
import random
def craps():
  dice_1, dice_2 = random.randrange(1,7), random.randrange(1,7)
  dice_sum = dice_1+dice_2
  print "You rolled " + str(dice_1)+ " + " +str(dice_2) + " = "+ str(dice_sum)
  if dice_sum == 7 or dice_sum == 11: return "You win"
  elif dice_sum == 2 or dice_sum == 3 or dice_sum ==12: return "You lose"
  else:
    print "Your point is " + str(dice_sum)
    old_dice_sum = dice_sum
    while dice_sum != 7 or dice_sum != old_dice_sum:
      dice_1, dice_2 = random.randrange(1,7), random.randrange(1,7)
      dice_sum = dice_1 + dice_2
      print "You rolled " + str(dice_1)+ " + " +str(dice_2) + " = "+ str(dice_sum)
      if dice_sum == 7: return "You lose" 
  return "You win"

# print craps()

def factorial(n):
  if n == 0: return 1
  return n*factorial(n-1)
# print factorial(5)

import math
cal_year = ['January','February','March','April','May','June','July','August','September','October','November','December']

def leapYear(year):
  if year%4 !=0:
    return False
  elif year%100 != 0:
    return True
  elif year%400 != 0:
    return False
  else:
   return True


def dayOfWeekJan1(year):
  def r_function (y,x):
    return y%x
  return r_function(1+5*r_function(year-1,4)+4*r_function(year-1,100)+6*r_function(year-1,400),7)


def numDaysInMonth(month_num,leap_year):
  if month_num >0 and month_num <13:
    return (28 + leap_year) if month_num == 2 else 31 - (month_num - 1) % 7 % 2;

def constructCalMonth(month_num, first_day_of_month, num_days_in_month):
  calendar = [cal_year[month_num-1]]
  first_row= ' '
  day = 1
  if first_day_of_month!=0:
    for x in range(7):
      if x<first_day_of_month:
        first_row +='   '
      elif x == 6: 
        first_row +=str(day)
        day+=1
      else:
        first_row +=str(day) + '  '
        day +=1
    calendar += [first_row]
 
  row = ''
  day_counter =1
  for y in range(day,num_days_in_month+1):
    if y<=9:
      if day_counter%7==0:
        row += ' '+str(y)
        calendar += [row]
        row =''
      else:
        row +=' '+str(y)+' '
    else:
      if day_counter%7==0 or y == num_days_in_month:
        row+= str(y)
        calendar +=[row]
        row =''
      else:
        row += str(y)+' '
    day_counter+=1

  return calendar


def constructCalYear(year):
  cal_year = [year]
  months=[]
  sum_of_days =0
  first_day_of_month = dayOfWeekJan1(year)
  for month_no in range(12):
    sum_of_days += numDaysInMonth(month_no+1 , leapYear(year))
    months += [constructCalMonth(month_no+1, first_day_of_month, numDaysInMonth(month_no+1 , leapYear(year)))]
    first_day_of_month = (sum_of_days+dayOfWeekJan1(year))%7
  cal_year += months
  return cal_year


def displayCalendar(calendar_year):
  year = constructCalYear(calendar_year)
  print_cal = ''
  for x in range(1,len(year)):
    for week_info in year[x]:
      if week_info in cal_year:
        if week_info != 'January':
          print_cal +='\n\n' 
        print_cal+= week_info
        print_cal += '\n' + ' S  M  T  W  T  F  S'
      else:
        print_cal += '\n' +week_info
       
  return print_cal
