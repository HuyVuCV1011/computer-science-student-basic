class Warehouse:

    def __init__(self):
        self.listItem = {}

    def total_item(self):
        total = 0

        for value in self.listItem.values():
            total += value

        return total

    def add_item(self, name, value):

        # 2 case:
        # TH1: item da co san, tang value cua hang do len
        # Vi du: list {(ao, 10),(quan, 5),(ao khoac, 3)}
        # add_item(ao,3) -> list {(ao, 13),(quan, 5),(ao khoac, 3)}
        #
        # Th2: item chua co san
        # add_item(giay, 6) -> list {(ao, 13),(quan, 5),(ao khoac, 3),(giay, 6)}
        if name in self.listItem:
            self.listItem[name] = self.listItem[name] + value
        else:
            self.listItem[name] = value

    def checkItem(self, name):
        for item in self.listItem:
            if item == name:
                return True

        return False

    def getItemValue(self, name):
        if self.checkItem(name):
            return self.listItem[name]

        print("Do not have {} in the this warehouse".format(name))

    def getItem(self, name, value):
        if name not in self.listItem:
            print("No item")
        else:
            if self.getItemValue(name) < value:
                print("Not enough")
            else:
                self.listItem[name] = self.listItem[name] - value


A = Warehouse()
print(A)

A.add_item("car",60)
print(A.total_item())



