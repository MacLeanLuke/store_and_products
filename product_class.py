
# Create a Product class with 3 attributes
class Products():

    # Create a Product class with 3 attributes
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    # Add the update_price method to the Product class
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price = self.price * (1 + percent_change)
        else:
            self.price = self.price * (1 - percent_change)

    # Add the print_info method to the Product class
    def print_info(self):
        print(f"Product: {self.name} - Category: {self.category} - Price: {self.price}")