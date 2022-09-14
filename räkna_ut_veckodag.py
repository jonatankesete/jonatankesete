
#Jonatan Kesete, 990724-9099

day = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']

months = ['jan','feb','mars','april','maj','juni','juli','aug','sep','okt','nov','dec']

maxdagar = [31,28,31,30,31,30,31,30,31,30,31]

year = int(input('Year: '))
while year < 1583 or year > 9999:
    print ('Out of allowed range 1583 to 9999')
    year = int(input('Year: '))

month = int(input('Month: '))
while month  <  1 or month  > 12:
    print ('Out of allowed range 1 to 12')
    month = int(input('Month: '))


day = int(input('Day: '))
if year %400 == 0 or ( year %4 == 0 or year %100 !=0):
    while month == 2 and (day  <  1 or day  > 29):
         print ('Out of allowed range 1 to 29')

while month in (1,3,5,7,8,10,12) and (day <  1 or day> 31):
    print ('Out of allowed 1 to 32')
    day = int(input('Day: '))

while month in (4,6,9,11) and (day <  1 or day  > 30):
    print ('Out of allowed 1 to 30')
    day = int(input('Day: '))

else:
    while month == 2 and (day <  1 or day  > 28):
        print ('Out of allowed 1 to 28')
        day = int(input('Day: '))

    while month in (1,3,5,7,8,10,12) and (day <  1 or day  > 31):
        print ('Out of allowed 1 to 31')
        day = int(input('Day: '))

if month == 1 or month == 2:
    month += 12
    year -= 1
    
weekday = ( day + 13*(month+1)//5 + year + year//4
 - year//100 + year//400 ) % 7
if weekday == 0:
    print ('It is a Saturday')

elif weekday == 1:
    print ('It is a Sunday')

elif weekday == 2:
    print ('It is a Monday')

elif weekday == 3:
    print ('It is a Tuesday')

elif weekday == 4:
    print ('It is a Wednesday')
    
elif weekday == 5:
    print ('It is a Thursday')

elif weekday == 6:
    print ('It is a Friday')
