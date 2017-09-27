from werkzeug.security import check_password_hash, generate_password_hash
from . import login_manager
from flask_login import UserMixin
import re
from _datetime import datetime


class User(UserMixin, object):
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

    def get_id(self):
        """return the unicode identifier"""
        return self.user_name

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

    def __init__(self, name, author=None):
        if isinstance(name, str) or type(name) == int:
            self.name = name
        else:
            raise ValueError('The shopping list name can only be a string or integer')

        self.author = author
        self.date_created = datetime.utcnow()
        self.date_last_modified = datetime.utcnow()
        self.items = []
        self.total = 0


class Item(object):
    """ creates instance of items to be added to the item list in the shopping list object"""

    def __init__(self, name, quantity, price, description=None, author=None):
        if not isinstance(name, str):
            raise ValueError()
        if not isinstance(quantity, str):
            raise ValueError(" The quantity value should be a string")
        else:
            pattern = r'\d+'
            numbers_list = re.findall(pattern, quantity)
            if len(numbers_list):
                number = numbers_list[0]
            else:
                raise ValueError("The quantity amount is not quantifiable")
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
        self.author = author
        self.date_added = datetime.utcnow()
        self.date_last_modified = datetime.utcnow()
        self.description = description
        self.amount = 0


@login_manager.user_loader
def load_user(user_name):
    """Return the User object with the given email or else None"""
    gear1 = Gears()
    return gear1.get_user_by_username(user_name)


