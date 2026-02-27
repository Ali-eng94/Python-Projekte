class Hotel:
    def __init__(self,name,location):
        self._name = name
        self._location = location
    def BookungInfo(self):
        return "This Hotel has Standar Rooms"

class LuxuryHotel(Hotel):
    def __init__(self,name,location,amenities):
        super().__init__(name,location)
        self._amenities = amenities
    def BookungInfo(self):
        return "This Hotel has luxary Rooms"                  #will take new one Method
                                                              #This is what we call Method Overriding

hotel = LuxuryHotel("Hotel ALi Haji","San Diego" ,True)
print(hotel.BookungInfo())      #This Hotel has Standar Rooms
print(hotel.BookungInfo())      #This Hotel has luxary Rooms