class Hotel:
    def __init__(self,type):
        self.__type = type

    def RoomType(self):
        return f"The Type is {self.type}"

    def type(self):    #getter
        return self.__type
    def SetType(self,value):
        if value in ["single","double","suite"]:
            self.__type = value
        else:
            raise TypeError("invalid Room type")

hotel1 = Hotel("signle")
print(hotel1.type())       # signle

hotel1.SetType("single")
print(hotel1.type())     #single
hotel1.SetType("double")
print(hotel1.type())     #double
hotel1.SetType("suite")
print(hotel1.type())     #suite
hotel1.SetType("Ali Haji")
print(hotel1.type())      #error 