class Gears(object):
    """ more of a toolbox : contains methods that will assist in the data persistent tasks"""

    user_list = []  # holds the user objects

    def __init__(self):
        pass

    def get_user_by_email(self, email):
        """ gos through the users list and returns the user object with the given email"""
        for user in self.user_list:
            if user.email == email:
                return user
        return None

    def get_user_by_username(self, user_name):
        """loops through users and returns the user with the given username"""
        for user in self.user_list:
            if user.user_name == user_name:
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
        user.set_password(password)
        self.user_list.append(user)
        return True

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

    def create_list(self, name, author=None):
        """ input: a shopping-list name
        calls the shopping list constructor
        output: updated shopping_list else false"""
        if isinstance(name, str) or type(name) == int:
            list_obj = ShoppingList(name, author=author)
        else:
            raise ValueError('A list name can only contain alpha numeric characters')
        # we cant force a format style on users, but yet they should not be able to add lists with the same name
        name = name.strip()
        if self.name_checker(name):
            self.shopping_lists.append(list_obj)
            self.get_lists_name_set()
        else:
            raise ValueError('the name {} is already in use'.format(name))
        return self.shopping_lists

    def get_lists_name_set(self):
        """ Returns a set that contains the names in the current shoppingLists lists"""
        set_ = set()
        for list in self.shopping_lists:
            set_.add(list.name)
        return set_

    def name_checker(self, name):
        """input: list_name
        returns true if the name is not already being used for another list else False"""
        names_set = self.get_lists_name_set()
        for name_ in names_set:
            if name_.capitalize() == name.capitalize():
                return False
        return True

    def modify_list(self, name, new_name=None):
        """input: name of list and the arguments to be changed
        output: returns new list"""
        # we can only modify the name of a list, for other attributes see modify_items()
        list_ = self.get_list_by_name(name)
        if new_name and self.name_checker(new_name):
            list_.name = new_name
            list_.date_last_modified = datetime.utcnow()
        else:
            raise ValueError("Seems like you already have a list with that name")
        return True

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

    def view_list(self, sort='date_created', author=None):
        """ returns all the list sorted as per 3 list attributes: name, date created, date modified
        """
        # extract the attributes to a temp_list sort them then loop through shopping list
        # while arranging them

        filter_list = []
        if author is not None:
            for list_ in self.shopping_lists:
                self.set_total(list_)
                if list_.author == author:
                    filter_list.append(list_)
        else:
            filter_list = self.shopping_lists
        temp_ = []
        temp_lists = []
        if sort == 'date_created':
            for list_ in filter_list:
                temp_.append(list_.date_created)
            temp_.sort()
            for attr in temp_:
                for list_ in filter_list:
                    if attr == list_.date_created:
                        temp_lists.append(list_)
            return temp_lists

        if sort == 'name':
            for list_ in filter_list:
                temp_.append(list_.name)
            temp_.sort()
            for attr in temp_:
                for list_ in filter_list:
                    if attr == list_.name:
                        temp_lists.append(list_)
            return temp_lists

        if sort == 'date_last_modified':
            for list_ in filter_list:
                temp_.append(list_.date_last_modified)
            temp_.sort()
            for attr in temp_:
                for list_ in filter_list:
                    if attr == list_.date_last_modified:
                        temp_lists.append(list_)
            return temp_lists
        raise Exception('Unkown sort configuration')


    def add_item(self,  list_name, item_name, quantity, price, description=None, author=None):
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

        item_obj = Item(item_name, quantity, price=price, description=description, author=author)
        list_.items.append(item_obj)

        list_.total = self.set_total(list_).total

        list_.date_last_modified = datetime.utcnow()

        return list_

    def extract_number_from_quantity(self, quantity):
        """ takes in a string and returns the number in the string"""
        pattern = r'\d+'
        numbers_list = re.findall(pattern, quantity)
        number = numbers_list[0]
        return float(number)

    def modify_item(self, item_name, list_name, name=None, price=None, description=None, quantity=None):
        """ input: specified parameters
        output: the updated list object"""
        # we can only modify name, price, description, quantity
        item = self.get_item_by_name(item_name=item_name, list_name=list_name)
        if item:
            # also check that the items name is not already with another item
            if name and self.item_name_checker(item_name=name, list_name=list_name):
                item.name = name
            if price:
                item.price = price
            if description:
                item.description = description
            if quantity:
                item.quantity = quantity
            item.date_last_modified = datetime.utcnow()
            list_ = self.get_list_by_name(list_name)
            list_.date_last_modified = datetime.utcnow()
            list_.total = self.set_total(list_).total
        else:
            raise Exception('Item {} was not found in the {} list'.format(item_name, list_name))

    def item_name_checker(self, item_name, list_name):
        """ Checks if the item_name is already a name of an item in the given list
        input: item_name, and list_name
        output: returns True if item_name is not in lits_name.items.names"""
        list_ = self.get_list_by_name(list_name)
        for item in list_.items:
            if item.name == item_name:
                return False
        return True

    def get_item_by_name(self, item_name, list_name):
        """" input: a list name and an item name
        output: the item whose name is specified -> and that belongs to the list with the name that has been parsed"""
        list_ = self.get_list_by_name(list_name)
        for item in list_.items:
            if item.name == item_name:
                return item
        return False

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
        list_.items.pop(list_.items.index(item_obj))
        list_.date_last_modified = datetime.utcnow()
        list_.total = self.set_total(list_).total

        return list_

    def view_item(self, list_name, sort='date_added'):
        """ retrieves returns the list items of the specified list while sorted """
        # get lis; get items list from the list; sort the items return list
        # items can only be sorted by their name, date_added, date modified, quantity and price
        shl_list = self.get_list_by_name(list_name)
        item_list = shl_list.items

        list_ = []
        temp_list = []
        if sort == 'name':
            for item in item_list:
                temp_list.append(item.name)
            temp_list.sort()
            for name in temp_list:
                for item in item_list:
                    if item.name == name:
                        list_.append(item)
            shl_list.items = list_
            return shl_list
        if sort == 'date_added':
            for item in item_list:
                temp_list.append(item.date_added)
            temp_list.sort()
            for date_added in temp_list:
                for item in item_list:
                    if item.date_added == date_added:
                        list_.append(item)
            shl_list.items = list_
            return shl_list
        if sort == 'date_last_modified':
            for item in item_list:
                temp_list.append(item.date_last_modified)
            temp_list.sort()
            for date_last_modified in temp_list:
                for item in item_list:
                    if item.date_last_modified == date_last_modified:
                        list_.append(item)
            shl_list.items = list_
            return shl_list
        if sort == 'quantity':
            for item in item_list:
                temp_list.append(item.quantity)
            temp_list.sort()
            for quantity in temp_list:
                for item in item_list:
                    if item.quantity == quantity:
                        list_.append(item)
            shl_list.items = list_
            return shl_list
        if sort == 'price':
            for item in item_list:
                temp_list.append(item.price)
            temp_list.sort()
            for price in temp_list:
                for item in item_list:
                    if item.price == price:
                        list_.append(item)
            shl_list.items = list_
            return shl_list
        raise Exception('Unknown sort configuration')

    def set_total(self, list_):
        """
        input: a list
        action: goes through each item and sets the item.amount and updates the list.total
        called for modify_item, delete_item, add_item, view_item
        return the list
        """
        items = list_.items
        list_total = 0
        for item in items:
            item_total = self.extract_number_from_quantity(item.quantity) * item.price
            item.amount = item_total
            list_total += item_total
        list_.total = list_total
        return list_
