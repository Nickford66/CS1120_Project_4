import unittest

class TestBookshop(unittest.TestCase):
    def setUp(self):
        self.orders = [[1, ("5464", 4, 9.99), ("8274", 18, 12.99), ("9744", 9, 44.95)],
                       [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
                       [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
                       [4, ("8732", 7, 11.99), ("7733", 11, 18.99), ("88112", 5, 39.95)]]

        self.test_order = Bookshop(self.orders)

    def test_01(self):
        actual = self.test_order.method1()
        expected = [
            (1, ('5464', 49.96), ('8274', 233.82), ('9744', 404.55)),
            (2, ('5464', 99.91), ('9744', 404.55)),
            (3, ('5464', 99.91), ('88112', 274.89)),
            (4, ('8732', 93.93), ('7733', 208.89), ('88112', 199.75))
        ]
        self.assertEqual(actual, expected)
        print("\nExpected:", expected)
        print("Actual:", actual)
        
    def test_02(self):
      self.assertTrue()
        
    def test_03(self):
      self.assertTrue()
        
    def test_04(self):
        actual = self.test_order.method4()
        expected = [
            (1, 678.33),
            (2, 494.46),
            (3, 364.8),
            (4, 492.57)
        ]
        self.assertEqual(actual, expected)
        print("\nExpected:", expected)
        print("Actual:", actual)
        
    def test_05(self):
        actual = self.test_order.method5()
        expected = '9744'
        self.assertIn(expected, actual)
        print("\nBook order number:", expected)
        print("Returned List:", actual)
        
    def test_06(self):
      self.assertTrue()
        
    def test_07(self):
        actual = self.test_order.method7()
        expected = [
            (1, 31),
            (4, 23),
            (3, 20),
            (2, 18)
        ]
        self.assertEqual(actual, expected)
        print("\nExpected:", expected)
        print("Actual:", actual)
        
    def test_08(self):
      self.assertTrue()
        
    def test_09(self):   
        actual = self.test_order.method9()
        expected = ['5464', '8274']
        self.assertEqual(actual, expected)
        print("\nExpected:", expected)
        print("Actual:", actual)
        
    def test_10(self):
      self.assertTrue()

if __name__ == '__main__':
    unittest.main()

  

