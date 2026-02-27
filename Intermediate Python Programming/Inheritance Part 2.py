# -------------------------------
# Base Class (Encapsulation)
# -------------------------------

class Accommodation:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self._isBooked = False   # underscore = protected (Encapsulation idea)

    def describe(self):
        return f"{self.name}, located in {self.location}, Available: {'NO' if self._isBooked else 'YES'}"

    def setAvailability(self, booked):
        self._isBooked = booked


# -------------------------------
# Hotel Class (Inheritance)
# -------------------------------

class Hotel(Accommodation):
    def __init__(self, name, location, roomService):
        super().__init__(name, location)
        self.roomService = roomService

    def amenities(self):
        return "Room Service: Available" if self.roomService else "Room Service: Not Available"


# -------------------------------
# Chalet Class
# -------------------------------

class Chalet(Accommodation):
    def __init__(self, name, location, fireplace):
        super().__init__(name, location)
        self.fireplace = fireplace

    def amenities(self):
        return "Fireplace: Available" if self.fireplace else "Fireplace: Not Available"


# -------------------------------
# Apartment Class
# -------------------------------

class Apartment(Accommodation):
    def __init__(self, name, location, kitchen, privateParking):
        super().__init__(name, location)
        self.kitchen = kitchen
        self.privateParking = privateParking

    def amenities(self):
        return (
            f"Kitchen: {'Available' if self.kitchen else 'Not Available'}, "
            f"Private Parking: {'Available' if self.privateParking else 'Not Available'}"
        )


# --------------------------------
# TEST SECTION
# --------------------------------

chalet1 = Chalet("The Great Chalet", "Lebanon", True)
print(chalet1.describe())  # output : The great chalet, located in lebanon, Available: Yes

chalet1.setAvailability(True)
print(chalet1.describe())     # output : The great chalet, located in lebanon, Available: NO

hotel1 = Hotel("Phoenix Hotel", "New York", False)
apartment1 = Apartment("Phoenix Apartment", "New York", False, True)

print(hotel1.describe(), "-", hotel1.amenities())    #Phoenix Hotel, located in New York, Available: Yes

hotel1.setAvailability(True)
print(hotel1.describe(), "-", hotel1.amenities())
hotel1.isBooked = True      #Phoenix Hotel, located in New York, Available: NO Room Service : Not Available




