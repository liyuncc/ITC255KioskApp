from item import Item
from orderitem import OrderItem

class Order():
    def __init__(self):
        self.orderitems = []

    def addOrderItems(self, orderitem):
        self.orderitems.append(orderitem)

    def calculateTotal(self):
        total = 0.0
        for o in self.orderitems:
            total += o.getItem().price * o.quantity

        return str(total)