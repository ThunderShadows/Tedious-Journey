def convert_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def convert_temperature(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def max(number):
    max=0
    for i in number:
        if i>max:
            max=i
    
    return max