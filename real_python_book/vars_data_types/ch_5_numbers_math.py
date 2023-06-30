# Numbers and Math
# You don’t need to be a math whiz to program well. The truth is, few
# programmers need to know more than basic algebra.
# Of course, how much math you need to know depends on the
# application you are working on. In general, the level of math required to
# successfully work as a programmer is less than you might expect.
# Although math and computer programming aren’t as correlated as
# some people might believe, numbers are an integral part of any
# programming language and Python is no exception.
# In this chapter, you will learn how to:
# • Work with Python’s three built-in number types: integer, floating
# point, and complex numbers
# • Round numbers to a given number of decimal places
# • Format and display numbers in strings
# Integers and Floating-Point
# Numbers
# Python has three built-in number data types: integers, floating-point
# numbers, and complex numbers. In this section, you’ll learn about
# integers and floating-point numbers, which are the two most commonly
# used number types. You’ll learn about complex numbers in section
# 5.6.

# Integers
# An integer is a whole number with no decimal places. For example,
# 1 is an integer, but 1.0 isn’t. The name for the integer data type is int,
# which you can see with the type() function:
print(type(1))
# You can create an integer by simply typing the number explicitly or
# using the int() function. In Chapter 4, you learned how to convert
# a string containing an integer to a number using int(). For example,
# the following converts the string "25" to the integer 25:
print(int('25'), type(int('25')))
# An integer literal is an integer value that is written explicitly in your
# code, just like a string literal is a string that is written explicitly in
# your code. For example, 1 is an integer literal, but int("1") isn’t.
# Integer literals can be written in two different ways:
print(1000000)
print(1_000_000)
# The first example is straightforward. Just type a 1 followed by six
# zeros. The downside to this notation is that large numbers can be
# difficult to read.
# When you write large numbers by hand, you probably group digits
# into groups of three, separated by a comma. 1,000,000 is a lot easier
# to read than 1000000.
# In Python, you can’t use commas to group digits in integer literals,
# but you can use an underscore (_). The value 1_000_000 expresses one
# million in a more readable manner.

# Floating-Point Numbers
# A сoating-point number, or сoat for short, is a number with a
# decimal place. 1.0 is a floating-point number, as is -2.75. The name
# of a floating-point data type is float:
print(1.0, type(1.0))
# Floats can be created by typing a number directly into your code, or by
# using the float() function. Like int(), float() can be used to convert
# a string containing a number to a floating-point number:
print(float('1.25'))
# A floating-point literal is a floating-point value that is written
# explicitly in your code. 1.25 is a floating-point literal, while float("1.25")
# is not.
# Floating-point literals can be created in three different ways. Each of
# the following creates a floating-point literal with a value of one million
print(1000000.0)
print(1_000_000.0)
print(1e6)
# The first two ways are similar to the two methods for creating integer
# literals that you saw earlier. The second method, which uses
# underscores to separate digits into groups of three, is useful for creating
# float literals with lots of digits.
# For really large numbers, you can use E-notation. The third method
# in the previous example uses E-notation to create a float literal.
# To write a float literal in E-notation, type a number followed by the
# letter e and then another number. Python takes the number to the
# left of the e and multiplies by 10 raised to the power of the number
# after the e. So 1e6 is equivalent to 1×10⁶.
# E-notation is short for exponential notation, and is the more
# common name for how many calculators and programming languages
# display large numbers.
# Python also uses E-notation to display large floating point numbers:
print(200000000000000000.0)
# The float 200000000000000000.0 gets displayed as 2e+17. The + sign
# indicates that the exponent 17 is a positive number. You can also use
# negative numbers as the exponent:
print(1e-4)
# The literal 1e-4 is interpreted as 10 raised to the power -4, which is
# 1/10000 or, equivalently, 0.0001.
# Unlike integers, floats do have a maximum size. The maximum
# floating-point number depends on your system, but something like
# 2e400 ought to be well beyond most machines’ capabilities. 2e400 is
# 2×10⁴⁰⁰, which is far more than the total number of atoms in the
# universe!
# When you reach the maximum floating-point number, Python returns
# a special float value inf:
print(2e400)
# inf stands for infinity, and it just means that the number you’ve tried
# to create is beyond the maximum floating-point value allowed on your
# computer. The type of inf is still float:
n = 2e320
print(n, type(n))
# There is also -inf which stands for negative infinity, and represents a
# negative floating-point number that is beyond the minimum floating point
# number allowed on your computer:
print(-n, type(n))
# You probably won’t come across inf and -inf often as a programmer,
# unless you regularly work with extremely large numbers.

