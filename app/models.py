__author__ = 'Sudo Pnet'
import time
from werkzeug.security import check_password_hash, generate_password_hash
from . import login_manager


class User(object):
    """ creates an instance of a user object """

    def __init__(self, first_name, user_name, email, other_names=None):
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
        hashed_pass = None

    @property
    def password(self, password):
        """ raises an attribute error for the format: User.password"""
        pass

    @password.setter
    def set_password(self, password):
        """uses werkzeug hashing functions to hash the password """
        self.hashed_pass = generate_password_hash(password)

    def check_password(self, password):
        """ returns True if fed in password, has the same hash as the users password else False"""
        return check_password_hash(self.hashed_pass, password=password)


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
        """ this function retrieves the username(from session) of the currently logged in user"""
        pass


class Item(object):
    """ creates instance of items to be added to the item list in the shopping list object"""

    def __init__(self, name, quantity, price, description=None):
        name = name
        quantity = quantity
        price = price
        author = self.get_author()
        date_added = time.time()
        date_last_modified = time.time()
        description = description

    def get_author(self):
        """ returns the username of the person logged in when the item was added"""
        pass


class Gears(object):
    """ more of a toolbox : contains methods that will assist in the data persistent tasks"""

    user_list = []  # holds the user objects

    def __init__(self):
        pass

    @login_manager.user_loader
    def load_user(email):
        """Return the User object with the given email or else None"""
        pass

    def get_user_by_email(self, email):
        """ gos through the users list and returns the user object with the given email"""
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

    shopping_lists = []
    lists_name_set = {}

    def __init(self):
        pass

    def create_list(self, name):
        """ input: a shopping-list name
        calls the shopping list constructor
        output: updated shopping_list else false"""
        if isinstance(name, str) or type(name) == int:
            list_obj = ShoppingList(name)
        else:
            raise ValueError('A list name can only contain alpha numeric characters')
        # we cant force a format style on users, but yet they should not be able to add lists with the same name
        name = name.strip()
        if self.name_checker(name):
            self.shopping_lists.append(list_obj)
            self.lists_name_set.add(list_obj.name.capitalize())
        else:
            raise ValueError('the name is already in use')
        return self.shopping_lists

    def name_checker(self, name):
        """input: list_name
        returns true if the name is not already used for another list else False"""
        return name.capitalize() not in self.lists_name_set

    def modify_list(self, name, **kwargs):
        """input: name of list and the arguments to be changed
        output: returns new list"""
        pass

    def delete_list(self, name):
        """ input: name of list: retrieves list object with the fed in name and pop it
        from the system then return updated shopping_lists"""
        list_obj = self.get_list_by_name(name)
        self.shopping_lists.pop(self.shopping_lists.index(list_obj))
        return self.shopping_lists

    def get_list_by_name(self, name):
        """input: a list's name; returns the list object with the given name"""
        if self.name_checker(name):
            # return list_object ->  conundrum due to arbitrary use of different cases when a user feels like it
            # we will check a capitalized copy of the name against capitalized versions of the lists names
            for list_obj in self.shopping_lists:
                if name.capitalize() == list_obj.name.capitalize():
                    return list_obj
        else:
            raise ValueError('Shopping list with the name {} cannot be found'. format(name))

    def view_list(self, sort='date_added'):
        """ returns all the list sorted as per certain list attributes
        """
        pass

    def add_item(self, item_name, quantity, price, list_name, description=None):
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