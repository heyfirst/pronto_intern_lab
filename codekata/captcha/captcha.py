import random
import unittest
from unittest.mock import patch


class Captcha(object):
    def random_number(self):
        return random.randint(0, 10)

    def random_operator(self):
        operators = [
            '+',
            '-',
            '*',
            '/',
        ]
        return random.choice(operators)

    def random_word_number(self):
        word_numbers = [
            'one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine',
            'ten',
        ]
        return random.choice(word_numbers)

    def convert_word_number_to_number(self, word_number):
        number = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'ten': 10,
        }
        return number[word_number]

    def calculate(self):
        left_operand = self.random_number()
        operator = self.random_operator()
        word_number = self.random_word_number()
        right_operand = self.convert_word_number_to_number(word_number)

        result_by_operator = {
            '+': left_operand + right_operand,
            '-': left_operand - right_operand,
            '*': left_operand * right_operand,
            '/': left_operand / right_operand,
        }

        return result_by_operator[operator]


class CaptchaTest(unittest.TestCase):
    def setUp(self):
        self.captcha = Captcha()
        self.operators = [
            '+',
            '-',
            '*',
            '/',
        ]
        self.word_numbers = [
            'one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine',
            'ten',
        ]

    @patch('__main__.random.randint')
    def test_random_number_should_call_randint(self, mock_randint):
        self.captcha.random_number()
        mock_randint.assert_called_once_with(0, 10)

    def test_random_number_should_return_number(self):
        result = self.captcha.random_number()
        self.assertTrue(str(result).isdigit())

    @patch('__main__.random.choice')
    def test_random_operator_should_call_random_choice(self, mock_choice):
        self.captcha.random_operator()
        mock_choice.assert_called_once_with(self.operators)

    def test_random_operator_should_return_operator(self):
        result = self.captcha.random_operator()
        self.assertTrue(result in self.operators)

    @patch('__main__.random.choice')
    def test_random_word_number_should_call_random_choice(self, mock_choice):
        self.captcha.random_word_number()
        mock_choice.assert_called_once_with(self.word_numbers)

    def test_random_word_number_should_return_word_number(self):
        result = self.captcha.random_word_number()
        self.assertTrue(result in self.word_numbers)

    def test_calculate_1_plus_one_should_return_2(self):
        with patch('__main__.Captcha.random_number') as mock_randint:
            with patch('__main__.Captcha.random_operator') as mock_chioce:
                with patch('__main__.Captcha.random_word_number'
                           ) as mock_chioce_word_number:
                    mock_randint.return_value = 1
                    mock_chioce.return_value = '+'
                    mock_chioce_word_number.return_value = 'one'

                    result = self.captcha.calculate()
                    self.assertEqual(result, 2)

    def test_calculate_9_minus_two_should_return_7(self):
        with patch('__main__.Captcha.random_number') as mock_randint:
            with patch('__main__.Captcha.random_operator') as mock_chioce:
                with patch('__main__.Captcha.random_word_number'
                           ) as mock_chioce_word_number:
                    mock_randint.return_value = 9
                    mock_chioce.return_value = '-'
                    mock_chioce_word_number.return_value = 'two'

                    result = self.captcha.calculate()
                    self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main()
