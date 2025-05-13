import math


def replace_math_symbol_with_language_operator(expression: [str]) -> [str]:
    expression = expression.replace(" ", "")
    expression = expression.replace("x", "*")
    expression = expression.replace("÷", "/")
    expression = expression.replace("mod", "%")
    return expression


def evaluate_polarity(expression: str) -> str:
    for index, char in enumerate(expression):
        if len(expression) > index + 1 and char in ["+", "-"] and char == expression[index + 1]:
            expression = expression[:index] + "+" + expression[index + 2:]
            return evaluate_polarity(expression)
        elif len(expression) > index + 1 and char in ["+", "-"] and expression[index + 1] in ["+", "-"] and char != \
                expression[index + 1]:
            expression = expression[:index] + "-" + expression[index + 2:]
            return evaluate_polarity(expression)
    return expression


def generate_expression_list(expression: str) -> list:
    # handle polarity of number, at the beginning, the last non-operator-operator eval("----2")
    new_list = []
    temp = ""

    for character in expression:
        if character in ["%", "*", "/", "+", "-", "!", "^", "(", ")", "√"]:
            new_list.extend([temp, character])
            temp = ""
        else:
            temp += character
    new_list.append(temp)
    new_list = [x for x in new_list if x != ""]
    if new_list[0] in ["+", "-"] and new_list[1] not in ["%", "*", "/", "+", "-", "!", "^", "(", ")", "√"]:
        new_list[1] = new_list[0] + new_list[1]
        new_list.pop(0)
    return new_list


def _calculate_factorials(a: int) -> int:
    result = a
    while a > 1:
        a = a - 1
        return result * _calculate_factorials(a)
    return result


def __resolved_expression(expression_list: [str], index: int, operation: str) -> [str]:
    new_element = float(0)

    match operation:
        case "!":
            return _resolve_factorial(expression_list, index)
        case "√":
            return _resolve_square_root(expression_list, index)
        case ")":
            return _resolve_parenthesis(expression_list, index)

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


def _resolve_factorial(expression_list: [str], index: int) -> [int]:
    a = int(expression_list[index - 1])
    new_element = float(_calculate_factorials(int(a)))
    expression_list = expression_list[:index - 1] + [str(new_element)] + expression_list[index + 1:]
    return expression_list


def _resolve_square_root(expression_list: [str], index: int) -> [str]:
    b = float(expression_list[index + 1])
    new_element = math.sqrt(b)
    expression_list = expression_list[:index] + [str(new_element)] + expression_list[index + 2:]
    return expression_list


def _resolve_parenthesis(expression_list: [str], index: int) -> [str]:
    close_parenthesis_index = index
    open_parenthesis_index = _get_index_of_last_opening_parenthesis_before_index(expression_list,
                                                                                 close_parenthesis_index)
    new_expression = ""
    for element in expression_list[(open_parenthesis_index + 1): close_parenthesis_index]:
        new_expression += element
    new_element = calculate(new_expression)
    expression_list = (expression_list[:open_parenthesis_index] +
                       [str(new_element)] +
                       expression_list[(close_parenthesis_index + 1):])
    return expression_list


def _get_index_of_last_opening_parenthesis_before_index(expression_list: [str], closing_parenthesis_index: int) -> int:
    sub_expression_list = expression_list[:closing_parenthesis_index]
    sub_expression_list.reverse()
    index_of_open_parenthesis_on_reverse_list = sub_expression_list.index("(")
    INDEX_OFF_BY_ONE = 1
    return len(sub_expression_list) - index_of_open_parenthesis_on_reverse_list - INDEX_OFF_BY_ONE


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


def evaluate_parenthesis(expression_list: list) -> [str]:
    return _evaluate_operation(expression_list, ")")


def calculate(expression: str) -> float:
    expression = replace_math_symbol_with_language_operator(expression)
    expression = evaluate_polarity(expression)
    expression_list = generate_expression_list(expression)
    expression_list = evaluate_parenthesis(expression_list)
    expression_list = evaluate_factorials(expression_list)
    expression_list = evaluate_square_roots(expression_list)
    expression_list = evaluate_exponents(expression_list)
    expression_list = evaluate_multiplications(expression_list)
    expression_list = evaluate_divisions(expression_list)
    expression_list = evaluate_remainders(expression_list)
    expression_list = evaluate_additions(expression_list)
    result = evaluate_subtractions(expression_list)
    return float(result[0])

# TODO i could show workings/ break down
