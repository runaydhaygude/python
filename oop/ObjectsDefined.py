# Define a simple object representing a car
class Car:
  def __init__(self, color, model):
    self.color = color
    self.model = model

  def display_info(self):
    print("Car: {self.color} {self.model}")

# Define a simple object representing an engine
class Engine:
  def start(self):
    print("Engine started.")

# Define a simple object representing a wheel
class Wheel:
  def rotate(self):
    print("Wheel rotating.")