

# Class declaration
class MyClass:
    pass

obj = MyClass()  # creating a MyClass Object
print(obj)



class Employee:
    # defining the properties and assigning them none
    # you have to initialize or else it won't compile
    ID = None
    salary = None
    department = None

# cerating an object of the Employee class
Steve = Employee()

# printing properties of Steve - an object of the Employee class
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)


# assigning values to properties of Steve - an object of the Employee class
Steve.ID = 3789
print("ID =", Steve.ID)




class EmployeeWithInitializer:
    # defining the properties and assigning them None
    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary = salary
        self.department = department


# creating an object of the Employee class with default parameters
Steve = EmployeeWithInitializer(3789, 2500, "Human Resources")

# Printing properties of Steve
print("ID :", Steve.ID)
print("Salary :", Steve.salary)
print("Department :", Steve.department)








class EmployeeWithOptionaParameters:
    # defining the properties and assigning None to them
    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department


# creating an object of the Employee class with default parameters
Steve = EmployeeWithOptionaParameters()
Mark = EmployeeWithOptionaParameters("3789", 2500, "Human Resources")

# Printing properties of Steve and Mark
print("Steve")
print("ID :", Steve.ID)
print("Salary :", Steve.salary)
print("Department :", Steve.department)
print("Mark")
print("ID :", Mark.ID)
print("Salary :", Mark.salary)
print("Department :", Mark.department)