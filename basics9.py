from pathlib import Path 

path = Path("ecommerce/shipping.py")
print(path.exists())

path1=Path()
for file in path1.glob("*.py"):
    print(file)

for file1 in path1.iterdir():
    print(file1)

    