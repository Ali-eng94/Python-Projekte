try:
    x = int(input("enter first number"))
    y = int(input("enter second number"))

    print(x / y)

except ValueError:
    print(" You can't divide int by string")

except ZeroDivisionError:
    print(" You can't divide by zero")

# If you have a problem with the code. you can report the error here along with the reason for the error




