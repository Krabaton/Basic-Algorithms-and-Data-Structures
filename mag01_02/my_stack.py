def infix_to_postfix(exp: str) -> str:
    priority = {'+': 1, "-": 1, "*": 2, "/": 2}
    output = []
    stack = []
    for token in exp.split():
        if token.isdigit():
            output.append(token)
        elif token in priority:
            while stack and priority[stack[-1]] >= priority[token]:
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return ' '.join(output)


def my_eval(expr: str):
    stack = []
    for token in expr.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a / b)
    return stack.pop()


expression = "3 + 4 * 2"
postfix_exrp = infix_to_postfix(expression)
print(postfix_exrp)
print(my_eval(postfix_exrp))
