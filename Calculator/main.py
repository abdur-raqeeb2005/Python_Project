while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    choose = input("Choose Operation (+, -, *, /) q to quit: ")

    if choose == "+":
        print("Result:",a+b)

    elif choose == "-":
        print("Result:",a - b)   

    elif choose == "*":
        print("Result:",a * b)

    elif choose == "/":
        print("Result:",a / b)

    elif choose == "/":
        if b == 0:
            print("Error: Cannot divide by zero!")
        else: 
            print("Result:",a / b)

    elif choose == "q":
        print("See you next time")
        break

    else:
        print("Invalid Operation")

    