from unittest import TestCase

from main.calculator.services.calculator import *


class Test(TestCase):
    def test_calculate(self):
        self.assertEqual(1.0, calculate("1"))
        self.assertEqual(4.0, calculate("2+2"))
        self.assertEqual(6000000.0, calculate("2x3000000"))
        self.assertEqual(140.88888888888889, calculate("122 + 34 * 5 / 9"))

    def test_generate_expression_list(self):
        actual = generate_expression_list("12")
        expected = ["12"]
        self.assertListEqual(actual, expected)

        actual = generate_expression_list("12 + 2")
        expected = ["12", "+", "2"]
        self.assertListEqual(actual, expected)

        actual = generate_expression_list("122 + 34 * 5 / 9 ")
        expected = ["122", "+", "34", "*", "5", "/", "9"]
        self.assertListEqual(actual, expected)

        actual = generate_expression_list("122 + 34 ! * 5 ^ 2 / 9 ")
        expected = ["122", "+", "34", "!", "*", "5", "^", "2", "/", "9"]
        self.assertListEqual(actual, expected)

    def test_evaluate_multiplications(self):
        sample = ["12"]
        actual = evaluate_multiplications(sample)
        expected = ["12"]
        self.assertListEqual(actual, expected)

        sample = ["2", "*", "2"]
        actual = evaluate_multiplications(sample)
        expected = ["4.0"]
        self.assertListEqual(actual, expected)

        sample = ["2", "*", "2", "*", "2"]
        actual = evaluate_multiplications(sample)
        expected = ["8.0"]
        self.assertListEqual(actual, expected)

        sample = ["2", "*", "2", "*", "2", "+", "2"]
        actual = evaluate_multiplications(sample)
        expected = ["8.0", "+", "2"]
        self.assertListEqual(actual, expected)

        sample = ["2", "+", "2", "*", "2", "*", "2"]
        actual = evaluate_multiplications(sample)
        expected = ["2", "+", "8.0"]
        self.assertListEqual(actual, expected)

    def test_evaluate_division(self):
        sample = ["12"]
        actual = evaluate_divisions(sample)
        expected = ["12"]
        self.assertListEqual(actual, expected)

        sample = ["2", "/", "2"]
        actual = evaluate_divisions(sample)
        expected = ["1.0"]
        self.assertListEqual(actual, expected)

        sample = ["2", "/", "2", "/", "2"]
        actual = evaluate_divisions(sample)
        expected = ["0.5"]
        self.assertListEqual(actual, expected)

        sample = ["2", "/", "2", "/", "2", "+", "2"]
        actual = evaluate_divisions(sample)
        expected = ["0.5", "+", "2"]
        self.assertListEqual(actual, expected)

        sample = ["2", "+", "2", "/", "2", "/", "2"]
        actual = evaluate_divisions(sample)
        expected = ["2", "+", "0.5"]
        self.assertListEqual(actual, expected)

    def test_evaluate_remainder(self):
        sample = ["12"]
        actual = evaluate_remainders(sample)
        expected = ["12"]
        self.assertListEqual(actual, expected)

        sample = ["10", "%", "2"]
        actual = evaluate_remainders(sample)
        expected = ["0.0"]
        self.assertListEqual(actual, expected)

        sample = ["10", "%", "3"]
        actual = evaluate_remainders(sample)
        expected = ["1.0"]
        self.assertListEqual(actual, expected)

        sample = ["100", "%", "13", "%", "2"]
        actual = evaluate_remainders(sample)
        expected = ["1.0"]
        self.assertListEqual(actual, expected)

        sample = ["100", "%", "13", "%", "2", "+", "9"]
        actual = evaluate_remainders(sample)
        expected = ["1.0", "+", "9"]
        self.assertListEqual(actual, expected)

        sample = ["9", "+", "100", "%", "13", "%", "2"]
        actual = evaluate_remainders(sample)
        expected = ["9", "+", "1.0"]
        self.assertListEqual(actual, expected)

    def test_evaluate_additions(self):
        sample = ["12"]
        actual = evaluate_additions(sample)
        expected = ["12"]
        self.assertListEqual(actual, expected)

        sample = ["10", "+", "2"]
        actual = evaluate_additions(sample)
        expected = ["12.0"]
        self.assertListEqual(actual, expected)

        sample = ["10", "+", "3"]
        actual = evaluate_additions(sample)
        expected = ["13.0"]
        self.assertListEqual(actual, expected)

        sample = ["100", "+", "13", "+", "2"]
        actual = evaluate_additions(sample)
        expected = ["115.0"]
        self.assertListEqual(actual, expected)

        sample = ["100", "+", "13", "+", "2", "/", "9"]
        actual = evaluate_additions(sample)
        expected = ["115.0", "/", "9"]
        self.assertListEqual(actual, expected)

        sample = ["9", "%", "100", "+", "13", "+", "2"]
        actual = evaluate_additions(sample)
        expected = ["9", "%", "115.0"]
        self.assertListEqual(actual, expected)

    def test_evaluate_subtractions(self):
        sample = ["12"]
        actual = evaluate_subtractions(sample)
        expected = ["12"]
        self.assertListEqual(actual, expected)

        sample = ["10", "-", "2"]
        actual = evaluate_subtractions(sample)
        expected = ["8.0"]
        self.assertListEqual(actual, expected)

        sample = ["10", "-", "3"]
        actual = evaluate_subtractions(sample)
        expected = ["7.0"]
        self.assertListEqual(actual, expected)

        sample = ["100", "-", "13", "-", "2"]
        actual = evaluate_subtractions(sample)
        expected = ["85.0"]
        self.assertListEqual(actual, expected)

        sample = ["100", "-", "13", "-", "2", "/", "9"]
        actual = evaluate_subtractions(sample)
        expected = ["85.0", "/", "9"]
        self.assertListEqual(actual, expected)

        sample = ["9", "%", "100", "-", "13", "-", "2"]
        actual = evaluate_subtractions(sample)
        expected = ["9", "%", "85.0"]
        self.assertListEqual(actual, expected)

    def test_evaluation_polarity(self):
        sample = "+1"
        actual = evaluation_polarity(sample)
        expected = "+1"
        self.assertEqual(actual, expected)

        sample = "++2"
        actual = evaluation_polarity(sample)
        expected = "+2"
        self.assertEqual(actual, expected)

        sample = "+++3"
        actual = evaluation_polarity(sample)
        expected = "+3"
        self.assertEqual(actual, expected)

        sample = "+-3"
        actual = evaluation_polarity(sample)
        expected = "-3"
        self.assertEqual(actual, expected)

        sample = "--3"
        actual = evaluation_polarity(sample)
        expected = "+3"
        self.assertEqual(actual, expected)

    def test_evaluation_factorials(self):
        sample = ["12"]
        actual = evaluate_factorials(sample)
        expected = ["12"]
        self.assertListEqual(actual, expected)

        sample = ["2", "!", "-", "2"]
        actual = evaluate_factorials(sample)
        expected = ["2.0", "-", "2"]
        self.assertListEqual(actual, expected)

        sample = ["3", "!"]
        actual = evaluate_factorials(sample)
        expected = ["6.0"]
        self.assertListEqual(actual, expected)

        sample = ["3", "!", "+", "4", "!", "/", "5", "!"]
        actual = evaluate_factorials(sample)
        expected = ["6.0", "+", "24.0", "/", "120.0"]
        self.assertListEqual(actual, expected)

    def test_evaluate_exponents(self):
        sample = ["12"]
        actual = evaluate_exponents(sample)
        expected = ["12"]
        self.assertListEqual(actual, expected)

        sample = ["12", "^", "2"]
        actual = evaluate_exponents(sample)
        expected = ["144.0"]
        self.assertListEqual(actual, expected)

        sample = ["3", "^", "2", "+", "34"]
        actual = evaluate_exponents(sample)
        expected = ["9.0", "+", "34"]
        self.assertListEqual(actual, expected)

    def test_evaluate_square_roots(self):
        sample = ["12"]
        actual = evaluate_square_roots(sample)
        expected = ["12"]
        self.assertListEqual(actual, expected)

        sample = ["√", "9"]
        actual = evaluate_square_roots(sample)
        expected = ["3.0"]
        self.assertListEqual(actual, expected)

        sample = ["√", "36", "+", "36"]
        actual = evaluate_square_roots(sample)
        expected = ["6.0" , "+", "36"]
        self.assertListEqual(actual, expected)

        sample = ["3", "-", "√", "36"]
        actual = evaluate_square_roots(sample)
        expected = ["3", "-", "6.0"]
        self.assertListEqual(actual, expected)

    def test_evaluate_parenthesis(self):

        pass
