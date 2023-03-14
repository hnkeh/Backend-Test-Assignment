class Product:
    def __init__(self, id, name, delivery_days, type, days_in_advance):
        self.id = id
        self.name = name
        # A list of weekdays when the product can be delivered.
        self.delivery_days = delivery_days
        # Normal, external or temporary.
        self.type = type
        # How many days before delivery the products need to be ordered.
        self.days_in_advance = days_in_advance