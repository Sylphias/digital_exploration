def extractValues(values):
  return tuple(int(x) for x in values.split(" "))


def calcRatios(values):
  return float(min(values))/float(max(values)) if max(values) != 0 else None

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
    months += [constructCalMonth(month_no+1, first_day_of_month, numDaysInMonth(month_no+1 , leapYear(year)))]
    first_day_of_month = (sumOfDays(year,month_no+1)+dayOfWeekJan1(year))%7 #Optimize this part, running the forloop within a for loop each time is not optimal. Think about it
  cal_year += months
  return cal_year

def sumOfDays(year,month):
  sum_of_days = 0
  for x in range(month):
    sum_of_days += numDaysInMonth(x+1,leapYear(year))
  return sum_of_days

def displayCalendar(calendar_year,month):
  print_cal = ''  
  if month != None:
    first_day_of_month = (sumOfDays(calendar_year,month-1)+dayOfWeekJan1(calendar_year))%7
    year = constructCalMonth(month,first_day_of_month, numDaysInMonth(month,leapYear(calendar_year)))
    for week_info in year:
      if week_info in cal_year:
        print_cal += week_info
        print_cal += '\n' + ' S  M  T  W  T  F  S'
      else:
        print_cal += '\n' + week_info
  else:
    year = constructCalYear(calendar_year)
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
# print displayCalendar(2015,None)
print displayCalendar(2002,3)
print displayCalendar(2002,None)



