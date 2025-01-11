
# Variables
day = "Sunday"
print(day)

day = "Monday"
print(day)



# Lists
days_of_week = ["Sunday" , "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(days_of_week)

steps_per_day = [7000, 5500, 10300, 8000, 1200, 2000, 5000]
print(steps_per_day)
steps_per_day.append(27)
print(steps_per_day)


fitness_data = ["Juliana", 7000, 5500, 10300, 8000, 1200, 2000, 5000]
print(fitness_data)
first_index = fitness_data[0]
print(first_index)
last_index = fitness_data[7]
print(last_index)

fitness_data.remove("Juliana")
print(fitness_data)


# If else
num1 = 5
num2 = 8
maximum_num = 0

if num1 >= num2:
    maximum_num = num1
else:
    maximum_num = num2

print(maximum_num)




# for loop
numbers = [5,10,8]
maximum_num = 0
# Write your code here
for num in numbers:
  if num > maximum_num:
    maximum_num = num

print(maximum_num)



# Slice list
fitness_data = ["Juliana", 7000, 5500, 10300, 8000, 1200, 2000, 5000]
slice_list = fitness_data[1:3]
print(slice_list)



# While loop

index = 0
while index <= 9:
    print(index)
    index = index + 1





# Defining function
def hourly_to_daily_step(hourly_steps):
  daily_steps = []
  for i in range(0, len(hourly_steps), 24):
    day_counts = sum(hourly_steps[i:i + 24])
    daily_steps.append(day_counts)
  return daily_steps


data = ["Juliana",857,1178,1134,1133,780,1017,821,1180,0,0,0,0,0,0,0,1032,42,1129,1126,40,1032,743,1194,993,1054,969,1046,924,1064,1117,1094,795,0,0,0,0,0,0,44,26,47,736,22,46,851,27,846,769,1071,942,1010,1055,1011,834,1104,889,0,0,0,0,0,1120,38,1190,1100,959,874,1130,941,813,1106,934,1117,1043,1053,997,1055,1043,824,1183,908,0,0,0,0,0,0,0,937,1188,1145,747,1109,20,984,812,1059,742,739,926,1188,1072,1113,938,0,0,0,0,0,1067,26,29,45,722,796,32,28,36,1094,896,798,1101,963,928,829,842,1136,1115,0,0,0,0,0,0,0,27,769,26,1133,830,20,43,869,924,990,1000,963,768,1003,754,788,0,0,0,0,0,0,33,35,37,853,50,797,35,21,46,950,1099]

name = data[0]
hourly_steps = data[1:]

daily_steps = hourly_to_daily_step(hourly_steps)
print("Daily steps:", daily_steps)




# Importing numpy and reading single data value
import numpy

data = numpy.loadtxt('data.txt')

print(data)


# Reading multiple values
num1, num2 = numpy.loadtxt('data-two-values.csv', delimiter=',')
print(num1, num2)


# Loading multiples values into list
data_list = numpy.loadtxt('data-multiple-values.csv', delimiter=',')
print(data_list)


# Reading mixed data types

try:
   data = numpy.loadtxt('data-mixed-types.csv', delimiter = ',')
   print(data)
except:
   print("mixed data type error")


# Resolving the exception around mixed data types
data = numpy.loadtxt('data-mixed-types.csv', delimiter=',', dtype='str')
print(data)


# Convert the data types
data = numpy.loadtxt('data-mixed-types.csv', delimiter = ',', dtype = 'str')

name = data[0]
steps = data[1:]
steps = steps.astype(int)

print(type(steps[0]))

