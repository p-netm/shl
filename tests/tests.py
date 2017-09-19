__author__ = 'Sudo Pnet'
import unittest
from shl.app.models import Basket


class ShoppingListTests(unittest.TestCase):

    def setUp(self):
        """ instantiate common attributes for this class"""
        self.basket = Basket()

    def tearDown(self):
        """pretty straightforward, tears down attributes created in setUp()"""
        pass

    def test_if_shopping_list_constructor_has_error_checking(self):
        """ Test: create list with arguments being the wrong-type"""
        with self.assertRaises(ValueError) as context:
            self.basket.create_list({})
            self.assertTrue('The shopping list name can only be a string or integer' in context.exception)

    def test_shopping_list_create_item(self):
        initial_value = len(self.basket.shopping_list)
        self.assertFalse(initial_value)
        bool = self.basket.create_list('First list')
        self.assertTrue(bool)
        current_value = len(self.basket.shopping_list)
        self.assertTrue(current_value)
        self.assertEqual(current_value - initial_value, 1,
                         msg="there should be one user object in the shopping_list")

