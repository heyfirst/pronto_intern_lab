import unittest


class Roman(object):
    def say(self, number):
        result = ''
        while (number > 0):
            if (number >= 10):
                result += 'X'
                number -= 10
            elif (number >= 9):
                result += 'IX'
                number -= 9
            elif (number >= 5):
                result += 'V'
                number -= 5
            elif (number >= 4):
                result += 'IV'
                number -= 4
            elif (number >= 1):
                result += 'I'
                number -= 1

        return result


class RomanTest(unittest.TestCase):
    def setUp(self):
        self.roman = Roman()

    def test_input_1_return_I(self):
        actual = self.roman.say(1)
        self.assertEqual(actual, 'I')

    def test_input_2_return_II(self):
        actual = self.roman.say(2)
        self.assertEqual(actual, 'II')

    def test_input_4_return_IV(self):
        actual = self.roman.say(4)
        self.assertEqual(actual, 'IV')

    def test_input_5_return_V(self):
        actual = self.roman.say(5)
        self.assertEqual(actual, 'V')

    def test_input_6_return_VI(self):
        actual = self.roman.say(6)
        self.assertEqual(actual, 'VI')

    def test_input_7_return_VII(self):
        actual = self.roman.say(7)
        self.assertEqual(actual, 'VII')

    def test_input_9_return_IX(self):
        actual = self.roman.say(9)
        self.assertEqual(actual, 'IX')

    def test_input_10_return_X(self):
        actual = self.roman.say(10)
        self.assertEqual(actual, 'X')

    def test_input_12_return_XII(self):
        actual = self.roman.say(12)
        self.assertEqual(actual, 'XII')

    def test_input_15_return_XV(self):
        actual = self.roman.say(15)
        self.assertEqual(actual, 'XV')


unittest.main()