class Animal:
    def move(self):
        print("This animal moves.")

class Giraffe(Animal):
    def move(self):
        print("A giraffe gracefully strides across the savanna. 🦒")

class Elephant(Animal):
    def move(self):
        print("An elephant powerfully walks through the bush. 🐘")

class Human(Animal):
    def move(self):
        print("A person walks along the path. 🚶‍♀️")

def animal_action(animal):
    animal.move()

# Creating instances of different animal classes
gerald_the_giraffe = Giraffe()
ellie_the_elephant = Elephant()
amina_the_human = Human()

animals = [gerald_the_giraffe, ellie_the_elephant, amina_the_human]

# Demonstrating polymorphism
for animal in animals:
    animal_action(animal)