# Inheritance
# Parent Class
# Child Class


# Parent Class
class Hotel:
    isAvailable = True

    def sayHi(self):
        return "Welcome to our Hotel"

# Child Class
class Room(Hotel):
    def sayBye(self):
        return "Good Bye"

room1 = Room()
print(room1.isAvailable)
print(room1.sayHi())
print(room1.sayBye())

hotel = Hotel()
print(hotel.isAvailable)

#output :

#True
#Welcome to our Hotel
#Good Bye
#True