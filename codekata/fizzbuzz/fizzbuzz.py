import unittest


class FizzBuzz(object):
    def say(self, number):
        if (number % 3 == 0 and number % 5 == 0):
            return 'FizzBuzz'
        if (number % 3 == 0):
            return 'Fizz'
        if (number % 5 == 0):
            return 'Buzz'

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

    def test_input_30_return_FizzBuzz(self):
        actual = self.fizzbuzz.say(30)
        self.assertEqual(actual, 'FizzBuzz')

    def test_input_1_return_1(self):
        actual = self.fizzbuzz.say(1)
        self.assertEqual(actual, 1)

    def test_input_2_return_2(self):
        actual = self.fizzbuzz.say(1)
        self.assertEqual(actual, 1)


unittest.main()