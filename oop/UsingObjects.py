from ObjectsDefined import Car
from ObjectsDefined import Engine
from ObjectsDefined import Wheel

# Instantiate individual objects
my_car = Car("Red", "SUV")
my_engine = Engine()
my_wheels = [Wheel() for _ in range(4)]

# Demonstrate individual object functionality
print("Demonstration of Individual Object Functionality:")
my_car.display_info()  # Output: Car: Red SUV
my_engine.start()      # Output: Engine started.
for wheel in my_wheels:
  wheel.rotate()     # Output: Wheel rotating.