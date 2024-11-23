## While Loops and use of if conditions in Python
count=0
while count<3:
    number = int(input("Guess the number:"))
    if number == 5:
        print("Correct guess")
        break
    count=count+1

command = ""
started = False
while True:
    command = input("Enter a command: ").lower()
    if command == "help":
        print("Start- To start the car")
        print("Stop- To stop the car")
        print("Quit- To quit")
    elif command == "start":
        if started:
            print("Car is already started")
            continue
        else:
            started = True
            print("Car started")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car is stopped")
    elif command == "quit":
        break
    else:
        print("Undefined Command")