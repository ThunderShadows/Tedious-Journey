## Classes and object creation and constructors in Python
class Skills:
    def draw(self):
        print("Drawing")

    def speak(self):
        print("Speaking")
    
    def dance(self):
        print("Dancing")

person1=Skills()
person2=Skills()
person1.draw()
person2.dance()
person1.name="John"
person1.age=10
person2.name="Jane"
person2.age=20

print(person1.name)
print(person2.age)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def talk(self):
        print("Talking")
    

john=Person("John",10)
print(f"The person's name is {john.name} and age is {john.age}")