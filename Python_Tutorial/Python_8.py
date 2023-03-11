# While Loop
# It is same as normal while loop

i = int(input("Enter the number: "))
while(i<69):
    print("Re-enter the value of i")
    i = int(input("Enter the number: "))
    # print(i)
print("Finally!! You have guessed it ")

# The above one is an example of incrementing while loop
# The below one is an example of decrementing while loop

# We can use else also in while
coutn = 9
while(coutn>2):
    print(coutn)
    coutn -= 1

else:
    print("Inside the else statement and outside the while")


# There is no do-while loop in python
