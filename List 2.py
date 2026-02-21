num_items = int(input("How many Items: "))             # To calculate how many item in the array

items = []

for i in range(num_items):
    item = input("Enter item : " + str(i+1) + " ")
    items.append(item)

print(items)

#Output:
#How many Items: 5
#Enter item : 1 ALi
#Enter item : 2 Dennis
#Enter item : 3 Markus
#Enter item : 4 Dani
#Enter item : 5 Jeunus
#['ALi', 'Dennis', 'Markus', 'Dani', 'Jeunus']