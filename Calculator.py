#Calculator Project

def add(x, y):
    return(x+y)

def subtract(x, y):

    if(x>y):
        return (x-y)
    elif(y>x):
        return f"{x-y}"
    else:
        return ("Invalid")

def multiply(x,y):

    if(x == 0):
        return ("Zero")
    elif(y==0):
        return ("Zero")
    else:
        return(x*y)

def divide(x,y):

    if(y==0):
        return ("Cannot do this")
    elif (x==0):
        return ("Zero")
    else:
        return(float(x/y))

do(
print("Please select operation \n"\
    "1. Add\n" \
    "2. Subtract\n" \
    "3. Multiply\n" \
    "4. Divide\n")
select = int(input("Select:"))
x = int(input("Enter the first number = "))
y = int(input("Enter the second number = "))

if select == 1:
    print(add(x,y))

elif select == 2:
    print(subtract(x,y))

elif select == 3:
    print(multiply(x,y))

elif select == 4:
    print(divide(x,y))

else:
    print("Invalid ! ")
)while(select <5):
    print("Bye")
    break



