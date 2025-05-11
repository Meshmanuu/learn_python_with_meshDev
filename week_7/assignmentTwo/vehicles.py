class Vehicle:
    def move(self):
        print("This vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("Driving along the road. 🚗")

class Airplane(Vehicle):
    def move(self):
        print("Flying high above. ✈️")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling through the town. 🚴‍♀️")

class Motorcycle(Vehicle):
    def move(self):
        print("Riding on two wheels. 🏍️")

def vehicle_action(vehicle):
    vehicle.move()

if __name__ == "__main__":
    my_car = Car()
    a_plane = Airplane()
    a_bicycle = Bicycle()
    a_motorcycle = Motorcycle()

    vehicles = [my_car, a_plane, a_bicycle, a_motorcycle]

    for vehicle in vehicles:
        vehicle_action(vehicle)