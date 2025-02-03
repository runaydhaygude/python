# Implementing instance methods or also called as just methods
class Employee:
    # defining the initializer
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    def tax(self):
        return (self.salary * 0.2)

    def salaryPerDay(self):
        return (self.salary / 30)


# initializing an object of the Employee class
Steve = Employee(3789, 2500, "Human Resources")

# Printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
print("Tax paid by Steve:", Steve.tax())
print("Salary per day of Steve", Steve.salaryPerDay())









# Class Methods
class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @classmethod
    def getTeamName(cls):
        return cls.teamName


print(Player.getTeamName())






# Static Methods
class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @staticmethod
    def demo():
        print("I am a static method.")


p1 = Player('lol')
p1.demo()
Player.demo()





# Access Modifier

class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property
    
    def displaySalary(self):  # displaySalary is a public method
        print("Salary:", self.__salary)

    def __displayID(self):  # displayID is a private method
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
print("ID:", Steve.ID)

try:
    print("Salary:", Steve.__salary)  # this will cause an error
except:
    print("Error accessing private property")

Steve.displaySalary()

try:
    Steve.__displayID()  # this will cause an error
except:
    print("Error accessing private method")


print(Steve._Employee__salary)  # accessing a private property (Not so private)
