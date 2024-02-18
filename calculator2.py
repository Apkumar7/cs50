#TODO: THIS IS THE SECOND VERSION OF THIS CODE, MORE VERSIONS ARE GOING TO BE COMING WITH COOLER AND COOLER FEATURES THIS IMPLEMENTS FUNCTIONS!!!
#TODO: THIS CODE OFFICIALY WORKS

def multiply():
        #This code asks how many numbers the user would like to multiply which then affects the while loop
        aon = int(input("Enter the amount of numbers you would like to multiply toghether: "))

        #This code is checking whether the user gave a valid amount of numbers to multiply and if not then returning invalid use
        if aon < 2:
            print("Invalid use: Please put give the calculator at least 2 numbers to multiply!")

        #This code is creating a variable that is set to 1 which then changes on every itteration of the while loop
        nd = 1

        #This code is checking whether the variable nd(1) is less than to whatever the user input of aon is
        while nd < aon + 1:

            #This code is asking the user for the number they would like to multiply, this code gets called every itteration of the loop, therfor the user can multiply how many ever numbers they wanted to
            x = float(input(f"Enter in number {nd} that you would like to multiply: "))

            #This code runs through and checks whether this is the first time this code is running because if it is then we need to set x to a different variable so this does not become square root operation
            if nd == 1:
                y = x
            else:
                #This code multiplies whatever y is (y is whatever the first number they inputed is as of the code on like 21) and then x which is the input value that they just inputed and then saves that all in the variable y because next round it multiplies it by the y and x
                y = y*x

            #This checks whether this is the last time the while loop is going to run and if so then the loop will print out the value of whatever j is equal to(the product of all the numbers the user inputed)
            if nd == aon:
                if y <= 1:
                    print(y)
                else:
                    print(round(y))

            #last but not least, this code adds 1 to the variable nd so that this will not be a infinite loop
            nd += 1

def divide():
        #This code is setting the variable
        nd = 1

        #Ask the user how many numbers they would like to divide
        aon = float(input("Enter the amount of numbers you would like to divide: "))

        #This code is a while loop that runs until nd(1) = aon + 1 which is a user input therfor letting the user divide how many ever numbers toghether
        while nd < aon + 1:

            #This code will ask the user for the number that they would like to divide, this code gets called over and over through every itteration of this while loop
            x = float(input(f"Enter number {nd} you would like to divide: "))

            #This if loop is checking whether the loop is on its first itteration if so then it sets y as the first number that they have inputed to divide
            if nd == 1:
                y = x
            else:
                #This like of code divides y by x which is how we get the division factor in this code and then sets y = to that new number
                y = y/x

            #This code checks whether the while loop is on its last itteration if so then it prints out y so that the code is not printing out y every time the while loop runs
            if nd == aon:
                if y <= 1:
                    print(y)
                else:
                    print(round(y))

            #This code changes the variable nd by one which is how we stay out of an infinite loop
            nd += 1
def add():
        #This code will ask the user how many numbers they would like to multiply toghether
        aon = int(input("Enter the amount of numbers you want to add toghether: "))

        #This code makes sure the aon is more than one
        if aon <= 1:
            print("Usage: > 1")

        #this is a variable that will be a part of the while loop
        nd = 1

        #This is the while loop that everything will be in
        while nd < aon + 1:
            #ask user for input of what the numbers they would like to add are, this will run on every itteration of the while loop
            x = float(input(f"Enter number {nd} that you would like to sum: "))

            #if the loop is on its first itteration, then y = x
            if nd == 1:
                y = x
            #else y = y + x
            else:
                y = y + x

            if nd == aon:
                if y < 1:
                    print(y)
                else:
                    print(round(y))

            nd += 1
def subtract():
        #This first code creates a variable thats used in the while loop
        nd = 1

        #this next code uses user input to get the amount of numbers that they would like to subtract
        aon = int(input("Enter the amount of numbers you would like to subtract: "))

        #This next code checks whether aon is a valid number
        if aon <= 1:
            print(f"{aon} is not a valid amount of numbers, try something greater than 1!")

        while nd < aon + 1:
            x = float(input(f"Enter number {nd} that you would like to subtract: "))

            #if the loop is on its first itteration, then y = x
            if nd == 1:
                y = x
            #else y = y - x
            else:
                y = y - x

            if nd == aon:
                if y < 1:
                    print(y)
                else:
                    print(round(y))

            nd += 1
def square():
        #This code is just creating a variable
        nd = 0

        #this code is asking for user input of the number and then making the output an int
        x = float(input("Enter in the number you would like squared: "))

        #this code is multiplying x and x that gives the square root answer and then printing out whatever y is
        y = x*x
        print(y)

print("You have 5 operations you can use: Addition, Subtraction, Multiplication, Division, and Square")
choice = input("What operation would you like to use? ")

choice = choice.lower()

if choice == "multiplication" or "division" or "addition" or "subtraction" or "square":
#------------------------------------------------------------------------------------------------------------------------------------------------------#
    if choice == "multiplication":
        multiply()
#------------------------------------------------------------------------------------------------------------------------------------------------------#
    if choice == "division":
        divide()
#------------------------------------------------------------------------------------------------------------------------------------------------------#
    if choice == "addition":
        add()
#------------------------------------------------------------------------------------------------------------------------------------------------------#
    if choice == "subtraction":
        subtract()
#------------------------------------------------------------------------------------------------------------------------------------------------------#
    if choice == "square":
        square()

else:
    print("This is not a valid operation, try multiplication, division, addition, subtraction, or square")

