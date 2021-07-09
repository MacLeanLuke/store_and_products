from product_class import Products

# Create a Store class with 2 attributes
class Store():

    # Create a Store class with 2 attributes
    def __init__(self, name):
        self.name = name
        self.list_of_products = []

    # Add the add_product method to the Store class
    def add_product(self, new_product):
        self.list_of_products.append(new_product)

    # Add the sell_product method to the Store class
    def sell_product(self, id):
        self.list_of_products.pop(id)

    def inflation(self, percent_increase):
        for x in range(0, len(self.list_of_products)):
            self.list_of_products[x].update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for x in range(0, len(self.list_of_products)):
            if self.list_of_products[x].category == category:
                self.list_of_products[x].update_price(percent_discount, False)