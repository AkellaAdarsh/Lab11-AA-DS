import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(3,6),9)
    def test_subtract(self):
        self.assertEqual(sub(5,3),2)
        self.assertEqual(sub(0,4),-4)
        self.assertEqual(sub(10,7),3)
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0,5)
    def test_logarithm(self):
        self.assertEqual(log(10, 100), 2)
        self.assertEqual(log(2, 8), 3)
        self.assertEqual(log(4, 16), 2)
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 10)


    def test_multiply(self):
        self.assertEqual(mul(4, 5), 20)
        self.assertEqual(mul(-3, 6), -18)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self):
        self.assertEqual(div(20, 5), 4)
        self.assertAlmostEqual(div(7, 2), 3.5)
        self.assertAlmostEqual(div(1, 4), 0.25)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(0)

        with self.assertRaises(ValueError):
            log(-10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(8, 15), 17.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(25), 5.0)
        self.assertAlmostEqual(square_root(2), 1.41421356237, places=5)
        self.assertAlmostEqual(square_root(0), 0.0)


# Do not touch this
if __name__ == "__main__":
    unittest.main()