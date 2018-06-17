import unittest


class FizzBuzz(object):
    def say(self, number):
        fizzbuzz = {
          number % 15 == 0: 'Fizz'
          number % 3 == 0: 'Fizz'
          number % 3 == 0: 'Fizz'
        }

        return number


class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def test_input_3_return_Fizz(self):
        actual = self.fizzbuzz.say(3)
        self.assertEqual(actual, 'Fizz')

    def test_input_6_return_Fizz(self):
        actual = self.fizzbuzz.say(6)
        self.assertEqual(actual, 'Fizz')

    def test_input_5_return_Buzz(self):
        actual = self.fizzbuzz.say(5)
        self.assertEqual(actual, 'Buzz')

    def test_input_10_return_Buzz(self):
        actual = self.fizzbuzz.say(10)
        self.assertEqual(actual, 'Buzz')

    def test_input_15_return_FizzBuzz(self):
        actual = self.fizzbuzz.say(15)
        self.assertEqual(actual, 'FizzBuzz')

    def test_input_1_return_1(self):
        actual = self.fizzbuzz.say(1)
        self.assertEqual(actual, 1)

    def test_input_2_return_2(self):
        actual = self.fizzbuzz.say(1)
        self.assertEqual(actual, 1)


unittest.main()