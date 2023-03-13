
for k in range(13):


    # continue is used to skip an iteration
    # continue me usse upar se saara run hoga toh isko pehle hi lagaio
    if(k==3):
        continue

    # Break is used to get out of the loop
    if(k==9):
        break

    print("5 *", k , "=", 5 * (k ))

    # Do-while loop can be this in java
while True:
    n = int(input("Guess a number"))
    print(n)
    if not n>100:
        break;