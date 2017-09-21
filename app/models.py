__author__ = 'Sudo Pnet'
import time
from werkzeug.security import check_password_hash, generate_password_hash
from . import login_manager


class User(object):
    """ creates an instance of a user object """

    def __init__(self, full_name, user_name, email):
        if isinstance(full_name, str):
            self.name = full_name

        if not isinstance(full_name, str):
            raise ValueError("A person's names can only be strings")
        if not str.isalnum(user_name):
            raise ValueError('The User name can only contain alpha-numeric characters')

        self.user_name = user_name
        self.email = email
        self.hashed_pass = None

    @property
    def password(self):
        """ raises an attribute error for the format: User.password"""
        raise AttributeError('Password has no read permissions')

    @password.setter
    def password(self, pass_word):
        """uses werkzeug hashing functions to hash the password """
        # self.hashed_pass = generate_password_hash(pass_word)
        pass

    def set_password(self, pass_word):
        """"""
        self.hashed_pass = pass_word

    def check_password(self, pass_word):
        """ returns True if fed in password, has the same hash as the users password else False"""
        return self.hashed_pass == pass_word
        # change implementation to werkzeug after installing db


class ShoppingList(object):
    """ Creates an instance of a list"""

    def __init__(self, name):
        if isinstance(name, str) or type(name) == int:
            self.name = name
        else:
            raise ValueError('The shopping list name can only be a string or integer')

        self.author = self.get_author()
        self.date_created = time.time()
        self.date_last_modified = time.time()
        self.items = []

    def get_author(self):
        """ this function retrieves the username(from session) of the currently logged in user"""
        pass


class Item(object):
    """ creates instance of items to be added to the item list in the shopping list object"""

    def __init__(self, name, quantity, price, description=None):
        if not isinstance(name, str):
            raise ValueError()
        if isinstance(quantity, str):
            pass
        else:
            raise ValueError
        if description is not None:
            if type(description) != str:
                raise ValueError
        if isinstance(price, int) or isinstance(price, float):
            price = float(price)
        else:
            raise ValueError
        self.name = name
        self.quantity = quantity
        self.price = price
        self.author = self.get_author()
        self.date_added = time.time()
        self.date_last_modified = time.time()
        self.description = description

    def get_author(self):
        """ returns the username of the person logged in when the item was added"""
        return True


class Gears(object):
    """ more of a toolbox : contains methods that will assist in the data persistent tasks"""

    user_list = []  # holds the user objects

    def __init__(self):
        pass

    @login_manager.user_loader
    def load_user(self, email):
        """Return the User object with the given email or else None"""
        return self.get_user_by_email(email)

    def get_user_by_email(self, email):
        """ gos through the users list and returns the user object with the given email"""
        for user in self.user_list:
            if user.email == email:
                return user
        return None

    def add_user(self, email, password, name, user_name):
        """ input: data to be stored: email, hashed password
        output returns True upon successful termination
        """
        # create a user, make sure to check username and email collision
        self.validate_email(email)
        self.validate_user_name(user_name)
        user = User(name, user_name, email)
        user.set_password(password=password)
        self.user_list.append(user)

    def validate_email(self, email):
        """ raises exception if email is already registered"""
        for user in self.user_list:
            if email == user.email:
                raise Exception('email already registered')
        return True

    def validate_user_name(self, user_name):
        """raises exception if user_name is already registered"""
        for user in self.user_list:
            if user_name == user.user_name:
                raise Exception('user_name already registered')
        return True

    def reset_password(self, email):
        """ serve users who are blocked out due to forgotten passwords with links
        from which they can reset their passwords
        input: email
        output: returns link to be emailed to fed in email."""
        pass


class Basket(object):
    """ toolbox with the tools for manipulating the shopping lists and the items on it"""

    def __init__(self):
        self.shopping_lists = []
        self.lists_name_set = set()

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
        returns true if the name is not already being used for another list else False"""
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
        if not self.name_checker(name):
            # return list_object ->  conundrum due to arbitrary use of different cases when a user feels like it
            # we will check a capitalized copy of the name against capitalized versions of the lists names
            for list_obj in self.shopping_lists:
                if name.capitalize() == list_obj.name.capitalize():
                    return list_obj
        else:
            raise ValueError('Shopping list with the name {} cannot be found'. format(name))

    def view_list(self, sort='date_created'):
        """ returns all the list sorted as per 3 list attributes: name, date created, date modified
        """
        # extract the attributes to a temp_list sort them then loop through shopping list
        # while arranging them
        temp_ = []
        temp_lists = []
        if sort == 'date_created':
            for list_ in self.shopping_lists:
                temp_.append(list_.date_created)
            temp_.sort()
            for attr in temp_:
                for list_ in self.shopping_lists:
                    if attr == list_.date_created:
                        temp_lists.append(list_)
            return temp_lists

        if sort == 'name':
            for list_ in self.shopping_lists:
                temp_.append(list_.name)
            temp_.sort()
            for attr in temp_:
                for list_ in self.shopping_lists:
                    if attr == list_.name:
                        temp_lists.append(list_)
            return temp_lists

        if sort == 'date_last_modified':
            for list_ in self.shopping_lists:
                temp_.append(list_.date_last_modified)
            temp_.sort()
            for attr in temp_:
                for list_ in self.shopping_lists:
                    if attr == list_.date_last_modified:
                        temp_lists.append(list_)
            return temp_lists
        return False

    def add_item(self,  list_name, item_name, quantity, price, description=None):
        """input: list_name, item name after which it calls the Item constructor, with appropriate details
        and then adds the created item object to a list object with the fed in list_name
        output: the updated list"""
        if not str.isalpha(item_name) and not str.isalnum(quantity):
            raise ValueError('item_name or quantity, wrong input types')
        if description is not None and isinstance(description, str):
            pass
        else:
            raise ValueError('Description, wrong input type')
        if isinstance(price, int) or isinstance(price, float):
            price = float(price)
        else:
            raise ValueError('Price, wrong input type')
        list_ = self.get_list_by_name(list_name)
        # need to make sure no other item with same name in list
        item_name_set = set()
        for item in list_.items:
            item_name_set.add(item.name)
        if item_name in item_name_set:
            raise ValueError('Item with name {} already exists'. format(item_name))

        item_obj = Item(item_name, quantity, price, description)
        list_.items.append(item_obj)

        return list

    def modify_item(self, item_name, list_name):
        """ input: specified parameters
        output: the updated list object"""
        pass

    def delete_item(self, item_name, list_name):
        """retrieves the list, retrieves the item from the list and then pops the item
        output: the updated list object"""
        # check if list exists
        # check if item exists the pop the item from the list
        list_ = self.get_list_by_name(list_name)
        item_obj = None
        for item in list_.items:
            if item.name == item_name:
                item_obj = item
        list_.items.pop(list.index(item_obj))

        return list

    def view_item(self, list_name, sort):
        """ retrieves returns the list items of the specified list while sorted """
        pass