from operator import itemgetter
from itertools import groupby

rows = [
    {'name': 'John Doe', 'date': '12/01/2018'},
    {'name': 'John Smith', 'date': '12/05/2018'},
    {'name': 'Mark Dobson', 'date': '12/02/2018'},
    {'name': 'P. Hilmiger', 'date': '12/03/2018'},
    {'name': 'Piter Fan', 'date': '12/02/2018'},
    {'name': 'M. Filtron', 'date': '12/05/2018'},
]

rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)
