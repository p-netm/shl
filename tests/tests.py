__author__ = 'Sudo Pnet'
import unittest
from shl.app.models import Basket, ShoppingList, User


class ShoppingListTests(unittest.TestCase):

    def setUp(self):
        """ instantiate common attributes for this class"""
        self.basket = Basket()

    def tearDown(self):
        """pretty straightforward, tears down attributes created in setUp()"""
        pass

    def test_shopping_list_auto_properties(self):
        """checks if the automatically set propeties are as they should be"""
        new_list = ShoppingList('Name')
        self.assertTrue(new_list.date_created)
        self.assertTrue(new_list.date_last_modified)
        self.assertFalse(len(new_list.items))


    def test_if_shopping_list_constructor_has_error_checking(self):
        """ Test: create list with arguments being the wrong-type"""
        with self.assertRaises(ValueError) as context:
            self.basket.create_list({})
            self.assertTrue('The shopping list name can only be a string or integer' in context.exception)

    def test_shopping_list_creates_and_adds_lists(self):
        """ test to see if the create list preserves a list object after instantiation."""
        initial_value = len(self.basket.shopping_lists)
        self.assertFalse(initial_value)
        bool = self.basket.create_list('First list')
        self.assertTrue(bool)
        current_value = len(self.basket.shopping_lists)
        self.assertTrue(current_value)
        self.assertEqual(current_value - initial_value, 1,
                         msg="there should be one user object in the shopping_list")

    def test_repeat_shopping_list_name(self):
        """ tests if a user can create two lists with the same name"""
        initial_value = len(self.basket.shopping_lists)
        self.basket.create_list('My_list')
        response = self.basket.create_list('My_list')
        self.assertFalse(response)
        self.assertTrue(len(self.basket.shopping_lists), 1,
                        msg='There should be only one list created')

    def test_delete_shopping_list(self):
        """ checks that a deleted list is no longer in the system"""
        self.basket.create_list('1')
        self.basket.create_list('2')
        self.basket.create_list('3')
        new_shopping_lists = self.basket.delete_list('2')
        current_value = len(self.basket.shopping_lists)
        self.assertTrue(current_value, 2)
        # create a list of the shopping_lists names and confirm the deleted list's name
        # is not in it
        list_names = []
        for list_obj in self.basket.shopping_lists:
            list_names.append(list_obj.name)
        self.assertNotIn('2', list_names,
                         msg="How comes the delted list names still shows up")

    def test_view_shopping_list(self):
        """ checks that the view list obeys the sorting order requested"""
        self.basket.create_list('1')
        self.basket.create_list('6')
        self.basket.create_list('2')
        self.basket.create_list('5')
        self.basket.create_list('3')

        new_shopping_lists = self.basket.view_list(sort='name')
        golden_lists = ['1', '2', '3', '5', '6']
        check_lists = []
        for list_obj in new_shopping_lists:
            check_lists.append(list_obj.name)

        self.assertListEqual(check_lists, golden_lists, msg="Lists not ordered")

    def test_basket_supporting_methods(self):
        """tests the methods that are called within the main class methods
        what i would call supporting methods-> contain delegated functionality"""
        # test name_checker
        self.basket.create_list('5')
        self.assertTrue(self.basket.name_checker('5'))
        self.assertFalse(self.basket.name_checker('another_list'))

        # get_list_by_name
        self.basket.create_list('3')
        response_list = self.basket.get_list_by_name('3')
        self.assertTrue(response_list)
        self.assertTrue(type(response_list) == ShoppingList)
        self.assertTrue(response_list.name == '3')
        with self.raises(ValueError):
            response_list = self.basket.get_list_by_name('error')





class UserTests(unittest.TestCase):
    """ Concerned with user operations and attributes"""

    def setUp(self):
        self.user1 = User('Dennis', 'Ngari', 'DNgari', 'DNgari@gmail.com')
        self.user2 = User('Kevin', 'Nick', 'KNick', 'Nickson@hotmail.com')

    def tearDown(self):
        pass

    def test_password_has_no_read_feature(self):
        """ checks to make sure the password cannot be retrieved through dot notation"""
        self.assertEqual(self.user1.f_name, 'Dennis', msg="Retrieved wrong name")
        self.assertEqual(self.user2.o_name, 'Nick', msg="Retrieved wrong name")
        with self.assertRaises(AttributeError):
            self.user1.password

        # checks that two users with the same password have different hashes
        self.user1.set_password('sdsf')
        self.user2.set_password('sdsf')
        self.assertFalse(self.user1.hashed_pass == self.user2.hashed_pass)

        # test check_password function
        self.assertTrue(self.user1.check_password('sdsf'))
        self.assertFalse(self.user2.check_password('sdasfs'))

    def test_if_one_can_create_user_with_same_email(self):
        """ register 2 users with the same email and check for and exception"""




