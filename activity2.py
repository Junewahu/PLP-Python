# Define the base class Animal
class Animal:
    def move(self):
        pass  # Placeholder for polymorphism

    # Define the Dog subclass
class Dog(Animal):
    def move(self):
        print("Running on four legs!")

# Define the Bird subclass
class Bird(Animal):
    def move(self):
        print("Flying in the sky!")

# Define the Fish subclass
class Fish(Animal):
    def move(self):
        print("Swimming in the water!")

# Create objects of each subclass
my_dog = Dog()
my_bird = Bird()
my_fish = Fish()

# Call the move() method on each object
my_dog.move()
my_bird.move()
my_fish.move()

# Defining vehicle classes
class Car:
    def move(self):
        print("Driving on the road 🚗")

class Plane:
    def move(self):
        print("Flying in the air ✈️")

# Creating objects and calling the move() method
vehicles = [Car(), Plane()]

for vehicle in vehicles:
    vehicle.move()