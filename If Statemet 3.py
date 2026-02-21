number1 = int(input("Please enter a number: "))
op = input("Please enter your operation: ")
number2 = int(input("Please enter second number: "))

if op == "+":
    result = number1 + number2
elif op == "-":
    result = number1 - number2
elif op == "*":
    result = number1 * number2
elif op == "/":
    if number2 == 0:
        result = "undefined(division by zero)"
    else:
        result = number1 / number2
else:
    result = "invalid operation"
print("the result is " + str(result))

#output:
#Please enter a number: 5
# #Please enter your operation: *
#Please enter second number: 10
#the result is 50

#output:
#Please enter a number: 5
#Please enter your operation: /
#Please enter second number: 0
#+the result is undefined(division by zero)