import random

x = random.randint(1,10)
y = random.random()

print(x)# Each time he takes a different number
print(y) # it will print a number with a dot

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)

print(z) #it will constantly choose between rock paper scissors

cards = [1,2,3,4,5,6,7,8,9, "J" , "Q" , "K" , "A"]

random.shuffle(cards)
print(cards) # The array order will be constantly shuffled