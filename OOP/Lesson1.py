class Garage:
    listCar = []
    totalPrice = 0

    def __init__(self, name):
        self.ownerName = name

    def checkCar(self, carName):
    #Neu co thi return true, neu khong thi return false
        for i in self.listCar:
            if carName == i[0]:
                return True
        return False

    def addCar(self, carName, price):
        if self.checkCar(carName):
            print('you already have this one')

        else:
            self.listCar.append([carName, price])
            self.totalPrice += price
    # def sellCar(self, carName):
    # #tru total price
    #pop
    def sellCar(self, carName):
        for i in self.listCar:
            if i[0] == carName:
                self.totalPrice -= i[1]
                self.listCar.remove(i)
                break
    # def price(self):
    # #Return ve total price
    #
    # def myCars(self):
    # #In ra toan bo chiec xe minh dang co trong list car






    def myCars(self):
        print('You have: ')

        for i in self.listCar:
            print(i[0])

A = Garage("Johny")
A.addCar("toyota",100)
A.addCar("mercedes",10)
A.addCar("bmw",100)

print(A.listCar)