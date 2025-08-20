class Car:
    def move(self):
        print("Driving on the road 🚗")

class Plane:
    def move(self):
        print("Flying in the sky ✈️")

class Boat:
    def move(self):
        print("Sailing on water ⛵")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Each class defines move() differently
