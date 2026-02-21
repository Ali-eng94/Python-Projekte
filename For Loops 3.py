Number = int (input("Enter a number: "))
result = 1

for i in range(1,Number+1,):
    result = i * result

print("The result is " + str(result))

#output:
#Enter a number: 5
#The result is 120