# Arithmetic Operators and Expressions
# In this section, you’ll learn how to do basic arithmetic with numbers
# in Python, such as addition, subtraction, multiplication, and division.
# Along the way, you’ll learn some conventions for writing mathematical
# expressions in code.
# Addition
# Addition is performed with the + operator:
print(1 + 2)
# The two numbers on either side of the + operator are called operands.
# In the previous example, both operands are integers, but operands do
# not need to be the same type. You can add an int to a float with no
# problem:
print(1.0 + 2)
# Notice that the result of 1.0 + 2 is 3.0, which is a float. Any time a
# float is added to a number, the result is another float. Adding two
# integers together always results in an int.

# Subtraction
# To subtract two numbers, just put a - in between them
print(1 - 1)
print(1.0 - 1)
# Just like adding two integers, subtracting two integers always results
# in an int. Whenever one of the operands is a float, the result is also a
# float.
# The - operator is also used to denote negative numbers
print(-3)
# You can subtract a negative number from another number, but as you
# can see below, this can sometimes look confusing:
print(1 - -3)
# the first is the most PEP 8 compliant.
# That said, you can surround -3 with parentheses to make it even
# clearer that the second - is modifying 3:
print(1 - (-3))
# Using parentheses is a good idea because it makes the code more
# explicit. Computers execute code, but humans read code. Anything you
# can do to make your code easier to read and understand is a good
# thing.
# Multiplication
# To multiply two numbers, use the * operator:
print(2 * 3)
print(2 * 3.3)
# The type of number you get from multiplication follows the same rules
# as addition and subtraction. Multiplying two integers results in an int,
# and multiplying a number with a float results in a float

# Division
# The / operator is used to divide two numbers
# Unlike addition, subtraction, and multiplication, division with the /
# operator always returns a float. If you want to make sure that you get
# an integer after dividing two numbers, you can use int() to convert
# the result:
print(2 / 3)
print(int(2 / 3))
# Keep in mind that int() discards any fractional part of the number

