
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