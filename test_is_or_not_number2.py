import unittest
import is_or_not_number2 as num


class MyTestCase(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(num.is_even(2))
        self.assertFalse(num.is_even(5))
        self.assertRaises(TypeError,num.is_even,-2)
        self.assertRaises(TypeError,num.is_even,2.2)
        self.assertTrue(num.is_even(0))

    def test_is_odd(self):
        self.assertTrue(num.is_odd(3))
        self.assertFalse(num.is_odd(6))
        self.assertRaises(TypeError,num.is_odd,-3)
        self.assertRaises(TypeError,num.is_odd,5.3)

    def test_is_armstrong(self):
        self.assertTrue(num.is_armstrong(153))
        self.assertFalse(num.is_armstrong(11))
        self.assertTrue(num.is_armstrong(0))
        self.assertTrue(num.is_armstrong(1))
        self.assertRaises(TypeError,num.is_armstrong,-3)
        self.assertRaises(TypeError,num.is_armstrong,5.3)

if __name__ == '__main__':
    unittest.main()
