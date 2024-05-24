class Order:
    def __init__(self, table_number, order_type):
        self.table_number = table_number
        self.order_type = order_type
        self.status = 'Pending'
        self.items = []
        self.price = 0

    def add_item(self, item):
        self.items.append(item)
        self.calculate_total()

    def calculate_total(self):
        self.price = sum(item.price for item in self.items)

    def get_total(self):
        return self.price