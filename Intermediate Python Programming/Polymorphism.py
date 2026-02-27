#Polymorphism

class HotelRoom():
    def price(self):
        pass

class SingleRoom(HotelRoom):
    def price(self):
        return "Price is 100$ Per Night"

class DoubleRoom(HotelRoom):
    def price(self):
        return "Price is 150$ Per Night"

class SuiteRoom(HotelRoom):
    def price(self):
        return "Price is 200$ Per Night"

single1 = SingleRoom()
double1 = DoubleRoom()
suite1 = SuiteRoom()
print(single1.price())    # output: Price is 100$ Per Night
print(double1.price())    # output: Price is 150$ Per Night
print(suite1.price())     # output: Price is 200$ Per Night
