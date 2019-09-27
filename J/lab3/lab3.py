import operator
from pythonds.basic import Stack

def toPostfix(infix):
    stack = []
    postfix = ''

    for c in infix:
        if isOperand(c):
            postfix += c
        else:
            if isLeftParenthesis(c):
                stack.append(c)
            elif isRightParenthesis(c):
                operator = stack.pop()
                while not isLeftParenthesis(operator):
                    postfix += operator
                    operator = stack.pop()              
            else:
                while (not isEmpty(stack)) and hasLessOrEqualPriority(c,peek(stack)):
                    postfix += stack.pop()
                stack.append(c)
    while (not isEmpty(stack)):
        postfix += stack.pop()
    return postfix

def calc(expr):
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = [0]
    for token in expr.split(" "):
        if token in OPERATORS:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(OPERATORS[token](op1,op2))
        elif token:
            stack.append(float(token))
    return stack.pop()

expr = input()
expr = calc(toPostfix(expr))
print(expr)
