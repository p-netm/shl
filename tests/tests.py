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
        new_list = ShoppingList('Name', 'Peter', 'faedas')
        self.assertTrue(new_list.date_created)
        self.assertTrue(new_list.date_last_modified)
        self.assertFalse(len(new_list.items))
        del basket

    def test_if_shopping_list_constructor_has_error_checking(self):
        """ Test: create list with arguments being the wrong-type"""
        basket = Basket()
        with self.assertRaises(ValueError) as context:
            basket.create_list({}, 'Peter', 'faedas')
            self.assertTrue('The shopping list name can only be a string or integer' in context.exception)
        del basket

    def test_shopping_list_creates_and_adds_lists(self):
        """ test to see if the create list preserves a list object after instantiation."""
        basket = Basket()
        initial_value = len(basket.shopping_lists)
        self.assertFalse(initial_value)
        boolean = basket.create_list('First list', 'Peter', 'faedas')
        self.assertTrue(boolean)
        current_value = len(basket.shopping_lists)
        self.assertTrue(current_value)
        self.assertEqual(current_value - initial_value, 1,
                         msg="there should be one user object in the shopping_list")
        del basket

    def test_repeat_shopping_list_name(self):
        """ tests if a user can create two lists with the same name"""
        basket = Basket()
        basket.create_list('My_list', 'Peter', 'faedas')
        with self.assertRaises(ValueError):
            basket.create_list('My_list', 'Peter', 'faedas')
        self.assertTrue(len(basket.shopping_lists) == 1,
                        msg='There should be only one list created')
        del basket

    def test_delete_shopping_list(self):
        """ checks that a deleted list is no longer in the system"""
        basket = Basket()
        basket.create_list('1', 'Peter', 'faedddas')
        basket.create_list('2', 'Peter', 'faedddas')
        basket.create_list('3', 'Peter', 'faedsdas')
        new_shopping_lists = basket.delete_list('Peter','2')
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
        basket.create_list('1', 'Peter', 'faedas')
        basket.create_list('6', 'Peter', 'faedas')
        basket.create_list('2', 'Peter', 'faedas')
        basket.create_list('5', 'Peter', 'faedas')
        basket.create_list('3', 'Peter', 'faedas')

        new_shopping_lists = basket.view_list(sort='name')
        print(len(new_shopping_lists))
        golden_lists = ['1', '2', '3', '5', '6']
        check_lists = []
        for list_obj in new_shopping_lists:
            check_lists.append(list_obj.name)

        self.assertListEqual(check_lists, golden_lists, msg="Lists not ordered")
        del basket

    def test_view_shopping_list(self):
        """ checks that once a list is modified , the name supposedly changes"""
        basket = Basket()
        basket.create_list('1', 'Peter', 'faedas')
        basket.create_list('6', 'Peter', 'faedas')
        basket.create_list('2', 'Peter', 'faedas')
        basket.create_list('5', 'Peter', 'faedas')
        basket.create_list('3', 'Peter', 'faedas')

        basket.modify_list(name='1', link_name='Peter', new_name='one')
        lists_names = []
        for list_ in basket.shopping_lists:
            lists_names.append(list_.name)
        self.assertNotIn('1', lists_names)
        self.assertIn('one', lists_names)
        self.assertEqual(len(basket.shopping_lists), 5, msg=" the number of list should not change")


    def test_basket_support_methods(self):
        """tests the methods that are called within the main class methods
        what i would call supporting methods-> contain delegated functionality"""
        basket = Basket()
        # test name_checker
        basket.create_list('5', 'Peter', 'faedas')
        self.assertFalse(basket.name_checker('Peter', '5'))
        self.assertTrue(basket.name_checker('Peter', 'another_list'))

        # get_list_by_name
        basket.create_list('3', 'Peter', 'faedas')
        response_list = basket.get_list_by_name('3', 'Peter')
        self.assertTrue(response_list)
        self.assertTrue(type(response_list) == ShoppingList)
        self.assertTrue(response_list.name == '3')
        with self.assertRaises(ValueError):
            response_list = basket.get_list_by_name('error', 'Peter')
        token = basket.generate_token(response_list.name)
        print(token)
        list_name = basket.decodes_token(token)
        self.assertTrue(list_name == response_list.name)
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
        self.assertTrue(self.user1.check_password('sdsf', self.user1.hashed_pass ))
        self.assertFalse(self.user2.check_password('sdasfs', self.user2.hashed_pass))

    def test_if_one_can_create_user_with_same_email(self):
        """ register 2 users with the same email and check for and exception"""


