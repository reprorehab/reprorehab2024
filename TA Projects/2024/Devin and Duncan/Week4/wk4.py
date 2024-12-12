# ReproRehab Pod 2 24/25 - Week 4 Activities 
# When you run this script you should see all tests fail
# Your goal is to edit the code such that all tests pass 

# Topics - Functions (debuggin inherent)

import unittest
import week4_funs

class Week4(unittest.TestCase):
    
    def test_sum_func_1(self):
        self.assertEqual(week4_funs.sum_values(3, 4), 7)

    def test_is_upper_case_1(self):
        self.assertTrue(week4_funs.is_upper_case('H'))

    def test_is_upper_case_2(self):
        self.assertFalse(week4_funs.is_upper_case('h'))

    def test_add_element_to_list_1(self):
        a = ['hello', 'world']
        b = 'Devin'
        self.assertEqual(week4_funs.add_element_if_unique(a, b), a.append(b))

    def test_add_element_to_list_2(self):
        a = ['i', 'like', 'turtles']
        b = 'turtles'
        self.assertEqual(week4_funs.add_element_if_unique(a, b), a)

    def test_fizz_buzz_1(self):
        self.assertEqual(week4_funs.fizz_buzz(3), 'Fizz')

    def test_fizz_buzz_2(self):
        self.assertEqual(week4_funs.fizz_buzz(5), 'Buzz')

    def test_fizz_buzz_3(self):
        self.assertEqual(week4_funs.fizz_buzz(15), 'FizzBuzz')

    def test_fizz_buzz_4(self):
        self.assertEqual(week4_funs.fizz_buzz(11), None)
        

if __name__ == "__main__":
    unittest.main()
