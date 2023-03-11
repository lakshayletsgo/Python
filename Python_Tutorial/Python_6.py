# If-else Statement
a = int(input("Enter your age: "))
print("Your age is ",a)
if(a>18):
    print("You can drive")
    print("This is inside the if condition ")
else:
    print("You can't drive")
    print("This is inside the else statement")
print("This is outside the if-else condition ")


# This is nested if
if(a<10):
    print("This is inside the if statement")
    if(a>5):
        print("The number is greater than 5 but less than 10 ")
    elif(a<5):
        print("The number is less than 5")
    else:
        print("The number is 5")
elif(a>10):
    print("This is elif, It's like else if ")
else:
    print("This is inside the else statement")


# Create a program that says good morning or good afternoon according to the time
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
# print(timestamp)
if(timestamp>=12):
    print("Good afternoon")
else:
    print("Good morning")