## Loops and lists in Python
nums=[5,2,5,2,2,2] 
for i in nums:
    output=""
    for j in range(i):
        output+="x"
    print(output)

names=['Hi','Bye','Hello']
for name in names:
    print(name)

numbers=[2,5,34,133,60]
max=0
for i in numbers:
    if i>max:
        max=i
print(max)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    for i in row:
        print(f"{i}\t",end="")
    print()

numbers1=[5,8,3,72,71,9,5,5]
numbers1.append(10)
print(numbers1)
numbers1.pop()
print(numbers1)
numbers1.remove(3)
print(numbers1)
numbers1.insert(1,3)
print(numbers1)
numbers1.sort()
print(numbers1)
print(numbers1.index(8))
numbers1.reverse()
print(numbers1)
print(numbers1.count(5))
numbers2=numbers1.copy()
numbers2.append(10)
print(numbers2)

a=[1,2,2,2,3,3,4,5,6,6,6]
for i in a:
    if a.count(i)>1:
        a.remove(i)
print(a)

a1=(1,2,3)
print(a1)

a3=[1,2,3]
x,y,z=a3
print(x,y,z)