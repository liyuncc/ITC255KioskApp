from item import Item
from orderitem import OrderItem
from order import Order


def main():

    item1 = Item(1, 'medium fries', 4.00)
    item2 = Item(2, 'chicken nuggets', 5.50)
    item3 = Item(3, 'large coke', 2.25)
    
    orderitem1 = OrderItem(item1, 2)
    orderitem2 = OrderItem(item2, 4)
    orderitem3 = OrderItem(item3, 2)

    order = Order()
    order.addOrderItems(orderitem1)
    order.addOrderItems(orderitem2)
    order.addOrderItems(orderitem3)

    print("Here's your order summary: ")
    print(item1)
    print(item2)
    print(item3)


    subTotal = order.calculateSubTotal()
    tax = order.calculateTax()
    total = order.calculateTotal()
    print("Subtotal $" + subTotal)
    print("Tax $" + tax)
    print("Your total is $" + total)


main()