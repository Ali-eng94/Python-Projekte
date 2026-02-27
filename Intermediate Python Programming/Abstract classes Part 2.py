from abc import ABC, abstractmethod

class Room(ABC):
    def __init__(self,id,type,price):
        self.id = id
        self.type = type
        self.price = price

    @abstractmethod

    def calculatePrice(self,numDays):
        pass

    @abstractmethod

    def describe(self):
        pass

class SingleRoom(Room):
    def calculatePrice(self,numDays):
        return numDays * self.price

    def describe(self):
        print(f"a Single room with one bed,Base Price: ${self.price} Per Night")

class suiteRoom(Room):
    def calculatePrice(self,numDays):
        return numDays * (self.price * 1.3) + 50

    def describe(self):
        print(f"a suite Room with one double,Base Price: ${self.price * 1.3} Per Night")

class Hotel:
    def __init__(self,name,):
        self.name = name
        self.rooms = []

    def addRoom(self,room):
        self.rooms.append(room)

hotel1 = Hotel("Phoenix Hotel")
hotel1.addRoom(SingleRoom("101","Single",60))
hotel1.addRoom(suiteRoom("102","suite",60))

hotel1.rooms[0].describe()     #output: a Single room with one bed,Base Price: $60 Per Night
print(hotel1.rooms[0].calculatePrice(5))      #output: 300
hotel1.rooms[1].describe()    #a suite Room with one double,Base Price: $78.0 Per Night
print(hotel1.rooms[1].calculatePrice(5))  #output : 440.0
