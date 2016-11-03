import unittest
from basket import Basket
import numbers


class BasketTests(unittest.TestCase):

    def setUp(self):
        print("Setting up")
        self.keijon_ostoskori = Basket("Keijo", ["kissa", "pasi"], 5)
    
    def tearDown(self):
        print("Tearing down")
        del self.keijon_ostoskori
    
    def test_customer_is_string(self):
        self.assertTrue(isinstance(self.keijon_ostoskori.customer, str), "variable customer name should be a string")
    def test_contents_is_list(self):
        self.assertTrue(isinstance(self.keijon_ostoskori.contents, list), "variable contents should be a list")
    def test_price_is_number(self):
        self.assertTrue(isinstance(self.keijon_ostoskori.price, numbers.Number), "variable price should be a number")
    def test_list_add(self):
        self.keijon_ostoskori.add_product("kala", 5)
        self.assertIn("kala", self.keijon_ostoskori.contents, "add_product did not add product to the list")
    def test_list_delete(self):
        self.keijon_ostoskori.delete_product("kala", 5)
        self.assertNotIn("kala", self.keijon_ostoskori.contents, "delete_product did not delete product from the list")
    
if __name__ == '__main__':
    unittest.main()
        
