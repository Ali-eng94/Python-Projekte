#logical operators or and

temp = int(input("Please enter the temperature out side: "))

name = "ALi"

if temp > 50 and temp < 30 and name== "ALi":
    print("the weather is good today")
elif temp < 0 or temp > 30:
    print("the weather is not good today")

#output:
#Please enter the temperature out side: 50
#the weather is not good today
