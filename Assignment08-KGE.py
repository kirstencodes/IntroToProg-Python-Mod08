# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# KElghoroury,3.9.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

import pickle

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product(object):
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        KElghoroury,3.7.2021,Modified code to complete assignment 8
    """
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    def __str__(self):
        description = self.product_name + "   $" + self.product_price
        return description
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        KElghoroury,3.7.2021,Modified code to complete assignment 8
    """
    def save_data_to_file(file_name, list_of_product_objects):
        file = open(file_name, "wb")
        pickle.dump(list_of_product_objects, file)
        file.close()

    def read_data_from_file(file_name):
        file = open(file_name, "rb")
        list_of_product_objects = []
        try:
            list_of_product_objects = pickle.load(file)
        except EOFError:
            print("Empty list.")
        file.close()
        return list_of_product_objects
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Performs Input and Output tasks:

    methods:
        show_menu()
        input_menu_choice(strFileName, list_of_product_objects):
        print_current_products_in_list(list_of_product_objects):
        input_new_product_and_price(list_of_product_objects):
        save_and_exit(strFileName, list_of_product_objects):

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        KElghoroury,3.9.2021,Modified code to complete assignment 8
    """
    @staticmethod
    def show_menu():
        """ Displays menu of options

        """
        print("Hello, there!  Please choose from the following menu: " + "\n")
        print("(1) Show current products and prices." + "\n")
        print("(2) Add a product to the list." + "\n")
        print("(3) Save to file and exit." + "\n")

    @staticmethod
    def input_menu_choice(strFileName, list_of_product_objects):
        """ Gets the menu choice from a user

        :return: string
        """
        while(True):
            choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
            print()  # Add an extra line for looks
            #return choice
            if choice == '1':
                IO.print_current_products_in_list(list_of_product_objects)
            elif choice == '2':
                IO.input_new_product_and_price(list_of_product_objects)
            elif choice == '3':
                IO.save_and_exit(strFileName, list_of_product_objects)
            else:
                print("Please choose 1, 2, or 3.")

    @staticmethod
    def print_current_products_in_list(list_of_product_objects):
        """ Shows the current products in the list of products

        :param list_of_product_objects: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current products and prices are: *******")
        for row in list_of_product_objects:
            print(row)
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_product_and_price(list_of_product_objects):
        add_product = input("What product would you like to add: ")
        add_price = input("What is the price of this product: ")
        new_product = Product(add_product, add_price)
        list_of_product_objects.append(new_product)
        return(list_of_product_objects)

    @staticmethod
    def save_and_exit(strFileName, list_of_product_objects):
        FileProcessor.save_data_to_file(strFileName, list_of_product_objects)
        exit()
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
IO.print_current_products_in_list(lstOfProductObjects)

IO.show_menu()
IO.input_menu_choice(strFileName, lstOfProductObjects)
# Main Body of Script  ---------------------------------------------------- #

