age = int(input("Enter your age: "))

if age < 18:
    print("your need to be above 18 to enter the cinema")
else:
    ticket = input("do you have a ticket(yes/no)")
    if ticket == "no":
        print("you need a ticket to enter the cinema")
    elif ticket == "yes":
        if age > 21:
            print("you can access all movies")
        else:
            print("you can access some movies")

#output:
#Enter your age: 19
#do you have a ticket(yes/no)no
#you need a ticket to enter the cinema

#Enter your age: 25
#do you have a ticket(yes/no)yes
#you can access all movies
