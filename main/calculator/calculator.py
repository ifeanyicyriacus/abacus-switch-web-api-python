def generate_expression_list(expression: str) -> list:
    # handle polarity of number, at the beginning, the last non-operator-operator eval("----2")

    expression = expression.replace(" ", "")
    new_list = []
    temp = ""
    for character in expression:
        if character not in ["%", "*", "/", "+", "-"]:
            temp += character
            continue
        elif character == "*":
            new_list.extend([temp, "*"])
        elif character == "/":
            new_list.extend([temp, "/"])
        elif character == "%":
            new_list.extend([temp, "%"])
        elif character == "+":
            new_list.extend([temp, "+"])
        elif character == "-":
            new_list.extend([temp, "-"])
        temp = ""
    new_list.append(temp)
    return new_list


def resolved_expression(expression_list, index, operation) -> list:
    new_element = float(0)
    if operation == "*":
        new_element = float(expression_list[index - 1]) * float(expression_list[index + 1])
    elif operation == "/":
        new_element = float(expression_list[index - 1]) / float(expression_list[index + 1])
    elif operation == "%":
        new_element = float(expression_list[index - 1]) % float(expression_list[index + 1])
    elif operation == "+":
        new_element = float(expression_list[index - 1]) + float(expression_list[index + 1])
    elif operation == "-":
        new_element = float(expression_list[index - 1]) - float(expression_list[index + 1])

    expression_list = expression_list[:index - 1] + [str(new_element)] + expression_list[index + 2:]
    return expression_list


def evaluate_multiplications(expression_list: list) -> list:
    for index, element in enumerate(expression_list):
        if element == "*" and len(expression_list) > 1:
            expression_list = resolved_expression(expression_list=expression_list, index=index, operation="*")
            return evaluate_multiplications(expression_list)
    return expression_list


def evaluate_divisions(expression_list) -> list:
    for index, element in enumerate(expression_list):
        if element == "/" and len(expression_list) > 1:
            expression_list = resolved_expression(expression_list=expression_list, index=index, operation="/")
            return evaluate_divisions(expression_list)
    return expression_list


def evaluate_remainders(expression_list: list) -> list:
    for index, element in enumerate(expression_list):
        if element == "%" and len(expression_list) > 1:
            expression_list = resolved_expression(expression_list=expression_list, index=index, operation="%")
            return evaluate_remainders(expression_list)
    return expression_list


def evaluate_additions(expression_list: list) -> list:
    for index, element in enumerate(expression_list):
        if element == "+" and len(expression_list) > 1:
            expression_list = resolved_expression(expression_list=expression_list, index=index, operation="+")
            return evaluate_additions(expression_list)
    return expression_list


def evaluate_subtractions(expression_list: list) -> list:
    for index, element in enumerate(expression_list):
        if element == "-" and len(expression_list) > 1:
            expression_list = resolved_expression(expression_list=expression_list, index=index, operation="-")
            return evaluate_subtractions(expression_list)
    return expression_list


def calculate(expression: str) -> float:
    expression_list = generate_expression_list(expression)
    # parenthesis priority : a recursive function that calls this calculate function
    expression_list = evaluate_multiplications(expression_list)
    expression_list = evaluate_divisions(expression_list)
    expression_list = evaluate_remainders(expression_list)
    expression_list = evaluate_additions(expression_list)
    result = evaluate_subtractions(expression_list)
    return float(result[0])
