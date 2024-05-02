first = input("Please enter the First Value ")
opr = input("Please enter the Operator (+,-,x,/)")
second = input("Please enter the Second Value")

first = int(first)
second = int(second)

# first = 30
# opr = "+"
# second = 20

if opr == "+":
    print(first + second)
elif opr == "-":
    print(first - second)
elif opr == "x":
    print(first * second)
elif opr == "/":
    print(first / second)
else:
    print("Invalid Operator")