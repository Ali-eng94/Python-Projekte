#Property Decorator

class Hotel:
    def __init__(self,type):
        self.type = type

    @property
    def RoomType(self):
        return f"The Type is {self.type}"

hotel = Hotel(Hotel.RoomType)
print(hotel.RoomType)     # output : The Type is <property object at 0x000001F6DDBBF1A0>

hotel = Hotel("single")
print(hotel.RoomType)        # output : The Type is single