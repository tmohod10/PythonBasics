import datetime
from array import array

print(datetime.time(15, 45, 2))

print(datetime.date.today())

# this array is memory efficient and optimized than list
arr = array('i', [1, 2, 3])

print(arr[0])
