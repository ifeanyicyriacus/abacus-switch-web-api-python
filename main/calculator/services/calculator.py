def replace_math_symbol_with_language_operator(expression):
    expression = expression.replace(" ", "")
    expression = expression.replace("x", "*")
    expression = expression.replace("÷", "/")
    expression = expression.replace("^", "**")  # consider where it is placed
    expression = expression.replace("mod", "%")
    return expression

def evaluation_polarity(expression:str) -> str:
    for index, char in enumerate(expression):
        if len(expression) > index + 1 and char in ["+", "-"] and char == expression[index + 1]:
            expression = expression[:index] + "+" + expression[index + 2:]
            return evaluation_polarity(expression)
        elif len(expression) > index + 1 and char in ["+", "-"] and expression[index + 1] in ["+", "-"] and char != expression[index + 1]:
            expression = expression[:index] + "-" + expression[index + 2:]
            return evaluation_polarity(expression)
    return expression

def generate_expression_list(expression: str) -> list:
    # handle polarity of number, at the beginning, the last non-operator-operator eval("----2")

    expression = replace_math_symbol_with_language_operator(expression)

    new_list = []
    temp = ""

    for character in expression:
        if character in {"%", "*", "/", "+", "-"}:
            new_list.extend([temp, character])
            temp = ""
        else:
            temp += character
    new_list.append(temp)
    return new_list


def __resolved_expression(expression_list, index, operation) -> list:
    new_element = float(0)

    a = float(expression_list[index - 1])
    b = float(expression_list[index + 1])

    if operation == "*":
        new_element = a * b
    elif operation == "/":
        new_element = a / b
    elif operation == "%":
        new_element = a % b
    elif operation == "+":
        new_element = a + b
    elif operation == "-":
        new_element = a - b

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


def calculate(expression: str) -> float:
    expression_list = generate_expression_list(expression)
    # parenthesis priority : a recursive function that calls this calculate function

    expression_list = evaluate_multiplications(expression_list)
    expression_list = evaluate_divisions(expression_list)
    expression_list = evaluate_remainders(expression_list)
    expression_list = evaluate_additions(expression_list)
    result = evaluate_subtractions(expression_list)
    return float(result[0])
