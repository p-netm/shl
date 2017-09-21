__author__ = 'Sudo Pnet'
import unittest
from app.models import Basket, ShoppingList, User, Item, Gears


class ShoppingListTests(unittest.TestCase):

    def setUp(self):
        """ instantiate common attributes for this class"""
        pass

    def tearDown(self):
        """pretty straightforward, tears down attributes created in setUp()"""
        pass

    def test_shopping_list_auto_properties(self):
        """checks if the automatically set propeties are as they should be"""
        basket = Basket()
        new_list = ShoppingList('Name')
        self.assertTrue(new_list.date_created)
        self.assertTrue(new_list.date_last_modified)
        self.assertFalse(len(new_list.items))
        del basket

    def test_if_shopping_list_constructor_has_error_checking(self):
        """ Test: create list with arguments being the wrong-type"""
        basket = Basket()
        with self.assertRaises(ValueError) as context:
            basket.create_list({})
            self.assertTrue('The shopping list name can only be a string or integer' in context.exception)
        del basket

    def test_shopping_list_creates_and_adds_lists(self):
        """ test to see if the create list preserves a list object after instantiation."""
        basket = Basket()
        initial_value = len(basket.shopping_lists)
        self.assertFalse(initial_value)
        boolean = basket.create_list('First list')
        self.assertTrue(boolean)
        current_value = len(basket.shopping_lists)
        self.assertTrue(current_value)
        self.assertEqual(current_value - initial_value, 1,
                         msg="there should be one user object in the shopping_list")
        del basket

    def test_repeat_shopping_list_name(self):
        """ tests if a user can create two lists with the same name"""
        basket = Basket()
        basket.create_list('My_list')
        with self.assertRaises(ValueError):
            basket.create_list('My_list')
        self.assertTrue(len(basket.shopping_lists) == 1,
                        msg='There should be only one list created')
        del basket

    def test_delete_shopping_list(self):
        """ checks that a deleted list is no longer in the system"""
        basket = Basket()
        basket.create_list('1')
        basket.create_list('2')
        basket.create_list('3')
        new_shopping_lists = basket.delete_list('2')
        current_value = len(basket.shopping_lists)
        self.assertTrue(current_value, 2)
        # create a list of the shopping_lists names and confirm the deleted list's name
        # is not in it
        list_names = []
        for list_obj in basket.shopping_lists:
            list_names.append(list_obj.name)
        self.assertNotIn('2', list_names,
                         msg="How comes the deleted list names still shows up")
        del basket

    def test_view_shopping_list(self):
        """ checks that the view list obeys the sorting order requested"""
        basket = Basket()
        basket.create_list('1')
        basket.create_list('6')
        basket.create_list('2')
        basket.create_list('5')
        basket.create_list('3')

        new_shopping_lists = basket.view_list(sort='name')
        print(len(new_shopping_lists))
        golden_lists = ['1', '2', '3', '5', '6']
        check_lists = []
        for list_obj in new_shopping_lists:
            check_lists.append(list_obj.name)

        self.assertListEqual(check_lists, golden_lists, msg="Lists not ordered")
        del basket

    def test_basket_support_methods(self):
        """tests the methods that are called within the main class methods
        what i would call supporting methods-> contain delegated functionality"""
        basket = Basket()
        # test name_checker
        basket.create_list('5')
        self.assertFalse(basket.name_checker('5'))
        self.assertTrue(basket.name_checker('another_list'))

        # get_list_by_name
        basket.create_list('3')
        response_list = basket.get_list_by_name('3')
        self.assertTrue(response_list)
        self.assertTrue(type(response_list) == ShoppingList)
        self.assertTrue(response_list.name == '3')
        with self.assertRaises(ValueError):
            response_list = basket.get_list_by_name('error')
        del basket


class UserTests(unittest.TestCase):
    """ Concerned with user operations and attributes"""

    def setUp(self):
        self.user1 = User('Dennis Ngari', 'DNgari', 'DNgari@gmail.com')
        self.user2 = User('Kevin Nick', 'KNick', 'Nickson@hotmail.com')

    def tearDown(self):
        pass

    def test_password_has_no_read_feature(self):
        """ checks to make sure the password cannot be retrieved through dot notation"""
        self.assertEqual(self.user1.name, 'Dennis Ngari', msg="Retrieved wrong name")
        self.assertEqual(self.user2.name, 'Kevin Nick', msg="Retrieved wrong name")
        with self.assertRaises(AttributeError):
            self.user1.password
        # test check_password function
        self.user1.set_password('sdsf')
        self.user2.set_password('sdsf')
        self.assertTrue(self.user1.check_password('sdsf'))
        self.assertFalse(self.user2.check_password('sdasfs'))

    def test_if_one_can_create_user_with_same_email(self):
        """ register 2 users with the same email and check for and exception"""


class ItemTest(unittest.TestCase):
    """ tests item, creation, modification an deletion functionality"""

    def setUp(self):
        """setup commands to run before each test"""
        self.basket = Basket()
        self.basket.create_list('list1')
        self.basket.create_list('list2')

    def tearDown(self):
        """ cleans up after the preceding set up"""
        pass

    def test_item_creation(self):
        """checks to see if the automatically set properties are created"""
        item1 = Item('item', '20', 23.00, 'OF no importance')
        self.assertTrue(item1.author)
        self.assertTrue(item1.date_added)
        self.assertTrue(item1.date_last_modified)

    def test_item_creation_with_wrong_arguments(self):
        """" checks for data validation in item constructor"""
        with self.assertRaises(ValueError):
            Item(30, 2, '23.00', {})

    def test_basket_add_item_function(self):
        """Check for data validation, created items are added to correct list"""
        self.basket.add_item('list1', 'oranges', '20', 25.00, 'succulent')
        list_ = self.basket.get_list_by_name('list1')
        self.assertEqual(len(list_.items), 1)


class GearsTests(unittest.TestCase):
    """all things user related"""
    def setUp(self):
        """seting up """
        pass

    def tearDown(self):
        """ tears down setup"""
        pass

    def test_add_user_retrieve_function(self):
        """Checks if number of user increases after registration"""
        gear = Gears()
        initial_value = len(gear.user_list)
        response = gear.add_user('pmuriuki@gmail.com', 'password', 'Peter Muriuki', 'pnet')
        self.assertTrue(response)
        self.assertTrue(len(gear.user_list))
        current_value = len(gear.user_list)
        self.assertTrue(current_value - initial_value == 1, msg="afterall we just added one person")

        # add a person with the same username
        with self.assertRaises(Exception):
            response = gear.add_user('pemuri@gmail.com', 'password', 'Peter Muriuki', 'pnet')

        with self.assertRaises(Exception):
            response = gear.add_user('pmuriuki@gmail.com', 'password', 'Peter Muriuki', 'pn_et')

        # test retrieve user by email

        user = gear.get_user_by_email('pmuriuki@gmail.com')
        self.assertTrue(user)
        self.assertEqual(user.name, 'Peter Muriuki')

        user = gear.get_user_by_email('asbdahjsd')
        self.assertIsNone(user)