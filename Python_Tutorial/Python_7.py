# Match-Case Statement
# Match-Case is same as switch case but in this we can have multiple default cases by using if condition
x = int(input("Enter the value: "))
match x:
    case 0:
        print("x is 0")
    case 10:
        print("x is 10 ")
    case _ if x!=100:
        print("This is default case, X don't match any case")
    case _ if x==100:
        print("This is default case 2, X is 100")


# For Loops
a  = "Lakshay"
for i in a:
     print(i,end=',')
     if(i=='a'):
         print("\nThere is an a in the line")

colors  = ["Red","Blue","Orange","Green"]
for i in colors:
    print(i)


for k in range(10):
    print(k)    # This will print numbers from 0 to 9

for a in range(10):
    print(a+1)

for ka in range(1,10):
    print(ka)    # Both are same

for b in range(2,10,5):
    print(b)  # The third index tells about the skip function i.e it will skip five iteration directly