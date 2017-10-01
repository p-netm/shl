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


    def set_password(self, pass_word):
        """ assigns a password to the user"""
        self.hashed_pass = pass_word

    def check_password(self, pass_word, hashed_pass):
        """ returns True if fed in password, has the same pass as the users password else False"""
        return hashed_pass == pass_word


class ShoppingList(object):
    """ Creates an instance of a list"""

    def __init__(self, name, author, token, public=False):
        if isinstance(name, str) or type(name) == int:
            self.name = name
        else:
            raise ValueError('The shopping list name can only be a string or integer')

        self.author = author
        self.date_created = datetime.utcnow()
        self.date_last_modified = datetime.utcnow()
        self.items = []
        self.total = 0
        self.public = public
        self.token = token


class Item(object):
    """ creates instance of items to be added to the item list in the shopping list object"""

    def __init__(self, name, quantity, price, description=None, author=None, public=False):
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
        self.public = public


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

    def if_user_exists(self, link_name):
        """Checks if there is a registered user using the username given in the link_name
        it will return True if Found and else False"""
        for user in self.user_list:
            if user.user_name == link_name:
                # means that the object belongs to the logged in user
                return True
        return False
                

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
        self.gears = Gears()

    def create_list(self, name, author, token, public=False):
        """ input: a shopping-list name
        calls the shopping list constructor
        output: updated shopping_list else false"""
        if isinstance(name, str) or type(name) == int:
            list_obj = ShoppingList(name, author=author, token=token, public=public)
        else:
            raise ValueError('A list name can only contain alpha numeric characters')
        # we cant force a format style on users, but yet they should not be able to add lists with the same name
        name = name.strip()
        if self.name_checker(author, name):
            self.shopping_lists.append(list_obj)
            self.get_lists_name_set(author)
        else:
            raise ValueError('the name {} is already in use'.format(name))
        return self.shopping_lists

    def check_permission(self, object_, link_name):
        """Input: an object with an author field
        a link name containing the name in the url.
        output: return TRue if user with link_name has modification permission"""
        if object_.author != link_name:
            return False
        return True

    def get_lists_name_set(self, link_name):
        """ Returns a set that contains the names in the current shoppingLists lists"""
        set_ = set()
        for list in self.shopping_lists:
            if list.author == link_name:
                set_.add(list.name)
        return set_

    def name_checker(self, link_name, name):
        """input: list_name
        returns true if the name is not already being used for another list else False"""
        names_set = self.get_lists_name_set(link_name)
        for name_ in names_set:
            if name_.capitalize() == name.capitalize():
                return False
        return True

    def modify_list(self, name, link_name, new_name=None, public=None):
        """input: name of list and the arguments to be changed
        output: returns new list"""
        # we can only modify the name of a list, for other attributes see modify_items()
        list_ = self.get_list_by_name(name, link_name)
        if new_name and self.name_checker(link_name, new_name):
            list_.name = new_name
            list_.date_last_modified = datetime.utcnow()
        elif public is not None:
            list_.public = public
            list_.date_last_modified = datetime.utcnow()
        else:
            raise ValueError("Seems like you already have a list with that name")


        return True

    def delete_list(self, link_name, name):
        """ input: name of list: retrieves list object with the fed in name and pop it
        from the system then return updated shopping_lists"""
        list_obj = self.get_list_by_name(name, link_name)
        self.shopping_lists.pop(self.shopping_lists.index(list_obj))
        return self.shopping_lists

    def get_list_by_name(self, name, link_name):
        """input: a list's name; returns the list object with the given name"""
        if not self.name_checker(link_name, name):
            # return list_object ->  conundrum due to arbitrary use of different cases when a user feels like it
            # we will check a capitalized copy of the name against capitalized versions of the lists names
            for list_obj in self.shopping_lists:
                if name.capitalize() == list_obj.name.capitalize() and list_obj.author == link_name:
                    return list_obj
        else:
            raise ValueError('Shopping list with the name {} cannot be found'. format(name))

    def view_list(self, link_name, sort='date_created'):
        """ returns all the list sorted as per 3 list attributes: name, date created, date modified
        """
        # check that the user exists:
        if not self.gears.if_user_exists(link_name):
            raise Exception('No account with the user_name {}'.format(link_name))

        # extract the attributes to a temp_list sort them then loop through shopping list
        # while arranging them

        # if a person is logged he should view all his lists irrespective of the public attribute value
        filter_list = []
        if link_name is not None:
            for list_ in self.shopping_lists:
                self.set_total(list_)
                # we check that the author of the list is the guy in the link_name
                if list_.author == link_name:
                    filter_list.append(list_)
                # if the guys are different then only pick lists that have been made public
                elif list_.public:
                    filter_list.append(list_)
                    # we check that for a logged in user who is not the owner, if we cannot find any lists then we raise

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

    def add_item(self,  link_name, list_name, item_name, quantity, price, description=None, author=None):
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
        list_ = self.get_list_by_name(list_name, link_name)
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

    def modify_item(self, link_name, item_name, list_name, name=None, price=None, description=None, quantity=None):
        """ input: specified parameters
        output: the updated list object"""
        # we can only modify name, price, description, quantity
        item = self.get_item_by_name(link_name=link_name, item_name=item_name, list_name=list_name)
        if item:
            # also check that the items name is not already with another item
            if name and self.item_name_checker(link_name=link_name, item_name=name, list_name=list_name):
                item.name = name
            if price:
                item.price = price
            if description:
                item.description = description
            if quantity:
                item.quantity = quantity
            item.date_last_modified = datetime.utcnow()
            list_ = self.get_list_by_name(list_name, link_name)
            list_.date_last_modified = datetime.utcnow()
            list_.total = self.set_total(list_).total
        else:
            raise Exception('Item {} was not found in the {} list'.format(item_name, list_name))

    def item_name_checker(self, link_name, item_name, list_name):
        """ Checks if the item_name is already a name of an item in the given list
        input: item_name, and list_name
        output: returns True if item_name is not in lits_name.items.names"""
        list_ = self.get_list_by_name(list_name, link_name)
        for item in list_.items:
            if item.name == item_name:
                return False
        return True

    def get_item_by_name(self, link_name, item_name, list_name):
        """" input: a list name and an item name
        output: the item whose name is specified -> and that belongs to the list with the name that has been parsed"""
        list_ = self.get_list_by_name(list_name, link_name)
        for item in list_.items:
            if item.name == item_name:
                return item
        return False

    def delete_item(self, link_name, item_name, list_name):
        """retrieves the list, retrieves the item from the list and then pops the item
        output: the updated list object"""
        # check if list exists
        # check if item exists the pop the item from the list
        list_ = self.get_list_by_name(list_name, link_name=link_name)
        item_obj = None
        for item in list_.items:
            if item.name == item_name:
                item_obj = item
        list_.items.pop(list_.items.index(item_obj))
        list_.date_last_modified = datetime.utcnow()
        list_.total = self.set_total(list_).total

        return list_

    def view_item(self, link_name, list_name, sort='date_added'):
        """ retrieves returns the list items of the specified list while sorted """
        # get lis; get items list from the list; sort the items return list
        # items can only be sorted by their name, date_added, date modified, quantity and price
        shl_list = self.get_list_by_name(list_name, link_name)
        item_list = shl_list.items

        list_ = []
        temp_list = []

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
        return shl_list

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

    def generate_token(self, list_name):
        # means that we are generating a token ******************
        return list_name

    def decodes_token(self, token):
        # we retrieve the list name serialized in the token and return it
        return token
