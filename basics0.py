weight = int(input("Enter your weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "L":
    convert = weight * 0.45
    print(f"Your weight in kgs is {convert}")
else:
    convert = weight // 0.45
    print(f"Your weight in pounds is {convert}")