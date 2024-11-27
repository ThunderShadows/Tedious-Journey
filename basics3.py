## Dictionaries in Python
phone_no = input("Enter the phone number: ")
numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
for i in phone_no:
    print(numbers.get(i,"Invalid Number"), end=" ")

message = input("Enter the message: ")
words = message.split()
emojis = {
    ":)" : "😊",
    ":(" : "😔",
    ":D" : "😁",
    ":O" : "😮",
    ":P" : "😛"
}
output =""
for word in words:
    output+= emojis.get(word,word) + " "
print(output)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

my_dict_2 = dict(name="Lisa", age=27, city="Boston")
print(my_dict_2)
