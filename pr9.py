'''presentYear = input('enter the present year:')
dobYear = input ('enter your date of birth year :')
d=int(presentYear)
e=int(dobYear)
a=d-e
print ('your are at present is :',a)'''
# to calculate age when the year changed:
from datetime import date
enterYourbirthYear = int(input ('enter your age is :'))
currentYearis= date.today().year
a = currentYearis - enterYourbirthYear
print ('your age is :',a)
