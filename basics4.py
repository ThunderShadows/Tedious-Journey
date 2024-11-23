def good(name,num):
    print(f"Hello {name}")
    print(num)
    return num ** 2

result = good("John",4)
print(result)

message = input("Enter the message: ")
def emojify(message):
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
    return output

print(emojify(message))