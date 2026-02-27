#Encapsulation
# Public attribute
# Protected attribute
# Private attribute


class Hotel:
    def __init__(self, name, location, rooms):
        self.name = name                         # Public attribute
        self._location = location                # Protected attribute
        self.__rooms = rooms                     # Private attribute


hotel1 = Hotel("Phoenix Hotel", "New York", 50)
print(hotel1.name)
print(hotel1._location)

#output:
#Phoenix Hotel
#New York