class ItemTest(unittest.TestCase):
    """ tests item, creation, modification an deletion functionality"""

    def setUp(self):
        """setup commands to run before each test"""
        self.basket = Basket()
        self.basket.create_list('list1', 'Peter', 'faedas')
        self.basket.create_list('list2', 'Peter', 'faedas')

    def tearDown(self):
        """ cleans up after the preceding set up"""
        pass

    def test_item_creation(self):
        """checks to see if the automatically set properties are created"""
        item1 = Item('item', '20', 23.00, 'OF no importance')
        self.assertTrue(item1.date_added)
        self.assertTrue(item1.date_last_modified)

    def test_item_creation_with_wrong_arguments(self):
        """" checks for data validation in item constructor"""
        with self.assertRaises(ValueError):
            Item(30, 2, '23.00', {})

    def test_basket_add_item_function(self):
        """Check for data validation, created items are added to correct list"""
        self.basket.add_item('Peter', 'list1', 'oranges', '20', 25.00, 'succulent')
        list_ = self.basket.get_list_by_name('list1', 'Peter')
        self.assertEqual(len(list_.items), 1)

    def test_basket_modify_item(self):
        """ Tries and checks that an item data is changed after its called"""
        basket = Basket()
        basket.create_list('list1', 'Peter', 'faedas')
        basket.add_item('Peter', 'list1', 'oranges', '20', 25.00, 'succulent')
        #check modification time changes
        item_obj = basket.shopping_lists[0].items[0]
        init_mod_time = item_obj.date_last_modified
        basket.modify_item('Peter', 'oranges', 'list1', name='Bananas')
        self.assertEqual(item_obj.name, 'Bananas', msg="name has not changed")
        # change quantity
        basket.modify_item('Peter', 'Bananas', 'list1', quantity='15')
        self.assertTrue(item_obj.quantity == '15')
        init_price = item_obj.price
        basket.modify_item('Peter', 'Bananas', 'list1', price=3.23)
        self.assertFalse(init_price == item_obj.price)
        self.assertTrue(item_obj.price == 3.23)
        inti_desc = item_obj.description
        basket.modify_item('Peter', 'Bananas', 'list1', description="juicy")
        self.assertFalse(item_obj.description == inti_desc)
        self.assertTrue(item_obj.description == "juicy")

    def test_retrieve_item(self):
        """check error raised if item not found"""
        basket = Basket()
        basket.create_list('list1', 'Peter', 'faedas')
        basket.add_item('Peter', 'list1',  'oranges', '20', 25.00, 'succulent')
        response = basket.get_item_by_name(link_name='Peter', item_name='oranges', list_name='list1')
        self.assertTrue(response)
        self.assertTrue(response.name == 'oranges')
        self.assertEqual(type(response), Item)
        with self.assertRaises(Exception):
            basket.get_item_by_name('adjfgad')

    def test_delete_item(self):
        """ checks that an item ceases to exist after being deleted"""
        basket = Basket()
        basket.create_list('list1', 'Peter', 'faedas')
        basket.add_item('Peter', 'list1', 'oranges', '20', 25.00, 'succulent')
        response = basket.delete_item('Peter', 'oranges', 'list1')
        self.assertFalse(len(response.items))

    def test_view_item_sorted_list(self):
        """Checks if view_ item does sort """
        basket = Basket()
        basket.create_list('list1', 'Peter', 'faedas')
        basket.add_item('Peter', 'list1', 'oranges', '2', 25.00, 'succulent')
        basket.add_item('Peter', 'list1', 'mangoes', '10', 25.00, 'succulent')
        basket.add_item('Peter', 'list1', 'apples', '15', 25.00, 'succulent')
        basket.add_item('Peter', 'list1', 'peach', '7', 25.00, 'succulent')
        basket.add_item('Peter', 'list1', 'passion', '16', 25.00, 'succulent')

        list_ = basket.get_list_by_name('list1', 'Peter')
        item_names = []
        for item in list_.items:
            item_names.append(item.name)
        self.assertListEqual(item_names, ['oranges', 'mangoes', 'apples', 'peach', 'passion'])


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

    def test_extract_number_from_quantity(self):
        basket = Basket()
        number = basket.extract_number_from_quantity('2kgs')
        self.assertTrue(type(number) == float)
        self.assertEqual(number, 2.0)

    def test_checking_permission(self):
        """"sees to it that an owner is granted permissions to his lists"""
        basket = Basket()
        basket.create_list('list1', 'Peter', 'faedas')
        obj = basket.get_list_by_name('list1', 'Peter')
        boolean = basket.check_permission(obj, 'Peter')
        self.assertTrue(boolean)
        self.assertFalse(basket.check_permission(obj, 'Peterasd'))