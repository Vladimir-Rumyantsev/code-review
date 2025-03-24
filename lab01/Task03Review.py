# Recur22. Вывести значение целочисленного выражения, заданного в виде строки S.
# Выражение определяется следующим образом (функция M возвращает максимальный из своих параметров,
# а функция m — минимальный):
# <выражение> ::= <цифра> | M(<параметры>) | m(<параметры>)
# <параметры> ::= <выражение> | <выражение> , <параметры>


def evaluate_expression(expr: str) -> int:
    expr = expr.strip()
    if not expr:
        raise ValueError("Empty expression")

    if expr.isdigit():
        return int(expr)

    if expr.startswith('M(') or expr.startswith('m('):
        if not expr.endswith(")"):
            raise ValueError("Missing closing parenthesis")

        func = max if expr.startswith("M(") else min
        params_str = expr[2:-1].strip()

        param_list = []
        bracket_count = 0
        current_param = []

        for char in params_str:
            # if char == ',' and bracket_count == 0:
            #     param_list.append(current_param.strip())
            #     current_param = ''
            # else:
            #     if char == '(':
            #         bracket_count += 1
            #     elif char == ')':
            #         bracket_count -= 1
            #     current_param += char

            if char == "," and bracket_count == 0:
                param_list.append("".join(current_param).strip())
                current_param = []
            else:
                if char == "(":
                    bracket_count += 1
                elif char == ")":
                    bracket_count -= 1
                current_param.append(char)

        # if current_param:
        #     param_list.append(current_param.strip())
        # values = [evaluate_expression(param) for param in param_list]
        # return func(values)

        if current_param:
            param_list.append("".join(current_param).strip())

        if not param_list:
            raise ValueError("Function has no parameters")

            # Рекурсивное вычисление параметров
        values = [evaluate_expression(p) for p in param_list]
        return func(values)


# print(evaluate_expression("M(1, 2, 3)"))              # 3
# print(evaluate_expression("m(5, 3, 8, M(2, 6))"))     # 3
# print(evaluate_expression("M(1, m(2, 3), 4)"))        # 4
# print(evaluate_expression("m(M(1, 2), 3, M(4, 5))"))  # 2
# print(evaluate_expression("M(10, m(20, 30), 25)"))    # 25
# print(evaluate_expression("m(M(1, 5), M(2, 3), 4)"))  # 3
# print(evaluate_expression("M(m(1, 2), m(3, 4), 0)"))  # 3

if __name__ == "__main__":
    try:
        user_input = input("Введите выражение: ")
        result = evaluate_expression(expr=user_input)
        print(f"Результат: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
