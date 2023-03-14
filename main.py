#!/usr/bin/env python3
"""
Backend test assignment
"""

__author__ = "Henrik Holmström"
__version__ = "0.1.0"
__license__ = "MIT"

from core.classes.Product import Product
from core.enums.Weekday import Weekday
from core.enums.ProductType import ProductType
from core import get_delivery_dates

def main():
    """ Main entry point of the app """
    products = [
        Product(1, "Artichoke", [Weekday.WEDNESDAY, Weekday.THURSDAY], ProductType.EXTERNAL, 5),
        Product(2, "Mustard Greens", [Weekday.MONDAY, Weekday.FRIDAY], ProductType.NORMAL, 2),
        Product(3, "Gourds", [Weekday.THURSDAY, Weekday.WEDNESDAY], ProductType.TEMPORARY, 4),
        Product(4, "Romaine Lettuce", [Weekday.TUESDAY, Weekday.WEDNESDAY], ProductType.NORMAL, 2),
        Product(5, "Snow Peas", [Weekday.WEDNESDAY, Weekday.FRIDAY], ProductType.TEMPORARY, 3)
        ]
    
    delivery_dates = get_delivery_dates(17074, products)
    
    for x in delivery_dates: 
        print(x.__dict__)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
