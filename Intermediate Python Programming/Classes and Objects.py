# Object Oriented Programming (OOP)
# Classes and Objects Example

class Hotel:
    def _init_(self, name, location, area):
        # Constructor (initializer) that runs when a new object is created
        # It assigns values to the object's attributes
        self.name = name          # Hotel name
        self.location = location  # Hotel location (city)
        self.area = area          # Hotel area (size)

    def SayWelcome(self):
        # Method that prints a welcome message
        print("Welcome to our Hotel")


# Creating objects (instances) of the Hotel class
hotel1 = Hotel("Phoenix Hotel", "San Francisco", 1000)
hotel2 = Hotel("The Great Hotel", "Washington", 500)

# Accessing and printing attributes of hotel1
print(hotel1.name)
print(hotel1.location)
print(hotel1.area)

# Calling a method of hotel1
hotel1.SayWelcome()

# Accessing and printing attributes of hotel2
print(hotel2.name)
print(hotel2.location)
print(hotel2.area)

# Calling a method of hotel2
hotel2.SayWelcome()


# Expected Output:
# Phoenix Hotel
# San Francisco
# 1000
# Welcome to our Hotel
# The Great Hotel
# Washington
# 500
# Welcome to our Hotel


class Room:
    def _init_(self, roomNumber, type, price):
        # Constructor that initializes room details
        self.roomNumber = roomNumber  # Room number
        self.type = type              # Room type (single / double)
        self.price = price            # Room price

    def isAvailable(self):
        # Method that prints room availability status
        print("The Room is Available")


# Creating Room objects
room1 = Room("101", "single", 60)
room2 = Room("102", "double", 120)

# Accessing attributes and calling methods
print(room1.roomNumber)
room1.isAvailable()

# Expected Output:
# 101
# The Room is Available