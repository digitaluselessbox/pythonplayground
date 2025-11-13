class Car:
    __price = 'expensive'

    def receivePrice(self):
        return self.__price


c = Car()

print( c.receivePrice() )

# Car.__price = 'cheap'

# print( c.receivePrice() )
