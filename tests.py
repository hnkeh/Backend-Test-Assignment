import unittest
from core.classes.Product import Product
from core.enums.Weekday import Weekday
from core.enums.ProductType import ProductType
from core import get_delivery_dates

class TestStringMethods(unittest.TestCase):
    test_postal_code = 12345

    def test_should_raise_exception(self):
        exception = "Product with id: 1 has no type."
        products = [Product(1, "Artichoke", [Weekday.WEDNESDAY, Weekday.THURSDAY], "FAULTY TYPE", 5)]

        with self.assertRaises(Exception) as e:
            get_delivery_dates(self.test_postal_code, products)
        
        self.assertEqual(str(e.exception), exception)

    def test_should_get_is_green(self):
        products = [Product(1, "Artichoke", [Weekday.WEDNESDAY], ProductType.NORMAL, 5)]
        delivery_dates = get_delivery_dates(self.test_postal_code, products)
        self.assertTrue(delivery_dates[0].is_green_delivery)

    def test_should_not_get_is_green(self):
        products = [Product(1, "Artichoke", [Weekday.THURSDAY], ProductType.NORMAL, 5)]
        delivery_dates = get_delivery_dates(self.test_postal_code, products)
        self.assertFalse(delivery_dates[0].is_green_delivery)

if __name__ == '__main__':
    unittest.main()