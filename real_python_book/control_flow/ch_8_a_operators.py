# Operators and Expressions in Python
# In Python, operators are special symbols that designate that some sort of
# computation should be performed. The values that an operator acts on
# are called operands.
# Here is an example:
a = 10
b = 20
print(a + b)
# In this case, the + operator adds the operands a and b together.
# An operand can be either a literal value or a variable that references an
# object:
a = 10
b = 20
print(a + b - 5)
# A sequence of operands and operators, like a + b - 5, is called an
# expression. Python supports many operators for combining data objects
# into expressions. These are explored below.

# Arithmetic Operators
# The following table lists the arithmetic operators supported by Python:
# Operator	Example     Meaning	        Result
# + (unary)	+a	        Unary Positive	a
#                                       In other words, it doesn’t really do
#                                       anything. It mostly exists for the
#                                       sake of completeness, to complement
#                                       Unary Negation.

# + (binary) a + b	    Addition	    Sum of a and b

# - (unary)	 -a	        Unary Negation	Value equal to a but opposite
#                                       in sign

# - (binary) a - b	    Subtraction	    b subtracted from a

# *	        a * b	    Multiplication	Product of a and b

# /	        a / b	    Division	    Quotient when a is divided by b.
#                                       The result always has type float.

# %	        a % b	    Modulo	        Remainder when a is divided by b

# //	    a // b	    Floor Division 	Quotient when a is divided by b,
#                         (also called  rounded to the next smallest whole
#                          Integer      number
#                          Division)

# **	        a ** b	    Exponentiation	a raised to the power of b