# Integer Division
# If writing int(5.0 / 2) seems a little long-winded to you, Python
# provides a second division operator, //, called the integer division
# operator:
print(9 // 3)
print(3 // 2)
print(-3 // 2)
# The // operator first divides the number on the left by the number on
# the right and then rounds down to an integer. This might not give the
# value you expect when one of the numbers is negative.
# For example, -3 // 2 returns -2. First, -3 is divided by 2 to get -1.5.
# Then -1.5 is rounded down to -2. On the other hand, 3 // 2 returns 1
# Another thing the above example illustrates is that // returns a
# floating-point number if one of the operands is a float. This is why 9
# // 3 returns the integer 3 and 5.0 // 2 returns the float 2.0.
# Let’s see what happens when you try to divide a number by 0:
# >>> 1 / 0
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# Python gives you a ZeroDivisionError, letting you know that you just
# tried to break a fundamental rule of the universe.

# Exponents
# You can raise a number to a power using the ** operator:
print(2 ** 3)
# Exponents don’t have to be integers. They can also be floats:
print(2 ** 1.5)
print(2 ** (3 / 2))
# Raising a number to the power of 0.5 is the same as taking the square
# root, but notice that even though the square root of 9 is an integer,
# Python returns the float 3.0.
# For positive operands, the ** operator returns an integer if both
# operands are integers, and a float if any one of the operands is a
# floating-point number.
# You can also raise numbers to negative powers:
print(2 ** -1)
print(2 ** -2)
# Raising a number to a negative power is the same as dividing 1 by the
# number raised to the positive power. So, 2 ** -1 is the same as 1 / (2
# ** 1), which is the same as 1 / 2, or 0.5. Similarly 2 ** -2 is the same
# as 1 / (2 ** 2), which is the same as 1 / 4, or 0.25.

# The Modulus Operator
# The % operator, or the modulus, returns the remainder of dividing
# the left operand by the right operand:
print(5 // 2)
print(5 % 2)
print(20 % 4)
# 3 divides 5 once with a remainder of 2, so 5 % 3 is 2. Similarly, 7 divides
# 20 twice with a remainder of 6.
# In the last example, 16 is divisible by 8, so 16 % 8 is 0. Any time the
# number to the left of % is divisible by the number to the right, the result
# is 0.
# One of the most common uses of % is to determine whether or not one
# number is divisible by another. For example, a number n is even if
# and only if n % 2 is 0.
# What do you think 1 % 0 returns? Let’s try it out:
# >>> 1 % 0
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ZeroDivisionError: integer division or modulo by zero
# This makes sense because 1 % 0 is the remainder of dividing 1 by 0. But
# you can’t divide 1 by 0, so Python raises a ZeroDivisionError.
# When you work in IDLE’s interactive window, errors like ZeroDivisionError
# don’t cause much of a problem. The error is displayed and a new prompt pops
# up allowing you to continue writing code.
# However, whenever Python encounters an error while running
# a script, execution stops. The program is said to have crashed.
# In Chapter 8, you’ll learn how to handle errors so that your programs
# don’t crash unexpectedly.
# Things get a little tricky when you use the % operator with negative
# numbers:
print(5 % -3)
print(-5 % 3)
print(-5 % -3)
# These potentially shocking results are really quite well defined. To
# calculate the remainder r of dividing a number x by a number y, Python
# uses the equation r = x - (y * (x // y)).
# For example, to find 5 % -3, first find (5 // -3). Since 5 / -3 is about
# -1.67, 5 // -3 is -2. Now multiply that by -3 to get 6. Finally, subtract
# 6 from 5 to get -1.

# Arithmetic Expressions
# You can combine operators to form complex expressions.
# An expression is a combination of numbers, operators, and parentheses that
# Python can compute, or evaluate, to return a value.
# Here are some examples of arithmetic expressions:
print(2 * 3 - 1)
print(4 / 2 + 2 ** 3)
print(-1 + (-3 * 2 + 4))
# The rules for evaluating expressions work are the same as in everyday
# arithmetic. In school, you probably learned these rules under the
# name “order of operations.”
# The *, /, //, and % operators all have equal precedence, or priority,
# in an expression, and each of these has a higher precedence than the +
# and - operators. This is why 2*3 - 1 returns 5 and not 4. 2*3 is evaluated
# first, because * has higher precedence than the - operator.
# You may notice that the expressions in the previous example do not
# follow the rule for putting a space on either side of all of the operators.
# PEP 8 says the following about whitespace in complex expressions:
# “If operators with different priorities are used, consider
# adding whitespace around the operators with the lowest priority(ies).
# Use your own judgment; however,
# never use more than one space, and always have the
# same amount of whitespace on both sides of a binary
# operator.”
# — PEP 8, Other Recommendations

# Challenge: Perform Calculations on User Input
# Write a script called exponent.py that receives two numbers from the
# user and displays the first number raised to the power of the second
# number.
# A sample run of the program should look like this (with example input
# that has been provided by the user included below):
# Enter a base: 1.2
# Enter an exponent: 3
# 1.2 to the power of 3 = 1.7279999999999998
# Keep the following in mind:
# 1. Before you can do anything with the user’s input, you will have to
# assign both calls to input() to new variables.
# 2. The input() function returns a string, so you’ll need to convert the
# user’s input into numbers in order to do arithmetic.
# 3. You can use an f-string to print the result.
# 4. You can assume that the user will enter actual numbers as input.

# usr_base = input('Enter a base: ')
# usr_exponent = input('Enter an exponent: ')
# usr_power = float(usr_base) ** float(usr_exponent)
# print(f'{usr_base} to the power of {usr_exponent} = {usr_power}')

# Make Python Lie to You
# What do you think 0.1 + 0.2 is? The answer is 0.3, right? Let’s see what
# Python has to say about it. Try this out in the interactive window:
print(0.1 + 0.2)
# Well, that’s… almost right! What in the heck is going on here? Is this
# a bug in Python?
# No, it isn’t a bug! It’s a floating-point representation error, and
# it has nothing to do with Python. It’s related to the way floating-point
# numbers are stored in a computer’s memory.
# The number 0.1 can be represented as the fraction 1/10. Both the
# number 0.1 and it’s fraction 1/10 are decimal representations,
# or base 10 representations. Computers, however, store floating point
# numbers in base 2 representation, more commonly called
# binary representation.
# When represented in binary, something familiar yet possibly unexpected
# happens to the decimal number 0.1. The fraction 1/3 has no
# finite decimal representation. That is, 1/3 = 0.3333... with infinitely
# many 3’s after the decimal point. The same thing happens to the fraction
# 1/10 in binary.
# The binary representation of 1/10 is the following infinitely repeating
# fraction:
# 0.00011001100110011001100110011...
# Computers have finite memory, so the number 0.1 must be stored as
# an approximation and not as its true value. The approximation that
# gets stored is slightly higher than the actual value, and looks like this:
# 0.1000000000000000055511151231257827021181583404541015625
# You may have noticed, however, that when asked to print 0.1, Python
# prints 0.1 and not the approximated value above.
# Python doesn’t just chop off the digits in the binary representation for
# 0.1. What actually happens is a little more subtle.
# Because the approximation of 0.1 in binary is just that—an
# approximation—it is entirely possible that more than one decimal number
# have the same binary approximation.
# For example, the numbers 0.1 and 0.10000000000000001 both have the
# same binary approximation. Python prints out the shortest decimal
# number that shares the approximation.
# This explains why, in the first example of this section, 0.1 + 0.2 does
# not equal 0.3. Python adds together the binary approximations for 0.1
# and 0.2, which gives a number which is not the binary approximation
# for 0.3.
# If all this is starting to make your head spin, don’t worry! Unless you
# are writing programs for finance or scientific computing, you don’t
# need to worry about the imprecision of floating-point arithmetic.

# Math Functions and Number Methods
# Python has a few built-in functions you can use to work with numbers.
# In this section, you’ll learn about three of the most common ones:
# 1. round(), for rounding numbers to some number of decimal places
# 2. abs(), for getting the absolute value of a number
# 3. pow(), for raising a number to some power
# You’ll also learn about a method that floating-point numbers have to
# check whether or not they have an integer value.

# The round() function
# You can use round() to round a number to the nearest integer:
print(round(2.3))
print(round(2.7))
# round() has some unexpected behavior when the number ends in .5:
print(round(2.5))
print(round(3.5))
# 2.5 gets rounded down to 2 and 3.5 is rounded up to 4. Most people
# expect a number that ends in .5 to get rounded up, so let’s take a closer
# look at what’s going on here.
# Python 3 rounds numbers according to a strategy called rounding ties to even.
# A tie is any number whose last digit is a five. 2.5 and
# 3.1415 are ties, but 1.37 is not.
# When you round ties to even, you first look at the digit one decimal
# place to the left of the last digit in the tie. If that digit is even, you
# round down. If the digit is odd, you round up. That’s why 2.5 rounds
# down to 2 and 3.5 round up to 4.
# Rounding ties to even is the rounding strategy recommended
# for floating-point numbers by the IEEE (Institute of Electrical
# and Electronics Engineers) because it helps limit the impact
# rounding has on operations involving lots of numbers.
# The IEEE maintains a standard called IEEE 754 for how
# floating-point numbers are dealt with on a computer. It was
# published in 1985 and is still commonly used by hardware
# manufacturers today.
# You can round a number to a given number of decimal places by passing a
# second argument to round():
print(round(3.14159, 3))
print(round(2.71828, 2))
# The number 3.14159 is rounded to 3 decimal places to get 3.142, and
# the number 2.71828 is rounded to 2 decimal places to get 2.72.
# The second argument of round() must be an integer. If it isn’t, Python
# raises a TypeError.
print(round(2.675, 2))
# 2.675 is a tie because it lies exactly halfway between the numbers 2.67
# and 2.68. Since Python rounds ties to the nearest even number, you
# would expect round(2.675, 2) to return 2.68, but it returns 2.67 instead.
# This error is a result of floating-point representation error, and isn’t
# a bug in the round() function.
# Dealing with floating-point numbers can be frustrating, but this frustration
# isn’t specific to Python. All languages that implementthe IEEE
# floating-point standard have the same issues, including C/C++, Java,
# and JavaScript.
# In most cases, though, the little errors encountered with floating-point
# numbers are negligible, and the results of round() are perfectly
# useful.

# The abs() Function
# The absolute value of a number n is just n if n is positive, and -n
# if n is negative. For example, the absolute value of 3 is 3, while the
# absolute value of -5 is 5.
# To get the absolute value of a number in Python, you use the abs()
# function:
print(abs(3))
print(abs(-5))
# abs() always returns a positive number of the same type as its argument.
# That is, the absolute value of an integer is always a positive
# integer, and the absolute value of a float is always a positive float.

# The pow() Function
# In section 5.2, you learned how to raise a number to a power using
# the ** operator. You can also use the pow() function. pow() takes two
# arguments. The first is the base, that is the number to be raised to a
# power, and the second argument is the exponent.
# For example, the following uses pow() to raise 2 to the exponent 3:
print(pow(2, 3))
# Just like **, the exponent in pow() can be negative:
print(pow(2, -2))
# So, what’s the difference between ** and pow()? The pow() function
# accepts an optional third argument that computes the first number
# raised to the power of the second number and then takes the modulo
# with respect to the third number.
# In other words, pow(x, y, z) is equivalent to (x ** y) % z. Here’s an
# example with x = 2, y = 3, and z = 2:
print(pow(2, 3, 2))
# First, 2 is raised to the power 3 to get 8. Then 8 % 2 is calculated, which
# is 0 because 2 divides 8 with no remainder.

# Check if a Float Is Integral
# In Chapter 3 you learned about string methods like .lower(), .upper(),
# and .find(). Integers and floating-point numbers also have methods.
# Number methods aren’t used very often, but there is one that can be
# useful. Floating-point numbers have an .is_integer() method that
# returns True if the number is integral—meaning it has no fractional
# part—and returns False otherwise
num = 2.5
print(num.is_integer())
num = 2.0
print(num.is_integer())
# The .is_integer() method can be useful for validating user input. For
# example, if you are writing an app for a shopping cart for a store that
# sells pizzas, you will want to check that the quantity of pizzas the
# customer inputs is a whole number. You’ll learn how to do these kinds of
# checks in Chapter 8.
# Review Exercises
# 1. Write a script that asks the user to input a number and then displays that
# number rounded to two decimal places. When run, your
# program should look like this:
# Enter a number: 5.432
# 5.432 rounded to 2 decimal places is 5.43
# usr_number = input('Enter a number: ')
# rounded = f'{usr_number} rounded to 2 decimal' \
#     f' places is {round(float(usr_number), 2)}'
# print(rounded)
# # 2. Write a script that asks the user to input a number and then displays
# # the absolute value of that number. When run, your program
# # should look like this:
# # Enter a number: -10
# # The absolute value of -10 is 10.0
# usr_number = input('Enter a number: ')
# num_abs = f'The absolute value of' \
#     f' {usr_number} is {abs(float(usr_number))}'
# print(num_abs)
# # 3. Write a script that asks the user to input two numbers by using the
# # input() function twice, then display whether or not the difference
# # between those two number is an integer. When run, your program should look
# # like this:
# # Enter a number: 1.5
# # Enter another number: .5
# # The difference between 1.5 and .5 is an integer? True!
# # If the user inputs two numbers whose difference is not integral,
# # the output should look like this:
# # Enter a number: 1.5
# # Enter another number: 1.0
# # The difference between 1.5 and 1.0 is an integer? False!
# usr_number_1 = float(input('Enter a number: '))
# usr_number_2 = float(input('Enter another number: '))
# diff_num = usr_number_1 - usr_number_2
# test_int = f'The difference between {usr_number_1} and {usr_number_2}' \
#     f' is an integer? {diff_num.is_integer()}!'
# print(test_int)

# Print Numbers in Style
# Displaying numbers to a user requires inserting numbers into a string.
# In Chapter 3, you learned how to do this with f-strings by surrounding
# a variable assigned to a number with curly braces
# Those curly braces support a simple formatting language you can use
# to alter the appearance of the value in the final formatted string.
# For example, to format the value of n in the above example to two
# decimal places, replace the contents of the curly braces in the f-string
# with {n:.2f}:
n = 2.125
print(f'The value of n is {n:.2f}')
# The colon (:) after the variable n indicates that everything after it is
# part of the formatting specification. In this example, the formatting
# specification is .2f.
# The .2 in .2f rounds the number to two decimal places, and the f tells
# Python to display n as a рxed-point number. This means the number
# is displayed with exactly two decimal places, even if the original
# number has fewer decimal places.
# When n = 7.125, the result of {n:.2f} is 7.12. Just like round(), Python
# rounds ties to even when formatting numbers inside of strings. So, if
# you replace n = 7.125 with n = 7.126, then the result of {n:.2f} is "7.13"
# When you format a number as fixed-point, it’s always displayed with
# the precise number of decimal places specified:
print(f'The value of n is {n:.10f}')
# You can insert commas to group the integer part of large numbers by
# the thousands with the , option:
n = 1234567892.125
print(f'The value of n is {n:,.4f}')
# Another useful option is %, which is used to display percentages. The %
# option multiplies a number by 100 and displays it in fixed-point format,
# followed by a percentage sign.
# The % option should always go at the end of your formatting specification,
# and you can’t mix it with the f option. For example, .1% displays
# a number as a percentage with exactly one decimal place:
ratio = 0.9
print(f'Over {ratio:.1%} of Pythonistas say "Blabla"')
print(f'Over {ratio:.2%} of Pythonistas say "Blabla"')
# Review Exercises
# 1. Print the result of the calculation 3 ** .125 as a fixed-point number
# with three decimal places.
print(f'{(3 ** .125):.3f}')
# 2. Print the number 150000 as currency, with the thousands grouped
# with commas. Currency should be displayed with two decimal
# places.
print(f'{150000:,.2f} US$')
# 3. Print the result of 2 / 10 as a percentage with no decimal places.
# The output should look like 20%.
print(f'{(2 / 10):.0%}')

# Complex Numbers
# Python is one of the few programming languages that provides built-in
# support for complex numbers. While complex numbers do not
# come up often outside the domains of scientific computing and computer
# graphics, Python’s support for them is one of it’s strengths.
# Complex numbers only come up in a few specific situations.
# Many programmers never need to use them.
# Feel free to skip this section all together if you have no interest
# in how to work with complex numbers in Python. No other part
# of the book depends on the information in this section
# If you have ever taken a pre-calculus or higher level algebra math class,
# you may remember that a complex number is a number with two distinct
# components: a real component and an imaginary component.
# There are several ways to denote complex numbers, but a common
# method is to indicate the real component with the letter i and the
# imaginary component with the letter j. For example, 1i + 2j is the complex
# number with real part 1 and imaginary part 2.
# To create a complex number in Python, you simply write the real part,
# followed by a plus sign and the imaginary part with the letter j at the end
n = 1 + 2j
print(n)
# This convention helps eliminate any confusion that the displayed
# output may represent a string or a mathematical expression.
# Imaginary numbers come with two properties, .real and .imag, that
# return the real and imaginary component of the number, respectively:
print(n.real)
print(n.imag)
# Notice that Python returns both the real and imaginary components
# as floats, even though they were specified as integers.
# Complex numbers also have a .conjugate() method that returns the
# complex conjugate of the number:
print(n.conjugate())
# For any complex number, its conjugate is the complex number with
# the same real part and an imaginary part that is the same in absolute
# value but with the opposite sign. So in this case, the complex
# conjugate of 1 + 2j is 1 - 2j.
# The .real and .imag properties don’t need parentheses after
# them like the method .conjugate() does.
# The .conjugate() method is a function that performs an action
# on the complex number. .real and .imag don’t perform any
# action, they just return some information about the number.
# The distinction between methods and properties is a part of
# object oriented programming
# All of the arithmetic operators that work with floats and integers work
# with complex numbers also, except for the floor division (//) operator.
# Since this isn’t a math book, we won’t discuss the mechanics of
# complex arithmetic. Instead, here are some examples of using complex
# numbers with arithmetic operators
# All of the arithmetic operators that work with floats and integers work
# with complex numbers also, except for the floor division (//) operator.
# Since this isn’t a math book, we won’t discuss the mechanics of complex
# arithmetic. Instead, here are some examples of using complex
# numbers with arithmetic operators
a = 1 + 2j
b = 3 - 4j
print(a + b)
print(a - b)
print(a * b)
print(a ** b)
print(a / b)
