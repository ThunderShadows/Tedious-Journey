## Handling Exceptions and Errors in Python 
try:
    age = int(input("Enter your age: "))
    income = int(input("Enter your income:"))
    risk = income/age
    print(age)
    print(income)
    print(risk)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Age cannot be zero")

