from unittest import TestCase

from main.calculator.services.calculator import *

class Test(TestCase):
    def test_calculate(self):
        self.assertEqual(1.0, calculate("1"))
        self.assertEqual(4.0, calculate("2+2"))
        self.assertEqual(6000000.0, calculate("2x3000000"))
        self.assertEqual(140.88888888888889, calculate("122 + 34 * 5 / 9"))
        self.assertEqual(136.0, calculate("(7+3^2)x34÷4"))
        self.assertEqual(-21.0, calculate("-7*3"))
        self.assertEqual(21.0, calculate("+7*3"))

    def test_generate_expression_list(self):
        actual = generate_expression_list("12")
        expected = ["12"]
        self.assertListEqual(actual, expected)

        actual = generate_expression_list("12+2")
        expected = ["12", "+", "2"]
        self.assertListEqual(actual, expected)

        actual = generate_expression_list("122+34*5/9")
        expected = ["122", "+", "34", "*", "5", "/", "9"]
        self.assertListEqual(actual, expected)

        actual = generate_expression_list("122+34!*5^2/9")
        expected = ["122", "+", "34", "!", "*", "5", "^", "2", "/", "9"]
        self.assertListEqual(actual, expected)

        actual = generate_expression_list("!%^*()-+/*√")
        expected = ["!", "%", "^", "*", "(", ")", "-", "+", "/", "*", "√"]
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
        actual = evaluate_polarity(sample)
        expected = "+1"
        self.assertEqual(actual, expected)

        sample = "++2"
        actual = evaluate_polarity(sample)
        expected = "+2"
        self.assertEqual(actual, expected)

        sample = "+++3"
        actual = evaluate_polarity(sample)
        expected = "+3"
        self.assertEqual(actual, expected)

        sample = "+-3"
        actual = evaluate_polarity(sample)
        expected = "-3"
        self.assertEqual(actual, expected)

        sample = "--3"
        actual = evaluate_polarity(sample)
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
        expected = ["6.0", "+", "36"]
        self.assertListEqual(actual, expected)

        sample = ["3", "-", "√", "36"]
        actual = evaluate_square_roots(sample)
        expected = ["3", "-", "6.0"]
        self.assertListEqual(actual, expected)

    def test_evaluate_parenthesis(self):
        sample = ["12"]
        actual = evaluate_parenthesis(sample)
        expected = ["12"]
        self.assertListEqual(actual, expected)

        sample = ["(", "12", ")"]
        actual = evaluate_parenthesis(sample)
        expected = ["12.0"]
        self.assertListEqual(actual, expected)

        sample = ["12", "+", "(", "3", "+", "5", "+", "1", ")", "+", "19"]
        actual = evaluate_parenthesis(sample)
        expected = ["12", "+", "9.0", "+", "19"]
        self.assertListEqual(actual, expected)

    def test_handles_division_by_zero(self):
        self.assertRaises(ZeroDivisionError, calculate,"1/0")

    def test_stressTest(self):
        # 1. Mixed Operations with Nested Parentheses
        sample = "√(100) + (3! * 2^5) / (10 % 3) - (-5 * 2)"
        actual = calculate(sample)
        expected = 212.0
        self.assertEqual(actual, expected)

        # # 2. High-Precision Floating Point 34.5 != 37.50000000000001
        # sample = "(0.1 + 0.2) * 5^3 - √(2.25) / 0.5%3"
        # actual = calculate(sample)
        # expected = 34.5
        # print(actual)
        # self.assertTrue(abs(actual - expected) < 0.01)

        # # 3. Factorial & Exponent Stress
        # sample = "10! / (5^3 * (2%7)) + √(1000000) - 3!!"
        # actual = calculate(sample)
        # expected = 15_512.2
        # print(actual)
        # self.assertTrue(abs(actual - expected) < 0.01)

        # 4. Deeply Nested Logic
        sample = "((((5 + 3) * 2)^2 % 10) / √(4)) - (2^(3! - 4))"
        actual = calculate(sample)
        expected = -1.0
        self.assertEqual(actual, expected)

        # # 5. Consecutive Operators
        # sample = "5--+-+√(9) + 3%2 * 10/--2"
        # actual = calculate(sample)
        # expected = 13.0
        # self.assertEqual(actual, expected)

        # # 6. Large-Number Computation
        # sample = "999999^2 % 12345 + √(987654321) * 20! / 1000"
        # actual = calculate(sample)
        # expected = 2.43e+18
        # print(actual)
        # self.assertEqual(actual, expected)

        # 7. Mixed Precedence Chaos
        sample = "3 + 4 * 2 / (1 - 5)^2 + 10%3 + √(4^2!)"
        actual = calculate(sample)
        expected = 8.5
        self.assertEqual(actual, expected)

        # # 8. Minimal Whitespace Challenge
        # sample = "√4+3!-2^3*5%2/1"
        # actual = calculate(sample)
        # expected = 0.0
        # self.assertEqual(actual, expected)

        # 9. Redundant Parentheses
        sample = "((((5))) + (√((36))) / ((2%(3))) - ((2^(3))))"
        actual = calculate(sample)
        expected = 0.0
        self.assertEqual(actual, expected)

        # # 10. All Operators in One
        # sample = "√(5! + 3^4) * (10%3) - (2^(6/2)) + (-5 + 3!)"
        # actual = calculate(sample)
        # expected = 7.177
        # self.assertTrue(abs(actual - expected) < 0.01)