# read the data from the csv file
# store the data in a hash table

import csv

arr = []

with open('nyc_weather.csv') as nyc:
  lines = nyc.readlines()
  for line in lines[1:8]:
    #print(line)
    day, temp = line.split(',')
    arr.append(int(temp))

nyc.close()

avg = sum(arr) // len(arr)

print(avg)

  