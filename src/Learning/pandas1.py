import pandas as pd
import numpy as np
import datetime

my_array = np.array([1,2,3,4,5])
print(my_array.dtype)

s1 = pd.Series([33, 19, 24, 2, 6])

print(s1)
print(s1.values)
print(s1.index)

data = [33, 19, 24, 2, 6]
index = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri']

s2 = pd.Series(data, index)

print(s2)

dict1 = {'Mon': 33, 'Tues': 24, 'Wed': 40, 'Thurs': 35, 'Fri': 27}
s3 = pd.Series(dict1)

print(s3 / 2)
print(s3.cumsum())

for i,v in enumerate(s3):
    print i,v

list1 = [x*2 for x in s3]
print(list1)

for k, v in s3.iteritems():
    print v*2, k*2

start = datetime.datetime(2017,03,23)
end = datetime.datetime(2017, 03, 30)
step = datetime.timedelta(days=1)
dates=[]

while(start < end):
    dates.append(start.strftime('%d-%m'))
    start += step

print(dates)

dist2 = {"Dates": dates, "Days": ['Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed'], "Temp" : [33, 24, 45, 40, 44, 34, 30]}

temp = pd.DataFrame(dist2)

print(temp.Days)

csv_file = pd.read_csv('C:\\Users\\anandi.ramanathan\\Downloads\\emailStatistics.csv')

print(csv_file)

print(csv_file.Head1.value_counts)

print(csv_file.sort_index(axis=1))

x = csv_file[csv_file.Head2==22]

print(x)

print(csv_file.Head3.sort_values(ascending=False))

print(csv_file.sort_values(ascending=False, by = ['Head4']))