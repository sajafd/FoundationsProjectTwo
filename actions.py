# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart
from components import Store
from components import Product

site_name = "comprehensive_commerce.com"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    print ()
    for store in stores: 
        print ("- " + store.name)
    print()

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for store in stores:
        if store.name == store_name:
            # print ("found store name in stores")
            # print(store.products)
            return store
    print ("could not find store name")
    return False

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print_stores()
    picked_store = input("Pick a store by typing its name. Or type 'checkout' to pay your bills and say your goodbyes. \n \n")
    while not(picked_store.lower() == "checkout") and get_store(picked_store)==False:
        print ("No store with that name. Please try again." )    
        picked_store = input("Pick a store by typing its name. Or type 'checkout' to pay your bills and say your goodbyes. \n \n")  
    # if picked_store in store_names:
    #     print ("You picked a correct store, now pick your products")  
    if picked_store.lower() == "checkout":
        return "checkout"
    return get_store(picked_store)

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    picked_store.print_products()

    picked_product = input("Pick the itmes you\'d like to add in your cart by typing the product name exactly as it was spelled above. .\nType 'back' to go back to them main menu where you can checkout. \n \n")
    while (picked_product.lower() != "back"):
        # print ("in the first while loop - i.e. picked_product is not in picked_store.products")
        for product in picked_store.products:
            if product.name == picked_product:
                cart.add_to_cart(product)
        picked_product = input("Pick the itmes you\'d like to add in your cart by typing the product name exactly as it was spelled above. .\nType 'back' to go back to them main menu where you can checkout. \n \n")


def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    picked_store = pick_store()
    while picked_store != "checkout":
        pick_products(cart, picked_store)
        picked_store = pick_store()

    print(cart.products)
    cart.checkout()
        


def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
