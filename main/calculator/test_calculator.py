from unittest import TestCase

from calculator import *

class Test(TestCase):
    def test_calculate(self):
        self.assertEqual(1.0, calculate("1"))
        self.assertEqual(4.0, calculate("2+2"))
        self.assertEqual(6.0, calculate("2*3"))
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

    def test_evaluate_multiplications(self):
        sample_1 = ["12"]
        actual = evaluate_multiplications(sample_1)
        expected = ["12"]
        self.assertListEqual(actual, expected)

        sample_1 = ["2", "*", "2"]
        actual = evaluate_multiplications(sample_1)
        expected = ["4.0"]
        self.assertListEqual(actual, expected)

        sample_2 = ["2", "*", "2", "*", "2"]
        actual = evaluate_multiplications(sample_2)
        expected = ["8.0"]
        self.assertListEqual(actual, expected)

        sample_2 = ["2", "*", "2", "*", "2", "+", "2"]
        actual = evaluate_multiplications(sample_2)
        expected = ["8.0", "+", "2"]
        self.assertListEqual(actual, expected)

        sample_2 = ["2", "+", "2", "*", "2", "*", "2"]
        actual = evaluate_multiplications(sample_2)
        expected = ["2", "+", "8.0"]
        self.assertListEqual(actual, expected)

    def test_evaluate_division(self):
        sample_1 = ["12"]
        actual = evaluate_divisions(sample_1)
        expected = ["12"]
        self.assertListEqual(actual, expected)

        sample_1 = ["2", "/", "2"]
        actual = evaluate_divisions(sample_1)
        expected = ["1.0"]
        self.assertListEqual(actual, expected)

        sample_2 = ["2", "/", "2", "/", "2"]
        actual = evaluate_divisions(sample_2)
        expected = ["0.5"]
        self.assertListEqual(actual, expected)

        sample_2 = ["2", "/", "2", "/", "2", "+", "2"]
        actual = evaluate_divisions(sample_2)
        expected = ["0.5", "+", "2"]
        self.assertListEqual(actual, expected)

        sample_2 = ["2", "+", "2", "/", "2", "/", "2"]
        actual = evaluate_divisions(sample_2)
        expected = ["2", "+", "0.5"]
        self.assertListEqual(actual, expected)

    def test_evaluate_remainder(self):
        sample_1 = ["12"]
        actual = evaluate_remainders(sample_1)
        expected = ["12"]
        self.assertListEqual(actual, expected)

        sample_1 = ["10", "%", "2"]
        actual = evaluate_remainders(sample_1)
        expected = ["0.0"]
        self.assertListEqual(actual, expected)

        sample_1 = ["10", "%", "3"]
        actual = evaluate_remainders(sample_1)
        expected = ["1.0"]
        self.assertListEqual(actual, expected)

        sample_2 = ["100", "%", "13", "%", "2"]
        actual = evaluate_remainders(sample_2)
        expected = ["1.0"]
        self.assertListEqual(actual, expected)

        sample_2 = ["100", "%", "13", "%", "2", "+", "9"]
        actual = evaluate_remainders(sample_2)
        expected = ["1.0", "+", "9"]
        self.assertListEqual(actual, expected)

        sample_2 = ["9", "+", "100", "%", "13", "%", "2"]
        actual = evaluate_remainders(sample_2)
        expected = ["9", "+", "1.0"]
        self.assertListEqual(actual, expected)

    def test_evaluate_additions(self):
        sample_1 = ["12"]
        actual = evaluate_additions(sample_1)
        expected = ["12"]
        self.assertListEqual(actual, expected)

        sample_1 = ["10", "+", "2"]
        actual = evaluate_additions(sample_1)
        expected = ["12.0"]
        self.assertListEqual(actual, expected)

        sample_1 = ["10", "+", "3"]
        actual = evaluate_additions(sample_1)
        expected = ["13.0"]
        self.assertListEqual(actual, expected)

        sample_2 = ["100", "+", "13", "+", "2"]
        actual = evaluate_additions(sample_2)
        expected = ["115.0"]
        self.assertListEqual(actual, expected)

        sample_2 = ["100", "+", "13", "+", "2", "/", "9"]
        actual = evaluate_additions(sample_2)
        expected = ["115.0", "/", "9"]
        self.assertListEqual(actual, expected)

        sample_2 = ["9", "%", "100", "+", "13", "+", "2"]
        actual = evaluate_additions(sample_2)
        expected = ["9", "%", "115.0"]
        self.assertListEqual(actual, expected)

    def test_evaluate_subtractions(self):
        sample_1 = ["12"]
        actual = evaluate_subtractions(sample_1)
        expected = ["12"]
        self.assertListEqual(actual, expected)

        sample_1 = ["10", "-", "2"]
        actual = evaluate_subtractions(sample_1)
        expected = ["8.0"]
        self.assertListEqual(actual, expected)

        sample_1 = ["10", "-", "3"]
        actual = evaluate_subtractions(sample_1)
        expected = ["7.0"]
        self.assertListEqual(actual, expected)

        sample_2 = ["100", "-", "13", "-", "2"]
        actual = evaluate_subtractions(sample_2)
        expected = ["85.0"]
        self.assertListEqual(actual, expected)

        sample_2 = ["100", "-", "13", "-", "2", "/", "9"]
        actual = evaluate_subtractions(sample_2)
        expected = ["85.0", "/", "9"]
        self.assertListEqual(actual, expected)

        sample_2 = ["9", "%", "100", "-", "13", "-", "2"]
        actual = evaluate_subtractions(sample_2)
        expected = ["9", "%", "85.0"]
        self.assertListEqual(actual, expected)

    # def test_evaluation_polarity(self):
    #     sample = "+1"
    #     actual = evaluation_polarity(sample)
    #     expected = "1"
    #     self.assertEqual(actual, expected)
    #
    #     sample = "++2"
    #     actual = evaluation_polarity(sample)
    #     expected = "2"
    #     self.assertEqual(actual, expected)
    #
    #     sample = "+++3"
    #     actual = evaluation_polarity(sample)
    #     expected = "3"
    #     self.assertEqual(actual, expected)
    #
    # def test_evaluate_parenthesis(self):
    #     self.fail()
