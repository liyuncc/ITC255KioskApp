import unittest
from item import Item
from orderitem import OrderItem
from order import Order
from payment import Payment

class ItemTest(unittest, testCase):
    def setUp(self):
        self.item = Item(1, 'item1', 30.00)
    def test_string(self):
        self.assertEqual(str())


class OrderItemTest(unittest.TestCase):
    def setUp(self):
        self.item = Item(1, 'item1', 30.00)
        self.oitem = OrderItem(self.item, 2)

    def test_Quantity(self):
        self.assertEqual(self.oitem.getQuantity(), 2)

    def test_item(self):
        item = self.oitem.getItem()
        self.assertEqual(str(item, 'item1')

class OrderTest(unittest, testCase):
    def setUp(self):
        self.item1 = Item(1, 'beer', 6.25)
        self.item2 = Item(2, 'chips', 4.25)

        self.orderitem1 = OrderItem(item1, 2)
        self.orderitem2 = OrderItem(item2, 5)

        self.order = Order??