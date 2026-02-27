#Multi-level Inheritance
#Multiple Inheritance



#Multi-level Inheritance
class Building:
    def __init__(self,address):
        self.address = address

class Hotel:
    pass

class LuxuryHotel(Hotel,Building):   # it will take on the characteristics of voth class
    pass

