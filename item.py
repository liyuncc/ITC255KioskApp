class Item():
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        

    def getItemID(self):
        return self.id

    def getItemName(self):
        return self.name
    
    def getItemPrice(self):
        return self.price

    def __str__(self):
        return self.name + "price: " + self.price


  