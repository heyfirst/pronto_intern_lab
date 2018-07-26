import unittest


def isFizz(number):
    if (number % 3 == 0):
        return 'Fizz'
    return None


def isBuzz(number):
    if (number % 5 == 0):
        return 'Buzz'
    return None


def isFizzBuzz(number):
    if (number % 3 == 0 and number % 5 == 0):
        return 'FizzBuzz'
    return None


def notFizzBuzz(number):
    if (number % 3 != 0 and number % 5 != 0):
        return number
    return None


class FizzBuzzFactory(object):
    rules = []

    def say(self, number):
        for rule in self.rules:
            if rule(number) != None:
                return rule(number)


class FizzClass(FizzBuzzFactory):
    rules = [isFizz]


class BuzzClass(FizzBuzzFactory):
    rules = [isBuzz]


class FizzBuzzClass(FizzBuzzFactory):
    rules = [isFizzBuzz]


class NotFizzBuzzClass(FizzBuzzFactory):
    rules = [notFizzBuzz]


class FullFizzBuzzClass(FizzBuzzFactory):
    rules = [notFizzBuzz, isFizzBuzz, isBuzz, isFizz]


class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.fizzbuzz = FullFizzBuzzClass()

    def test_input_3_return_Fizz(self):
        fizzbuzz = FizzClass()
        actual = fizzbuzz.say(3)
        self.assertEqual(actual, 'Fizz')

    def test_input_6_return_Fizz(self):
        actual = self.fizzbuzz.say(6)
        self.assertEqual(actual, 'Fizz')

    def test_input_5_return_Buzz(self):
        fizzbuzz = BuzzClass()
        actual = fizzbuzz.say(5)
        self.assertEqual(actual, 'Buzz')

    def test_input_10_return_Buzz(self):
        actual = self.fizzbuzz.say(10)
        self.assertEqual(actual, 'Buzz')

    def test_input_15_return_FizzBuzz(self):
        fizzbuzz = FizzBuzzClass()
        actual = fizzbuzz.say(15)
        self.assertEqual(actual, 'FizzBuzz')

    def test_input_30_return_FizzBuzz(self):
        actual = self.fizzbuzz.say(30)
        self.assertEqual(actual, 'FizzBuzz')

    def test_input_1_return_1(self):
        fizzbuzz = NotFizzBuzzClass()
        actual = fizzbuzz.say(1)
        self.assertEqual(actual, 1)

    def test_input_2_return_2(self):
        actual = self.fizzbuzz.say(2)
        self.assertEqual(actual, 2)


unittest.main()