from abc import ABC, abstractmethod


# -------------------------------
# Abstract Base Class
# -------------------------------

class Accommodation(ABC):

    @abstractmethod
    def getDetails(self):
        pass

    @abstractmethod
    def calculatePrice(self):
        pass


# -------------------------------
# Concrete Child Class
# -------------------------------

class Hotel(Accommodation):

    def __init__(self, name, price_per_night):
        self.name = name
        self.price_per_night = price_per_night

    def getDetails(self):
        return f"Hotel Name: {self.name}"

    def calculatePrice(self):
        return f"Price per night: {self.price_per_night}"


# -------------------------------
# Test
# -------------------------------

hotel1 = Hotel("Phoenix Hotel", 120)

print(hotel1.getDetails())
print(hotel1.calculatePrice())

#output:
#Hotel Name: Phoenix Hotel
#Price per night: 120