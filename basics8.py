# Creating Packages and importing the methods andc classes and using them in Python
import module as md # Refer to module directory in the file directory structure
import random as rd
import ecommerce.shipping as eship # Refer to ecommerce directory in the file directory structure

value = int(input("Enter the number: "))
result = int(md.convert_temperature(value))
print(f"The temperature is {result}")

number=[10,20,30,42,512,94]
result1=int(md.max(number))
print(f"The maximum value in the list is {result1}")

eship.calc_shipping()

captains = ["Jack Sparrow", "Will Turner", "Elizabeth Swann"]
true_captain = rd.choice(captains)
print(true_captain)

first_value=rd.randint(1,6)
second_value=rd.randint(1,6)
print(first_value,second_value)