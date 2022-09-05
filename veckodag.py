
weekdays = ['måndag','tisdag','onsdag','torsdag','fredag','lördag','söndag']

months = ['jan','feb','mars','april','maj','juni','juli','aug','sep','okt','nov','dec']

maxdagar = [31,28,31,30,31,30,31,30,31,30,31]

weekday = input ('Veckodagen den 1a Januari)').lower()
while weekday not in weekdays:
    print ('Fel, mata in en ny veckodag' )
    weekday = input('Veckodagen den 1a Januari)').lower()
wnr = weekdays.index(weekday)

svar = input ('Är det skottår?').lower()
while svar not in ['ja','nej']:
    print ('fel, svara ja eller nej')
    svar =input ('Är det skottår?').lower()

if svar == 'ja':
    maxdagar [1] = 29

for mnr in range (0,12):
    print(months[mnr])
    for dnr in range(0,maxdagar[mnr]):
        print (dnr + 1,' '*5,weekdays[wnr])
        wnr += 1
        if wnr == 7:
            wnr = 0
