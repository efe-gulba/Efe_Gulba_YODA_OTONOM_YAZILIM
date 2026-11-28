def sum(a, b):
    return a + b 

def substraction(a, b):
    return a - b

def division(a, b):
    if b == 0:
        print("!!")
    else:
        return a / b 

def mult(a, b):
    return a * b

myList = []

while True:
    print("Exit - 1")
    print("Previous Calculations - 2")
    print("Continue - 3")

    answer = int(input("Press 1, 2 or 3: "))

    if answer == 1:
        break
    elif answer == 2:
        print("Previous calculations: ")
        for previous in myList:
            print(previous)
        continue
            
        

    

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter a operator + - * /: ")


    if operator == "+": 
        result = sum(num1, num2)
        print(f"The result = {result:.2f}")

    elif operator == "-":
        result = substraction(num1, num2)
        print(f"The result = {result:.2f}")

    elif operator == "/":
        if num2 == 0:
            print("Second number cannot be 0!")
            result = 0
        else:
            result = division(num1, num2)
            print(f"The result = {result:.2f}")

    elif operator == "*":
        result = mult(num1, num2)
        print(f"The result = {result:.2f}")
    
    
    previous = f"{num1:.2f} {operator} {num2:.2f} = {result:.2f}"
    myList.append(previous)
