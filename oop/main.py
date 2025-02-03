

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