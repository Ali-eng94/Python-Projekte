# Ask the user to enter the number of shoes available in inventory
NumberofShoes = int(input("Enter the number of shoes: "))

# Create an empty list to store shoe sizes
myList = []

print("Enter the shoe sizes: ")

# Loop to collect each shoe size
for i in range(NumberofShoes):
    # Prompt the user to enter a shoe size
    item = int(input("Enter the shoe size number: " + str(i + 1) + ": "))

    # Add the size to the list
    myList.append(item)

# Ask the user to enter the number of customers
NumberofCustomers = int(input("Enter the number of Customers: "))

# Variable to store the total income
total_income = 0

# Loop through each customer
for i in range(NumberofCustomers):
    # Ask for the customer's requested shoe size
    ShoesSize = int(input("Enter the shoe size for customer: " + str(i + 1) + ": "))

    # Ask for the price offered by the customer
    Price = int(input("Enter the shoe price for customer: " + str(i + 1) + ": "))

    # Check if the requested size is available
    if ShoesSize in myList:
        # Add the price to total income
        total_income += Price

        # Remove the sold shoe from inventory
        myList.remove(ShoesSize)

# Display the total income from sold shoes
print("Total income from sold shoes:", total_income)

#output:

#Enter the number of shoes: 3
#Enter the shoe sizes:
#Enter the shoe size number: 1: 50
#Enter the shoe size number: 2: 45
#Enter the shoe size number: 3: 43
#Enter the number of Customers: 2
#Enter the shoe size for customer: 1: 50
#Enter the shoe price for customer: 1: 60
#Enter the shoe size for customer: 2: 45
#Enter the shoe price for customer: 2: 75
#Total income from sold shoes: 135