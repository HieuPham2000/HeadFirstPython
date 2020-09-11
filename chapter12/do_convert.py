import pprint
from datetime import datetime

# convert time 24 to am/pm: 17:00 => 05:00PM
def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in  data: # không thể viết là data.read() hoặc data.readline()
        k, v = line.strip().split(',')
        flights[k] = v
        
pprint.pprint(flights)
print()

# dict comprehension
flights3 = {convert2ampm(k): v.title() 
            for k, v in flights.items() 
            if v == 'FREEPORT'}
pprint.pprint(flights3)
print()

# list comprehension
flight_times2 = [convert2ampm(ft) for ft in flights.keys()]
print(flight_times2)
print()





    
