__author__ = 'Sudo Pnet'
import time
from werkzeug.security import check_password_hash, generate_password_hash


class User(object):
    """ creates an instance of a user object """

    user_list = []  # holds the user objects

    def __init__(self, first_name, other_names, user_name, email, password):
        if isinstance(first_name, str):
            f_name = first_name
        else:
            raise ValueError('The first name can only be a string')
        if not isinstance(other_names, str):
            raise ValueError("A person's names can only be strings")
        if not str.isalnum(user_name):
            raise ValueError('The User name can only contain alpha-numeric characters')

        o_name = other_names
        user_name = user_name
        email = email
        password = password

    def add_to_list(self, user_object):
        """ adds a created user object to the user_list"""


class ShoppingList(object):
    """ Creates an instance of a list"""

    def __init__(self, name):
        if isinstance(name, str) or type(name) == int:
            name = name
        else:
            raise ValueError('The shopping list name can only be a string or integer')

        author = self.get_author()
        date_created = time.time()
        date_last_modified = time.time()
        items = []

    def get_author(self):
        """ this function retrieves the username of the currently logged in user"""
        pass


class Item(object):
    """ creates instance of items to be added to the item list in the shopping list object"""

    def __init__(self, name, quantity, price, description=None ):
        name = name
        quantity = quantity
        price = price
        author = self.get_author()
        time_added = time.time()
        description = description

    def get_author(self):
        """ returns the username of the person logged in when the item was added"""
        pass


class Gears(object):
    """ more of a toolbox : contains methods that will assist in the data persistent tasks"""

    def __init__(self):
        pass

    def log_in(self, email, password):
        """ input: data to be stored: email, hashed password
        output returns True upon successful termination
        """
        pass

    def register(self, user_object):
        """ input: data to be stored: email, hashed password, username and user names
        output returns True upon successful termination
        """

    def log_out(self):
        """Pops out the currently logged in user's credentials from session"""
        pass

    def reset_password(self, email):
        """ serve users who are blocked out due to forgotten passwords with links
        from which they can reset their passwords
        input: email
        output: returns link to be emailed to fed in email."""
        pass


class Basket(object):
    """ toolbox with the tools for manipulating the shopping lists and the items on it"""

    shopping_list = []

    def __init(self):
        pass

    def create_list(self, name):
        """ input: a shopping-list name
        calls the shopping list constructor
        output: Boolean"""
        list_obj = ShoppingList(name)
        self.shopping_list.append(list_obj)
        return True

    def modify_list(self, name, **kwargs):
        """input: name of list and the arguments to be changed
        output: returns new list"""
        pass

    def delete_list(self, name):
        """ input: name of list: retrieves list object with the fed in name and pop it
        from the system then return Boolean"""
        pass

    def view_list(self, sort):
        """ returns all the list sorted as per certain list attributes
        """
        pass

    def add_item(self, item_name, list_name):
        """input: list_name, item name after which it calls the Item constructor, with appropriate details
        and then adds the created item object to a list object with the fed in list_name
        output: the updated list"""

    def modify_item(self, item_name, list_name):
        """ input: specified parameters
        output: the updated list object"""
        pass

    def delete_item(self, item_name, list_name):
        """retrieves the list, retrieves the item from the list and then pops the item
        output: the updated list object"""

    def view_item(self, list_name, sort):
        """ retrieves returns the list items of the specified list while sorted """
        pass