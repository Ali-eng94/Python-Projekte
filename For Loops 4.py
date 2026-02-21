Basennumber = int(input("Enter the Base number: "))
exp = int(input("Enter the power: "))
result = 1

for i in range(1,exp+1,1):
    result = result * Basennumber

print("the result is " + str(result))

#output:
#Enter the Base number: 454
#Enter the power: 33
#the result is 4817737622188119997671217994085389836958063650413824330084623491372999028633958103384064

Basennumber = float(input("Enter the Base number: "))
exp = int(input("Enter the power: "))
result = 1

for i in range(1,exp+1,1):
    result = result * Basennumber

print("the result is " + str(result))

#output:
#Enter the Base number: 10.5
#Enter the power: 3
#the result is 1157.625