from item import Item
from orderitem import OrderItem

class Order():
    def __init__(self):
        self.orderitems = []

    def addOrderItems(self, orderitem):
        self.orderitems.append(orderitem)

    def calculateSubTotal(self):
        subTotal = 0.0
        for o in self.orderitems:
            subTotal += o.getItem().price * o.quantity
        return str(subTotal)

    def calculateTax(self):
        tax = 0.0
        for o in self.orderitems:
            tax = (o.getItem().price * o.quantity) * 0.10
        return str(tax)

    def calculateTotal(self):
        total = 0.0
        tax = 0.10
        for o in self.orderitems:
            total += (o.getItem().price * o.quantity) * (1+tax)

        return str(total)
        