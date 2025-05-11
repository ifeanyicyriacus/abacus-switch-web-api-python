import math


def replace_math_symbol_with_language_operator(expression):
    expression = expression.replace(" ", "")
    expression = expression.replace("x", "*")
    expression = expression.replace("÷", "/")
    expression = expression.replace("mod", "%")
    return expression


def evaluation_polarity(expression: str) -> str:
    for index, char in enumerate(expression):
        if len(expression) > index + 1 and char in ["+", "-"] and char == expression[index + 1]:
            expression = expression[:index] + "+" + expression[index + 2:]
            return evaluation_polarity(expression)
        elif len(expression) > index + 1 and char in ["+", "-"] and expression[index + 1] in ["+", "-"] and char != \
                expression[index + 1]:
            expression = expression[:index] + "-" + expression[index + 2:]
            return evaluation_polarity(expression)
    return expression


def generate_expression_list(expression: str) -> list:
    # handle polarity of number, at the beginning, the last non-operator-operator eval("----2")

    expression = replace_math_symbol_with_language_operator(expression)

    new_list = []
    temp = ""

    for character in expression:
        if character in {"%", "*", "/", "+", "-", "!", "^", "(", ")", "√"}:
            new_list.extend([temp, character])
            temp = ""
        else:
            temp += character
    new_list.append(temp)
    return new_list


def _calculate_factorials(a: int) -> int:
    result = a
    while a > 1:
        a = a - 1
        return result * _calculate_factorials(a)
    return result


def __resolved_expression(expression_list:[str], index:int, operation:str) -> [str]:
    new_element = float(0)

    match operation:
        case "!":
            a = int(expression_list[index - 1])
            new_element = float(_calculate_factorials(int(a)))
            expression_list = expression_list[:index - 1] + [str(new_element)] + expression_list[index + 1:]
            return expression_list
        case "√":
            b = float(expression_list[index + 1])
            new_element = math.sqrt(b)
            expression_list = expression_list[:index] + [str(new_element)] + expression_list[index + 2:]
            return expression_list

    a = float(expression_list[index - 1])
    b = float(expression_list[index + 1])

    match operation:
        case "*":
            new_element = a * b
        case "/":
            new_element = a / b
        case "%":
            new_element = a % b
        case "+":
            new_element = a + b
        case "-":
            new_element = a - b
        case "^":
            new_element = a ** b

    expression_list = expression_list[:index - 1] + [str(new_element)] + expression_list[index + 2:]
    return expression_list


def _evaluate_operation(expression_list: list[str], operator: str) -> list[str]:
    for index, element in enumerate(expression_list):
        if element == operator and len(expression_list) > 1:
            expression_list = __resolved_expression(expression_list=expression_list, index=index, operation=operator)
            return _evaluate_operation(expression_list, operator)
    return expression_list


def evaluate_multiplications(expression_list: list[str]) -> list[str]:
    return _evaluate_operation(expression_list, "*")


def evaluate_divisions(expression_list) -> list:
    return _evaluate_operation(expression_list, "/")


def evaluate_remainders(expression_list: list) -> list:
    return _evaluate_operation(expression_list, "%")


def evaluate_additions(expression_list: list) -> list:
    return _evaluate_operation(expression_list, "+")


def evaluate_subtractions(expression_list: list) -> list:
    return _evaluate_operation(expression_list, "-")

def evaluate_exponents(expression_list: list) -> list:
    return _evaluate_operation(expression_list, "^")

def evaluate_factorials(expression_list: list) -> list:
    return _evaluate_operation(expression_list, "!")

def evaluate_square_roots(expression_list: list) -> list:
    return _evaluate_operation(expression_list, "√")


def calculate(expression: str) -> float:
    expression_list = generate_expression_list(expression)
    # parenthesis priority : a recursive function that calls this calculate function

    expression_list = evaluate_multiplications(expression_list)
    expression_list = evaluate_divisions(expression_list)
    expression_list = evaluate_remainders(expression_list)
    expression_list = evaluate_additions(expression_list)
    result = evaluate_factorials(expression_list)


    # parenthesis>factorial>exponents>x/%+-
    return float(result[0])