# Here are some examples of these operators in use:
a = 4
b = 3
print(+a)
print(-b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
# The result of standard division (/) is always a float, even if the dividend
# is evenly divisible by the divisor
print(type(10 / 5))
# When the result of floor division (//) is positive, it is as though the
# fractional portion is truncated off, leaving only the integer portion.
# When the result is negative, the result is rounded down to the next smallest
# (greater negative) integer:
print(10 / 4)
print(10 // 4)
print(10 // -4)
print(-10 // 4)
print(-10 // -4)

# Comparison Operators
# Operator	    Example	    Meaning	        Result
# ==	        a == b	    Equal to	    True if the value of a is equal to
#                                           the value of b
#                                           False otherwise
# !=	        a != b	    Not equal to	True if a is not equal to b
#                                           False otherwise
# <	            a < b	    Less than	    True if a is less than b
#                                           False otherwise
# <=	        a <= b	    Less than       True if a is less than or
#                            or equal to    equal to b False otherwise
# >             a > b	    Greater than	True if a is greater than b
#                                           False otherwise
# >=	        a >= b	    Greater than	True if a is greater than or
#                           or equal to     equal to b False otherwise
# Here are examples of the comparison operators in use:
a = 10
b = 20
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a > b)
print(a < b)
# Comparison operators are typically used in Boolean contexts like conditional
# and loop statements to direct program flow, as you will see later.

# Equality Comparison on Floating-Point Values
# Recall from the earlier discussion of floating-point numbers that the value
# stored internally for a float object may not be precisely what you’d think
# it would be. For that reason, it is poor practice to compare floating-point
# values for exact equality. Consider this example:
x = 1.1 + 2.2
print(x == 3.3)
# Yikes! The internal representations of the addition operands are not exactly
# equal to 1.1 and 2.2, so you cannot rely on x to compare exactly to 3.3.
# The preferred way to determine whether two floating-point values are “equal”
# is to compute whether they are close to one another, given some tolerance.
# Take a look at this example:
tolerance = 0.00001
print(abs(x - 3.3) <= tolerance)
# abs() returns absolute value. If the absolute value of the difference between
# the two numbers is less than the specified tolerance, they are close enough
# to one another to be considered equal.

# Logical Operators
# The logical operators not, or, and and modify and join together expressions
# evaluated in Boolean context to create more complex conditions.
# Logical Expressions Involving Boolean Operands
# As you have seen, some objects and expressions in Python actually are of
# Boolean type. That is, they are equal to one of the Python objects True
# or False. Consider these examples:
x = 5
print(x < 10)
print(type(x < 10))
t = x > 10
print(t)
print(type(t))
print(callable(x))
print(type(callable(x)))
t = callable(len)
print(t)
print(type(t))
# In the examples above, x < 10, callable(x), and t are all Boolean objects
# or expressions.
# Interpretation of logical expressions involving not, or, and and is
# straightforward when the operands are Boolean:
# Operator      Example         Meaning
# not           not x	        True if x is False
#                               False if x is True
#                               (Logically reverses the sense of x)
# or	        x or y	        True if either x or y is True
#                               False otherwise
# and	        x and y	        True if both x and y are True
#                               False otherwise

# “not” and Boolean Operands
x = 5
print(not x < 10)
print(not callable(x))
# “or” and Boolean Operands
print(x < 10 or callable(x))
print(x < 0 or callable(x))
# “and” and Boolean Operands
print(x < 10 or callable(x))
print(x < 10 or callable(len))

# Evaluation of Non-Boolean Values in Boolean Context
# Many objects and expressions are not equal to True or False.
# Nonetheless, they may still be evaluated in Boolean context and determined
# to be “truthy” or “falsy.”
# So what is true and what isn’t? As a philosophical question, that is outside
# the scope of this tutorial!
# But in Python, it is well-defined.

# All the following are considered false
# when evaluated in Boolean context:
# The Boolean value False
# Any value that is numerically zero (0, 0.0, 0.0+0.0j)
# An empty string
# An object of a built-in composite data type which is empty
# The special value denoted by the Python keyword None

# Virtually any other object built into Python is regarded as true.
# You can determine the “truthiness” of an object or expression with the
# built-in bool() function. bool() returns True if its argument is truthy and
# False if it is falsy.

# Compound Logical Expressions and Short-Circuit Evaluation
# So far, you have seen expressions with only a single or or and operator
# and two operands:
# x or y
# x and y
# Multiple logical operators and operands can be strung together to form
# compound logical expressions.

# Compound “or” Expressions
# Consider the following expression:
# x1 or x2 or x3 or … xn
# This expression is true if any of the xi are true.
# In an expression like this, Python uses a methodology called short-circuit
# evaluation, also called McCarthy evaluation in honor of computer scientist
# John McCarthy. The xi operands are evaluated in order from left to right.
# As soon as one is found to be true, the entire expression is known
# to be true. At that point, Python stops and no more terms are evaluated.
# The value of the entire expression is that of the xi that
# terminated evaluation.
# To help demonstrate short-circuit evaluation, suppose that you have a simple
# “identity” function f() that behaves as follows:
# f() takes a single argument.
# It displays the argument to the console.
# It returns the argument passed to it as its return value.
# Because f() simply returns the argument passed to it, we can make the
# expression f(arg) be truthy or falsy as needed by specifying a value for
# arg that is appropriately truthy or falsy. Additionally, f() displays its
# argument to the console, which visually confirms whether or
# not it was called.
# Now, consider the following compound logical expression:
# >>> f(0) or f(False) or f(1) or f(2) or f(3)
# -> f(0) = 0
# -> f(False) = False
# -> f(1) = 1
# 1
# The interpreter first evaluates f(0), which is 0. A numeric value of 0
# is false. The expression is not true yet, so evaluation proceeds left to
# right. The next operand, f(False), returns False.
# That is also false, so evaluation continues.
# Next up is f(1). That evaluates to 1, which is true. At that point,
# the interpreter stops because it now knows the entire expression to be true.
# 1 is returned as the value of the expression, and the remaining operands,
# f(2) and f(3), are never evaluated. You can see from the display that the
# f(2) and f(3) calls do not occur.

# Compound “and” Expressions
# A similar situation exists in an expression with multiple and operators:
# x1 and x2 and x3 and … xn
# This expression is true if all the xi are true.
# In this case, short-circuit evaluation dictates that the interpreter stop
# evaluating as soon as any operand is found to be false, because at that
# point the entire expression is known to be false. Once that is the case,
# no more operands are evaluated, and the falsy operand that terminated
# evaluation is returned as the value of the expression:
# >>> f(1) and f(False) and f(2) and f(3)
# -> f(1) = 1
# -> f(False) = False
# False
# >>> f(1) and f(0.0) and f(2) and f(3)
# -> f(1) = 1
# -> f(0.0) = 0.0
# 0.0
# In both examples above, evaluation stops at the first term that is
# false—f(False) in the first case, f(0.0) in the second case—and neither
# the f(2) nor f(3) call occurs. False and 0.0, respectively, are returned as
# the value of the expression.
# If all the operands are truthy, they all get evaluated and the last
# (rightmost) one is returned as the value of the expression:
# >>> f(1) and f(2.2) and f('bar')
# -> f(1) = 1
# -> f(2.2) = 2.2
# -> f(bar) = bar
# 'bar'

# Idioms That Exploit Short-Circuit Evaluation
# There are some common idiomatic patterns that exploit short-circuit
# evaluation for conciseness of expression.
# Avoiding an Exception
# Suppose you have defined two variables a and b, and you want to
# know whether (b / a) > 0:
# >>> a = 3
# >>> b = 1
# >>> (b / a) > 0
# True
# But you need to account for the possibility that a might be 0,
# in which case the interpreter will raise an exception:
# >>> a = 0
# >>> b = 1
# >>> (b / a) > 0
# Traceback (most recent call last):
#   File "<pyshell#2>", line 1, in <module>
#     (b / a) > 0
# ZeroDivisionError: division by zero
# You can avoid an error with an expression like this:
# >>> a = 0
# >>> b = 1
# >>> a != 0 and (b / a) > 0
# False
# When a is 0, a != 0 is false. Short-circuit evaluation ensures that
# evaluation stops at that point. (b / a) is not evaluated,
# and no error is raised.
# If fact, you can be even more concise than that.
# When a is 0, the expression a by itself is falsy.
# There is no need for the explicit comparison a != 0:
# >>> a = 0
# >>> b = 1
# >>> a and (b / a) > 0
# 0

# Selecting a Default Value
# Another idiom involves selecting a default value when a specified value is
# zero or empty. For example, suppose you want to assign a variable s to the
# value contained in another variable called string. But if string is empty,
# you want to supply a default value.
# Here is a concise way of expressing this using short-circuit evaluation:
# s = string or '<default_value>'
# If string is non-empty, it is truthy, and the expression string or
# '<default_value>' will be true at that point. Evaluation stops, and the
# value of string is returned and assigned to s:
string = 'foo bar'
s = string or '<default_value>'
print(s)
# On the other hand, if string is an empty string, it is falsy.
# Evaluation of string or '<default_value>' continues to the next operand,
# '<default_value>', which is returned and assigned to s:
string = ''
s = string or '<default_value>'
print(s)

# Chained Comparisons
# Comparison operators can be chained together to arbitrary length.
# For example, the following expressions are nearly equivalent:
# x < y <= z
# x < y and y <= z
# They will both evaluate to the same Boolean value.
# The subtle difference between the two is that in the chained comparison
# x < y <= z, y is evaluated only once.
# The longer expression x < y and y <= z will cause y to be evaluated twice.
# Note: In cases where y is a static value, this will not be a
# significant distinction. But consider these expressions:
# x < f() <= z
# x < f() and f() <= z
# If f() is a function that causes program data to be modified,
# the difference between its being called once in the first case and twice in
# the second case may be important.
print(1 < 2 < 3)
print(1 < 2 and 2 < 3)
# More generally, if op1, op2, …, opn are comparison operators,
# then the following have the same Boolean value:
# x1 op1 x2 op2 x3 … xn-1 opn xn
# x1 op1 x2 and x2 op2 x3 and … xn-1 opn xn
# In the former case, each xi is only evaluated once.
# In the latter case, each will be evaluated twice except the first and last,
# unless short-circuit evaluation causes premature termination.

# Bitwise Operators
# Bitwise operators treat operands as sequences of binary digits and operate on
# them bit by bit. The following operators are supported:
# Operator      Example         Meaning         Result
# &	            a & b           bitwise AND     Each bit position in the result
#                                               is the logical AND of the bits
#                                               in the corresponding position
#                                               of the operands. (1 if both are
#                                               1, otherwise 0.)
# |             a | b	        bitwise OR	    Each bit position in the result
#                                               is the logical OR of the bits
#                                               in the corresponding position
#                                               of the operands. (1 if either
#                                               is 1, otherwise 0.)
# ~             ~a              bitwise         Each bit position in the result
#                               negation        is the logical negation of the
#                                               bit in the corresponding
#                                               position of the operand.
#                                               (1 if 0, 0 if 1.)
# ^             a ^ b           bitwise XOR     Each bit position in the result
#                               (exclusive OR)  is the logical XOR of the bits
#                                               in the corresponding position
#                                               of the operands. (1 if the bits
#                                               in the operands are different,
#                                               0 if they are the same.)
# >>            a >> n	        Shift right	    Each bit is shifted right
#                               n places        n places.
# <<            a << n	        Shift left	    Each bit is shifted left
#                               n places        n places.
# Here are some examples:
print('0b{:04b}'.format(0b1100 & 0b1010))
# '0b1000'
print('0b{:04b}'.format(0b1100 | 0b1010))
# '0b1110'
print('0b{:04b}'.format(0b1100 ^ 0b1010))
# '0b0110'
print('0b{:04b}'.format(0b1100 >> 2))
# '0b0011'
print('0b{:04b}'.format(0b0011 << 2))
# '0b1100'
# Note: The purpose of the '0b{:04b}'.format() is to format the numeric output
# of the bitwise operations, to make them easier to read.

# Identity Operators
# Python provides two operators, is and is not, that determine whether the
# given operands have the same identity—that is, refer to the same object.
# This is not the same thing as equality, which means the two operands refer
# to objects that contain the same data but are not necessarily
# the same object.
# Here is an example of two object that are equal but not identical:
x = 1001
y = 1000 + 1
print(x, y)
print(x == y)
print(x is y)

z = x == y
print(z is True)

# Operator Precedence
# Consider this expression:
# >>> 20 + 4 * 10
# 60
# There is ambiguity here. Should Python perform the addition 20 + 4 first and
# then multiply the sum by 10? Or should the multiplication 4 * 10 be
# performed first, and the addition of 20 second?
# Clearly, since the result is 60, Python has chosen the latter;
# if it had chosen the former, the result would be 240. This is standard
# algebraic procedure, found universally in virtually all programming languages
# All operators that the language supports are assigned a precedence.
# In an expression, all operators of highest precedence are performed first.
# Once those results are obtained, operators of the next highest precedence are
# performed. So it continues, until the expression is fully evaluated.
# Any operators of equal precedence are performed in left-to-right order.
# Here is the order of precedence of the Python operators you have seen so far,
# from lowest to highest:
#  	                    Operator                Description
# lowest precedence	    or	                    Boolean OR
#                       and	                    Boolean AND
#                       not	                    Boolean NOT
#                       ==, !=, <, <=,          comparisons, identity
#                       >, >=, is, is not
#                       |                       bitwise OR
#                       ^	                    bitwise XOR
#                       &	                    bitwise AND
#                       <<, >>	                bit shifts
#                       +, -	                addition, subtraction
#                       *, /, //, %	            multiplication, division,
#                                               floor division, modulo
#                       +x, -x, ~x              unary positive, unary negation,
#                                               bitwise negation
# highest precedence	**	                    exponentiation
# Operators at the top of the table have the lowest precedence, and those at
# the bottom of the table have the highest.
# Any operators in the same row of the table have equal precedence.
# It is clear why multiplication is performed first in the example above:
# multiplication has a higher precedence than addition.
# Similarly, in the example below, 3 is raised to the power of 4 first,
# which equals 81, and then the multiplications are carried out in order from
# left to right (2 * 81 * 5 = 810):
print(2 * 3 ** 4 * 5)
# Operator precedence can be overridden using parentheses.
# Expressions in parentheses are always performed first, before expressions
# that are not parenthesized. Thus, the following happens:
print(20 + 4 * 10)
print((20 + 4) * 10)
print(2 * 3 ** 4 * 5)
print(2 * 3 ** (4 * 5))
# In the first example, 20 + 4 is computed first, then the result is
# multiplied by 10. In the second example, 4 * 5 is calculated first,
# then 3 is raised to that power, then the result is multiplied by 2.
# There is nothing wrong with making liberal use of parentheses,
# even when they aren’t necessary to change the order of evaluation.
# In fact, it is considered good practice, because it can make the code
# more readable, and it relieves the reader of having to recall operator
# precedence from memory. Consider the following:
# (a < 10) and (b > 30)
# Here the parentheses are fully unnecessary, as the comparison operators have
# higher precedence than and does and would have been performed first anyhow.
# But some might consider the intent of the parenthesized version more
# immediately obvious than this version without parentheses:
# a < 10 and b > 30
# On the other hand, there are probably those who would prefer the latter;
# it’s a matter of personal preference.
# The point is, you can always use parentheses if you feel it makes the code
# more readable, even if they aren’t necessary to change the order
# of evaluation.

# Augmented Assignment Operators
# Python supports a shorthand augmented assignment notation for these
# arithmetic and bitwise operators:
# Arithmetic	Bitwise
# +           &
# -           |
# *           ^
# /           >>
# %           <<
# //
# **
# For these operators, the following are equivalent:
# x <op>= y
# x = x <op> y
# a += 5 is equivalent to a = a + 5
