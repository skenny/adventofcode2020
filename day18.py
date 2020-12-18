from functools import reduce

INPUT_FILE = "day18-input"

def read_input(file):
    with open(file, "r") as fin:
        return [l.strip() for l in fin.readlines()]

def evaluate_expr(expr):
    expr = expr.replace(' ', '')

    operands = []
    operators = []

    for c in list(expr):
        if c.isdigit():
            operands.append(int(c))
        elif c in ("+", "*"):
            if len(operators) > 0 and operators.count("(") == 0:
                lhs = operands.pop(0)
                rhs = operands.pop(0)
                operator = operators.pop(0)
                operands.insert(0, evaluate_op(operator, lhs, rhs))
            operators.append(c)
        elif c == "(":
            operators.append(c)
        elif c == ")":
            nested_operators = []
            nested_operands = []
            while operators[-1] != "(":
                nested_operators.insert(0, operators.pop())
                if len(nested_operands) == 0:
                    nested_operands.insert(0, operands.pop())
                nested_operands.insert(0, operands.pop())

            # remove the "("
            operators.pop()

            result = 0
            while len(nested_operators) > 0:
                lhs = nested_operands.pop(0)
                rhs = nested_operands.pop(0)
                operator = nested_operators.pop(0)
                result = evaluate_op(operator, lhs, rhs)
                if len(nested_operators) == 0:
                    operands.append(result)
                else:
                    nested_operands.insert(0, result)

    lhs = None
    for operator in operators:
        if lhs == None:
            lhs = operands.pop(0)
        rhs = operands.pop(0)
        lhs = evaluate_op(operator, lhs, rhs)
        
    return lhs

def evaluate_op(op, lhs, rhs):
    result = 0
    if op == "+":
        result = lhs + rhs
    elif op == "*":
        result = lhs * rhs
    #print("evaluating...", lhs, op, rhs, "=", result)
    return result

def run_tests():
    for t in [
        "1 + 2 * 3 + 4 * 5 + 6", 
        "2 * 3 + (4 * 5)", 
        "5 + (8 * 3 + 9 + 3 * 4 * 3)", 
        "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 
        "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
    ]:
        print(t, "=", evaluate_expr(t))

def run(input_file):
    exprs = read_input(input_file)
    sum = reduce(lambda total, expr: total + evaluate_expr(expr), exprs, 0)
    print(sum)

run_tests()
run(INPUT_FILE)
