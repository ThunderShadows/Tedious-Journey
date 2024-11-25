import module as md

value = int(input("Enter the number: "))
result = int(md.convert_temperature(value))
print(f"The temperature is {result}")

number=[10,20,30,42,512,94]
result1=int(md.max(number))
print(f"The maximum value in the list is {result1}")