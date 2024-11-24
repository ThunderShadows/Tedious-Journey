## Concept of Inheritance in Python
class Mammal:
    def __init__(self,animal):
        self.animal=animal
    
    def walk(self):
        print(f"{self.animal} is walking")

class Dog(Mammal):
    def bark(self):
        print("The Dog is barking")

class Cat(Mammal):
    def meow(self):
        print("The cat is meowing")

dog=Dog("Dog")
dog.walk()
dog.bark()

cat=Cat("Cat")
cat.meow()
cat.walk()