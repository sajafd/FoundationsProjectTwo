# CLASSES AND METHODS
class Store(object):
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        # your code goes here!
        self.name = name
        self.products = []


    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!
        self.products.append(product)

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        for product in self.products:
            print (product)


class Product(object):
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here!
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        # your code goes here!
        return "\n\tProduct Name: %s \n\tDescription: %s \n\tPrice: %s \n" % (self.name, self.description, self.price)


class Cart(object):
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!
        self.products = []


    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!
        self.products.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        print("in get_total_price in the cart class now")
        # print (self.products)
        total_cost = 0
        for product in self.products:
            print ('in for loop in get_total_price method in cart class now')
            product_cost = product.price
            total_cost += product_cost
            print ("total cost in get_total_price calculated to: %s" % str(total_cost))
        return total_cost

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        for product in self.products:
            print ("\tProduct Name: %s \n Description: %s \n Price: %s \n" % (product.name, product.description, product.price))
        total_price = self.get_total_price()
        price_to_string = str(total_price)
        print ("Your total price is: %s KD" % price_to_string)


    def checkout(self):
        """
        Does the checkout.
        """
        # your code goes here!
        self.print_receipt()
        confirmation = input("Confirm? (yes/no)")
        if confirmation == 'yes':
            print ("Your order has been placed")
        elif confirmation == "no":
            print ("Your order has been cancelled")

