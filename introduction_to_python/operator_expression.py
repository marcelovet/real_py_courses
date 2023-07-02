# https://realpython.com/python-operators-expressions/
# Em Python, os operadores são símbolos especiais que indicam que algum tipo de
# computação deve ser realizado. Os valores sobre os quais um operador atua são
# chamados de operandos.
a = 10
b = 20

# arithmetic operators
print(-a, 'unary positive')
print(+a, 'unary negativ')
print(a + b, 'addition')
print(a - b, 'subtraction')
print(a * b, 'multiplication')
print(a / b, 'division')
print(a // b, 'integer division')
print(a % b, 'modulo')
print(a ** b, 'exponentiation')

# comparison operators
print(a == b, 'equal to')
print(a != b, 'not equal to')
print(a > b, 'greather than')
print(a < b, 'less than')
print(a >= b, 'greather than or equal to')
print(a <= b, 'less than or equal to')

# because og how floating points are stored internally, its poor practice
# to compare then
x = 1.1 + 2.2
print(x == 3.3)
# the preferred way is to comparing than given some tolerance
tolerance = 0.00001
print(abs(x - 3.3) <= tolerance)

# logical operators
print(not (a == b), 'not x, given that x is True or False')
print((a > b) and (a < b), 'y and x, given that x and y is True or False')
print((a > b) or (a < b), 'y or x, given that x and y is True or False')

# falsy values (evaluates to False in boolean context)
# The Boolean value False
# Any value that is numerically zero (0, 0.0, 0.0+0.0j)
# An empty string
# An object of a built-in composite data type which is empty
# The special value denoted by the Python keyword None

# Compound Logical Expressions and Short-Circuit Evaluation
# Python uses a methodology called short-circuit evaluation, also called McCarthy
# evaluation in honor of computer scientist John McCarthy. The xi operands are
# evaluated in order from left to right. As soon as one is found to be the
# circuit break (true for the operator or and false to the operator and),
# the entire expression is known to be true or false. At that point, Python
# stops and no more terms are evaluated. The value of the entire expression is
# that of the xi that terminated evaluation.


def foo(val):
    print(val, end=" ")
    return val


# compund or
foo(0) or foo(False) or foo(True) or foo("not evaluated")
print()
# compund and
foo(0) and foo(False) and foo(True) and foo("not evaluated")
print()

# Idioms That Exploit Short-Circuit Evaluation

# avoid raise an exception ZeroDivisionError
a = 0
b = 1
print(a != 0 and (b / a) > 0)
# 0 is a falsy, so we can rewrite this expression
print(a and (b / a) > 0)

# Selecting a Default Value
# assign a variable to the value contained in another variable, but if that is
# empty than use a default value
for i in range(2):
    string = 'foo'
    if i == 1:
        string = ''
    s = string or "<default value>"
    print(s)

print(1 < 2 < 3)
print(1 < 2 and 2 < 3)

# identity operator is take id into account
x = 2
y = 2
print(x is y)
# int from -5 to 256 are stored in cache and results in the
# same object reference
x = 2
y = 2
print(x is y)
x = 3000
y = 2999 + 1
print(x is y)
# works only if executing in a console
# Python compiler optimize identical literals when compiled in the same code
# object.
