import unittest
from item import Item
from orderitem import OrderItem
from order import Order
from payment import Payment

class ItemTest(unittest.TestCase):
    def setUp(self):
        self.item = Item(1, 'sundae', 3.50)
    
    def test_getItemID(self):
        self.assertEqual(str(self.item.getItemID()),'1')

    def test_getItemName(self):
        self.assertEqual(str(self.item.getItemName()),'sundae')

    def test_getItemPrice(self):
        self.assertEqual(self.item.getItemPrice(), 3.50)



class OrderItemTest(unittest.TestCase):
    def setUp(self):
        self.item=Item(1,'iced mocha', 2.75)
        self.quantity=2
        self.orderitem=OrderItem(self.item, self.quantity)

    def test_getItem(self):
        self.item = self.orderitem.getItem()
        self.assertEqual(str(self.item),'iced mocha')

    def test_getItemPrice(self):
        self.item = self.orderitem.getItem()
        self.assertEqual(self.item.getItemPrice(), 2.75)

    def test_getQuantity(self):
        self.assertEqual(self.orderitem.getQuantity(),2)
    


class OrderTest(unittest.TestCase):
    
   def setUp(self):
       self.o=Order()
       self.item1=Item(1,'spicy chicken sandwich meal', 10.00)
       self.item2=Item(2,'sundae', 3.00)
       self.item3=Item(3,'apple pie', 2.00)

       self.orderitem1=OrderItem(self.item1,1)
       self.orderitem2=OrderItem(self.item2,3)
       self.orderitem3=OrderItem(self.item3,2)

       self.o.addOrderItems(self.orderitem1)
       self.o.addOrderItems(self.orderitem2)
       self.o.addOrderItems(self.orderitem3)

   def test_getOrderItems(self):
        self.oitems=self.o.getOrderItems()
        self.assertEqual(len(self.oitems),3)

   def test_calculateSubTotal(self):
        subtotal=self.o.calculateSubTotal()
        self.assertEqual(str(subtotal), '23.0')


class PaymentTest(unittest.TestCase):
    def setUp(self):
        self.payment = Payment(34.5032, 'credit card')
        
    def test_getType(self):
        self.assertEqual(str(self.payment.type), 'credit card')

    def test_paymentamount(self):
        self.assertEqual(round(self.payment.amount,2), 34.50) 