# Nearly all of the code you have seen in this book is unconditional.
# That is, the code does not make any choices. Every line of code is
# executed in the order that is written or that functions are called, with
# possible repetitions inside of loops.
# In this chapter, you will learn how to write programs that perform different
# actions based on different conditions using conditional logic.
# Paired with functions and loops, conditional logic allows you to write
# complex programs that handle many different situations
# In this chapter, you will learn how to:
# • Compare the values of two or more variables
# • Write if statements to control the flow of your programs
# • Handle errors with try and except
# • Apply conditional logic to create simple simulations

# Compare Values
# Conditional logic is based on performing different actions depending
# on whether or not some expression, called a conditional, is true or
# false
# In computer programming, conditionals often take the form of comparing two
# values, such as determining if one value is greater than
# another, or whether or not two values are equal to each other.
# A standard set of symbols called boolean comparators are used to make
# comparisons, and most of them may already be familiar to you.
# The following table describes these boolean comparators:
# Boolean Comparator Example Meaning
# >       a > b     a greater than b
# <       a < b     a less than b
# >=      a >= b    a greater than or equal to b
# <=      a <= b    a less than or equal to b
# !=      a != b    a not equal to b
# ==      a == b    a equal to b
# The term boolean is derived from the last name of the English
# mathematician George Boole, whose works helped lay the foundations
# of modern computing. In Boole’s honor, conditional logic is
# sometimes called boolean logic, and conditionals are sometimes
# called boolean expressions.
# There is also a fundamental data type called the boolean, or bool for
# short, which can have only one of two values. In Python, these values
# are conveniently named True and False:
import random

print(True, type(True))
print(False, type(False))
# Note that True and False both start with capital letters.
# The result of evaluating a conditional is always a boolean value:
print(1 == 1)
print(3 > 5)
print('a' > 'b')
# In the first example, since 1 is equal to 1, the result of 1 == 1 is True. In
# the second example, 3 is not greater than 5, so the result is False
# A common mistake when writing conditionals is to use the assignment
# operator =, instead of ==, to test whether or not two
# values are equal.
# Fortunately, Python will raise a SyntaxError if this mistake is encountered,
# so you’ll know about it before you run your program.
# The comparators < and > represent the notions of greater than and less
# than when used with numbers, but more generally they represent the
# notion of order. In this regard, "a" < "b" checks if the string "a" comes
# before the string "b". But how are string ordered?
# In Python, strings are ordered lexicographically, which is a fancy
# way to say they are ordered as they would appear in a dictionary. So
# you can think of "a" < "b" as asking whether or not the letter a comes
# before the letter b in the dictionary.
# Lexicographic ordering extends to strings with two or more characters
# by looking at each component letter of the string:
print('apple' < 'astronaut')
print('beauty' > 'truth')
# Since strings can contain characters other than letters of the alphabet,
# the ordering must extend to those other characters as well.
# We won’t go in to the details of how characters other than letters are
# ordered. In practice, the < and > comparators are most often used with
# numbers, not strings.

# Add Some Logic
# In addition to boolean comparators, Python has special keywords
# called logical operators that can be used to combine boolean
# expressions. There are three logical operators: and, or, and not.
# Logical operators are used to construct compound logical expressions.
# For the most part, these have meanings similar to their meaning in the
# English language, although the rules regarding their use in Python are
# much more precise.

# The and Keyword
# Consider the following statements:
# 1. Cats have four legs.
# 2. Cats have tails.
# In general, both of these statements are true.
# When we combine these two statements using and, the resulting sentence
# “cats have four legs and cats have tails” is also a true statement.
# If both statements are negated, the compound statement “cats do not
# have four legs and cats do not have tails” is false
# Even when we mix and match false and true statements, the compound statement
# is false. “Cats have four legs and cats do not have
# tails” and “cats do not have four legs and cats have tails” are both false
# statements.
# When two statements P and Q are combined with and, the truth value
# of the compound statement “P and Q” is true if and only if both P and
# Q are true.
# Python’s and operator works exactly the same way. Here are four example of
# compound statements with and:
print(1 < 2 and 3 < 4)
print(2 < 1 and 4 < 3)
print(2 < 1 and 3 < 4)
print(1 < 2 and 4 < 3)

# The following table summarizes the rules for the and operator:
# Combination using and Result
# True and True         True
# True and False        False
# False and True        False
# False and False       False

# The or Keyword
# When we use the word “or” in everyday conversation, sometimes we
# mean an exclusive or. That is, only the first option or the second
# option can be true.
# For example, the phrase “I can stay or I can go” uses the exclusive or.
# I can’t both stay and go. Only one of these options can be true.
# In Python the or keyword is inclusive. That is, if P and Q are two
# expressions, the statement “P or Q” is true if any of the following are true:
# 1. P is true
# 2. Q is true
# 3. Both P and Q are true
# Let’s look at some examples using numerical comparisons:
print(1 < 2 or 3 < 4)
print(2 < 1 or 4 < 3)
print(2 < 1 or 3 < 4)
print(1 < 2 or 4 < 3)
# Note that if any part of a compound statement is True, even if the other
# part is False, the result is always true True. The following table
# summarizes these results:
# Combination using or Result
# True or True          True
# True or False         True
# False or True         True
# False or False        False

# The not Keyword
# The not keyword reverses the truth value of a single expression:
# Use of not Result
# not True   False
# not False  True
# One thing to keep in mind with not, though, is that it doesn’t always
# behave the way you might expect when combined with comparators
# like ==. For example, not True == False returns True, but False == not
# True will raise an error:
# >>> not True == False
# True
# >>> False == not True
# File "<stdin>", line 1
# False == not True
#          ^
# SyntaxError: invalid syntax
# This happens because Python parses logical operators according to an
# operator precedence, just like arithmetic operators have an order
# of precedence in everyday math.
# The order of precedence for logical and boolean operators, from highest
# to lowest, is described in the following table. Operators on the
# same row have equal precedence
# Operator Order of Precedence (Highest to Lowest)
# <, <=, ==, >=, >
# not
# and
# or
# Looking again at the expression False == not True, not has a lower
# precedence than == in the order of operations. This means that when
# Python evaluates False == not True, it first tries to evaluate False ==
# not which is syntactically incorrect.
# You can avoid the SyntaxError by surrounding not True with parentheses:
print(True == (not False))

# Building Complex Expressions
# You can combine the and, or and not keywords with True and False to
# create more complex expressions. Here’s an example of a more complex
# expression:
print(True and not (1 != 1))
# What do you think the value of this expression is?
# To find out, break the expression down by starting on the far right side.
# 1 != 1 is False, since 1 has the same value as itself. So you can simplify
# the above expression as follows:
print(True and not (False))
# Now, not (False) is the same as not False, which is True. So you can
# simplify the above expression once more:
print(True and True)
# Finally, True and True is just True. So, after a few steps, you can see that
# True and not (1 != 1) evaluates to True.
# When working through complicated expressions, the best strategy is
# to start with the most complicated part of the expression and build
# outward from there.
# For instance, try evaluating the following expression:
print(("A" != "A") or not (2 >= 3))
# Start by evaluating the two expressions in parentheses. "A" != "A" is
# False because "A" is equal to itself. 2 >= 3 is also False because 2 is
# smaller than 3. This gives you the following equivalent, but simpler,
# expression:
print((False) or not (False))
# Since not has a higher precedence than or, the above expression is
# equivalent to the following:
print(False or (not False))
# not False is True, so you can simplify the expression once more:
print(False or True)
# Finally, since any compound expression with or is True if any one of
# the expressions on the left or right of the or is True, you can conclude
# that ("A" != "A") or not (2 >= 3) is True.
# Grouping expressions in a compound conditional statement with
# parentheses improves readability. Sometimes, though, parenthesis
# are required to produce the expected value.
# For example, upon first inspection, you may expect the following to
# output True, but it actually returns False:
print(True and False == True and False)
# The reason this is False is that the == operator has a higher precedence
# than and, so Python interprets the expression as True and (False ==
# True) and False. Since False == True is False, this is equivalent to True
# and False and False, which evaluates to False.
# The following shows how to add parentheses so that the expression
# evaluates to True:
print((True and False) == (True and False))
# Logical operators and boolean comparators can be confusing the first
# time you encounter them, so if you don’t feel like the material in this
# section comes naturally, don’t worry!
# With a little bit of practice, you’ll be able to make sense of what’s going
# on and build your own compound conditional statements when you
# need them.

# Control the Flow of Your Program
# Now that we can compare values to one other with boolean comparators
# and build complex conditional statements with logical operators,
# we can add some logic to our code so that it performs different actions
# for different conditions.
# The if Statement
# An if statement tells Python to only execute a portion of code if a condition
# is met.
# For example, the following if statement will print 2 and 2 is 4 if the
# conditional 2 + 2 == 4 is True:
if 2 + 2 == 4:
    print('2 and 2 is 4')
# Just like while loops, an if statement has three parts:
# 1. The if keyword
# 2. A test condition, followed by a colon
# 3. An indented block of code that is executed if the test condition is
# True
# In the above example, the test condition is 2 + 2 == 4. Since this
# expression is True, executing the if statement in IDLE displays the
# text 2 and 2 is 4.
# If the test condition is False (for instance, 2 + 2 == 5), Python skips
# over the indented block of code and continues execution on the next
# non-indented line.
# For example, the following if statement does not print anything:
if 2 + 2 == 5:
    print('Is this the mirror universe')
# Once the indented code block in an if statement is executed, Python
# will continue to execute the rest of the program.
# Consider the following script:
grade = 95
if grade >= 70:
    print("You passed the class!")
print("Thank you for attending.")
# Since grade is 95, the test condition grade >= 70 is True and the string
# "You passed the class!" is printed. Then the rest of the code is executed
# and "Thank you for attending." is printed.
# The line print("Thank you for attending.") is executed whether or not
# grade is greater than or equal to 70 because it is after the indented code
# block in the if statement.
# A failing student will not know that they failed if all they see from your
# code is the text "Thank you for attending.".
# Let’s add another if statement to tell the student they did not pass if
# their grade is less than 70:
grade = 40
if grade >= 70:
    print("You passed the class!")
if grade < 70:
    print("You did not pass the class :(")
print("Thank you for attending.")
# The output now looks like this:
# In English, we can describe an alternate case with the word “otherwise”.
# For instance, “If your grade is 70 or above, you pass the class.
# Otherwise, you do not pass the class.”
# Fortunately, there is a keyword that does for Python what the word
# “otherwise” does in English.

# The else Keyword
# The else keyword is used after an if statement in order to execute
# some code only if the if statement’s test condition is False.
# The following script uses else to shorten the code in the previous script
# for displaying whether or not a student passed a class:
grade = 40
if grade >= 70:
    print("You passed the class!")
else:
    print("You did not pass the class :(")
print("Thank you for attending.")
# Notice that the else keyword has no test condition, and is followed by
# a colon. No condition is needed, because it executes for any condition
# that fails the if statement’s test condition.
# The line that prints "Thank you for attending." still runs, even if the
# indented block of code after else is executed.
# The if and else keywords work together nicely if you only need to test
# a condition with exactly two states.
# Sometimes, you need to check three or more conditions. For that, you
# use elif.

# The elif Keyword
# The elif keyword is short for “else if” and can be used to add additional
# conditions after an if statement.
# Just like if statements, elif statements have three parts:
# 1. The elif keyword
# 2. A test condition, followed by a colon
# 3. An indented code block that is executed if the test condition evaluates
# to True
# The following script combines if, elif, and else to print the letter
# grade a student earned in a class:
grade = 85  # 1
if grade >= 90:  # 2
    print("You passed the class with a A.")
elif grade >= 80:  # 3
    print("You passed the class with a B.")
elif grade >= 70:  # 4
    print("You passed the class with a C.")
else:  # 5
    print("You did not pass the class :(")
print("Thanks for attending.")  # 6
# Both grade >= 80 and grade >= 70 are True when grade is 85, so you might
# expect both elif blocks on lines 3 and 4 to be executed.
# However, only the first block for which the test condition is True is
# executed. All remaining elif and else blocks are skipped
# Let’s break down the execution of the script step-by-step:
# 1. grade is assigned the value 85 in the line marked 1.
# 2. grade >= 90 is False, so the if statement marked 2 is skipped.
# 3. grade >= 80 is True, so the block under the elif statement in line 3
# is executed, and "You passed the class with a B." is printed.
# 4. The elif and else statements in lines 4 and 5 are skipped, since the
# condition for the elif statement on line 3 was met.
# 5. Finally, line 6 is executed and "Thanks for attending." is printed.
# The if, elif, and else keywords are some of the most commonly used
# keywords in the Python language. They allow you to write code that
# responds to different conditions with different behavior.
# The if statement allows you to solve more complex problems than
# code without any conditional logic. You can even nest an if statement
# inside another one to write code that handles tremendously complex
# logic!

# Nested if Statements
# Just like for and while loops can be nested within one another, you nest
# an if statement inside another to create complicated decision making
# structures.
# Consider the following scenario. Two people play a one-on-one sport
# against one another. You must decide which of two players wins depending
# on the players’ scores and the sport they are playing:
# • If the two players are playing basketball, the player with the greatest
# score wins.
# • If the two players are playing golf, then the player with the lowest
# score wins.
# • In either sport, if the two scores are equal, the game is a draw.
# The following program solves this using nested if statements:

# sport = input('Enter a sport: ').lower().strip()
# p1_score = input('Enter player 1 score: ')
# p2_score = input('Enter player 2 score: ')
sport = 'basketball'
p1_score = 1
p2_score = 2

if sport == 'basketball':
    if p1_score > p2_score:
        print('Player 1 wins')
    elif p1_score < p2_score:
        print('Player 2 wins')
    else:
        print('The game is a draw')
elif sport == 'golf':
    if p1_score > p2_score:
        print('Player 2 wins')
    elif p1_score < p2_score:
        print('Player 1 wins')
    else:
        print('The game is a draw')
else:
    print('Unknown sport')
# This program first asks the user to input a sport and the scores for two
# players.
# In (#1), the string assigned to sport is converted to lowercase using
# .lower() and is compared it to the string "basketball". This ensures
# that user input such as "Basketball" or "BasketBall" all get interpreted
# as the same sport.
# Then the players scores are compared. If they are equal, the game is
# a draw. If player 1’s score is larger than player 2’s score, then player
# 1 wins the basketball game. Otherwise, player 2 wins the basketball
# game.
# In (#2), the string assigned to sport is converted to lowercase gain and
# compared to the string "golf". Then the players scores are checked
# again. If the two scores are equal, the game is a draw. If player 1’s
# score is less than player 2’s score, then player 1 wins. Otherwise,
# player 2 wins.
# Finally, in (#3), if the sport variable is assigned to a string other than
# "basketball" or "golf", the message "Unknown sport" is displayed.
# The output of the script depends on the input value.
# Nested if statements can create many possible ways that your code
# can run. If you have many deeply nested if statements (more than
# two levels), then the number of possible ways the code can execute
# grows quickly.
# The complexity that results from using deeply nested if statements may make
# it difficult to predict how your program will
# behave under given conditions.
# For this reason, nested if statements are generally discouraged.
# Using this code, you can simplify the program quite a bit:
if sport == 'basketball' or sport == 'golf':
    p1_wins_bskt = p1_score > p2_score and (sport == 'basketball')
    p1_wins_gf = p1_score < p2_score and (sport == 'golf')
    p1_wins = p1_wins_bskt or p1_wins_gf

    if p1_wins:
        print('Player 1 wins')
    elif p1_score == p2_score:
        print('The game is a draw')
    else:
        print('Player 2 wins')
else:
    print('Unknown sport')

# Nested if statements are sometimes necessary. However, if you find
# yourself writing lots of nested if statements, it might be a good idea
# to stop and think about how you might simplify your code.

# Challenge: Find the Factors of a Number
# A factor of a positive integer n is any positive integer less than or equal
# to n that divides n with no remainder.
# For example, 3 is a factor of 12 because 12 divided by 3 is 4, with no
# remainder. However, 5 is not a factor of 12 because 5 goes into 12 twice
# with a remainder of 2.
# Write a script factors.py that asks the user to input a positive integer
# and then prints out the factors of that number. Here’s a sample run
# of the program with output:
# Enter a positive integer: 12
# 1 is a factor of 12
# 2 is a factor of 12
# 3 is a factor of 12
# 4 is a factor of 12
# 6 is a factor of 12
# 12 is a factor of 12


# def to_int_error_get_zero(string):
#     try:
#         new_int = int(string)
#         return new_int
#     except ValueError:
#         return 0


# usr_int = 0
# while usr_int <= 0:
#     usr_input = input('Enter a positive integer: ')
#     usr_int = to_int_error_get_zero(usr_input)

# for i in range(1, usr_int + 1):
#     if (usr_int % i) == 0:
#         print(f'{i} is a factor of {usr_int}')

# Recover From Errors
# Encountering errors in your code might be frustrating, but it’s totally
# normal! It happens to even the best programmers.
# Programmers often refer to run-time errors as exceptions. So, when
# you encounter an error, congratulate yourself! You’ve just made the
# code do something exceptional!
# Errors aren’t always a bad thing. That is, they don’t always mean you
# made a mistake. For example, trying to divide the 1 by 0 results in a
# ZeroDivisionError. If the divisor is entered by a user, you have no way
# of knowing ahead of time whether or not the user will enter a 0!
# In order to create robust programs, you need to be able to handle errors
# caused by invalid user input — or any other unpredictable source.
# In this section you’ll learn how.

# A Zoo of Exceptions
# When you encounter an exception, it’s useful to know what went
# wrong. Python has a number of built-in exception types that describe
# different kinds of errors.
# Throughout this book you have seen several different errors. Let’s
# collect them here and add a few new ones to the list.

# ValueError
# A ValueError occurs when an operation encounters an invalid value.
# For example, trying to convert the string "not a number" to an integer
# results in a ValueError:
# >>> int("not a number")
# Traceback (most recent call last):
# File "<pyshell#1>", line 1, in <module>
# int("not a number")
# ValueError: invalid literal for int() with base 10: 'not a number'
# The name of the exception is displayed on the last line, followed by a
# description of the specific problem that occurred. This is the general
# format for all Python exceptions.

# TypeError
# A TypeError occurs when an operation is performed on a value of the
# wrong type. For example, trying to add a string and an integer will
# result in a TypeError:
# >>> "1" + 2
# Traceback (most recent call last):
# File "<pyshell#1>", line 1, in <module>
# "1" + 2
# TypeError: can only concatenate str (not "int") to str

# NameError
# A NameError occurs when you try to use a variable name that hasn’t
# been defined yet:
# >>> print(does_not_exist)
# Traceback (most recent call last):
# File "<pyshell#3>", line 1, in <module>
# print(does_not_exist)
# NameError: name 'does_not_exist' is not defined

# ZeroDivisionError
# A ZeroDivisionError occurs when the divisor in a division operation is
# 0:
# >>> 1 / 0
# Traceback (most recent call last):
# File "<pyshell#4>", line 1, in <module>
# 1 / 0
# ZeroDivisionError: division by zero

# OverflowError
# An OverflowError occurs when the result of an arithmetic operation is
# too large. For example, trying to raise the value 2.0 to the power 1_-
# 000_000 results in an OverflowError:
# >>> pow(2.0, 1_000_000)
# Traceback (most recent call last):
# File "<pyshell#6>", line 1, in <module>
# pow(2.0, 1_000_000)
# OverflowError: (34, 'Result too large')
# You may recall from Chapter 5 that integers in Python have unlimited
# precision. This means that OverflowErrors can only occur with floating
# point numbers.
# Raising the integer 2 to the value 1_000_000 will not raise an
# OverflowError but a ValueError for too many digits

# The try and except Keywords
# Sometimes you can predict that a certain exception might occur.
# Instead of letting the program crash, you can catch the error if it occurs
# and do something else instead.
# For example, you might need to ask the user to input an integer. If the
# user enters a non-integer value, such as the string "a", you need to let
# them know that they entered an invalid value.
# To prevent the program from crashing you can use the try and except
# keywords. Let’s look at an example:
# try:
#     number = int(input("Enter an integer: "))
# except ValueError:
    # print("That was not an integer")
# The try keyword is used to indicate a try block and is followed by a
# colon. The code indented after try is executed. In this case, the user
# is asked to input an integer. Since input() returns a string, the user
# input is converted to an integer with int() and the result is assigned
# to the variable number.
# If the user inputs a non-integer value, the int() operation will raise
# a ValueError. If that happens, the code indented below the line except
# ValueError is executed. So, instead of the program crashing, the string
# "That was not an integer" is displayed.
# If the user does input a valid integer value, then the code in the except
# ValueError block is never executed.
# On the other hand, if a different kind of exception had occurred, such
# as a TypeError, then the program will crash. The above example only
# handles one type of exception — a ValueError.
# You can handle multiple exception types by separating the exception
# names with commas and putting the list of names in parentheses:


def divide(num1, num2):
    try:
        print(num1 / num2)
    except (TypeError, ZeroDivisionError):
        print('encountered a problem')
# In this example, the function divide() takes two parameters num1 and
# num2 and prints the result of dividing num1 by num2.
# If divide() is called with an argument that is a string, then the
# division operation will raise a TypeError. Additionally, if num2 is 0, then a
# ZeroDivisionError is raised.
# The line except (TypeError, ZeroDivisionError) will handle both of these
# exceptions and display the string "encountered a problem" if either
# exception is raised.
# Many times, though, it is helpful to catch each error individually so
# that you can display text that is more helpful to the user. To do this,
# you can use multiple except blocks after a try block:


def divide(num1, num2):
    try:
        print(num1 / num2)
    except TypeError:
        print('both types need to be numbers')
    except ZeroDivisionError:
        print('num2 must not be 0')
# In this example, the ValueError and ZeroDivisionError are handled separately.
# This way, a more descriptive message is displayed if something
# goes wrong.
# If one of num1 or num2 is not a number, then a TypeError is raised and
# the message "Both arguments must be numbers" is displayed. If num2 is 0,
# then a ZeroDivisionError is raised and the message "num2 must not be 0"
# is displayed.


# The “Bare” except Clause
# You can use the except keyword by itself without naming specific exceptions:
try:
    ...  # Do lots of hazardous things that might break
except:
    print("Something bad happened!")
# If any exception is raised while executing the code in the try block, the
# except block will run and the message "Something bad happened!" will be
# displayed.
# This might sound like a great way to ensure your program never
# crashes, but this is actually bad idea and the pattern is
# generally frowned upon!
# There are a couple of reasons for this, but the most important reason
# for new programmers is that catching every exception could hide bugs
# in your code, giving you a false sense of confidence that your code
# works as expected.
# If you only catch specific exceptions, then when unexpected errors are
# encountered, Python will print the traceback and error information
# giving you more information to work with when debugging your code.
# Review Exercises
# 1. Write a script that repeatedly asks the user to input an integer,
# displaying a message to “try again” by catching the ValueError that
# is raised if the user did not enter an integer.
# Once the user enters an integer, the program should display
# the number back to the user and end without crashing.
# while True:
#     try:
#         num_usr = int(input('Enter an integer: '))
#         print(num_usr)
#         break
#     except ValueError:
#         print('try again')
# 2. Write a program that asks the user to input a string and an integer
# n. Then display the character at index n in the string.
# Use error handling to make sure the program doesn’t crash
# if the user does not enter an integer or the index is out of bounds.
# The program should display a different message depending on
# what error occurs.
# while True:
#     try:
#         usr_str = input('Enter a string: ')
#         usr_idx = int(input('Enter a index (an integer): '))
#         print(usr_str[usr_idx])
#         break
#     except ValueError:
#         print('You must enter a integer as index')
#     except IndexError:
#         print("You don't have enough characters for this index")


# Simulate Events and Calculate
# Probabilities
# In this section, we’ll apply some of the concepts we’ve learned about
# loops and conditional logic to a real world problem: simulating events
# and calculating probabilities.
# We’ll be running a simple simulation known as a Monte Carlo experiment.
# Each experiment consists of a trial, which is just some process
# that can be repeated — such as flipping a coin – that generated some
# outcome — such as landing on heads or tails. The trial is repeated over
# and over again in order to calculate the probability that some outcome
# occurs.
# In order to do this, we need to add some randomness to our code.

# The random module
# Python provides several functions for generating random numbers in
# the random module. A module is a collection of related code. Python’s
# standard library is an organized collection of modules that you can
# import into your own code in order to solve various problems.
# To import the random module, type the following:
# >>> import random
# Now we can use functions from the random module in our code. For
# example, the randint() has two required parameters called a and b and
# returns a random integer that is greater than or equal to a and less
# than or equal to b. Both a and b must be integers.
# For example, the following code produces a random integer between
# 1 and 10:
print(random.randint(1, 10))
# Since the result is random, your output will probably be different than
# 9. If you type the same code in again, you will likely get a different
# number.
# Since randint() is located in the random module, you must type random
# followed by a dot (.) and then the function name in order to use it.
# It is important to remember that when using randint(), the two
# parameters a and b must both be integers, and the output might be
# equal to one of a and b, or any number in-between. For instance,
# random.randint(0, 1) randomly returns either a 0 or a 1.
# Furthermore, each integer between a and b is equally likely to be return
# by randint(). So, for randint(1, 10), each integer between 1 and 10
# has a 10% chance of being returned. For randint(0, 1), there is a 50%
# chance a 0 is returned.

# Flipping Fair Coins
# Let’s see how to use randint() to simulate flipping a fair coin. By a
# fair coin, we mean a coin that, when flipped, has an equal chance of
# landing on heads or tails.
# One trial for our experiment will be flipping the coin. The outcome is
# either a heads or a tails. The question is: in general, over many coin
# flips, what is the ratio of heads to tails?
# Let’s think about how to solve this problem. We’ll need to keep track
# of how many times we get a heads or tails, so we need a heads tally
# and a tails tally. Each trial has two steps:
# 1. Flip the coin.
# 2. If the coin lands on heads, update the heads tally. Otherwise, the
# coin lands on tails so update the tails tally.
# We need to repeat the trial many times, say 10,000. A for loop over
# range(10_000) is a good choice for doing something like that.
# Now that we have a plan, let’s start by writing a function called coin_-
# flip() that randomly returns the string "heads" or the string "tails".
# We can do this using random.randint(0, 1). We’ll use 0 to represent
# heads and 1 for tails.
# Here’s the code for the coin_flip() function:


def coin_flip():
    """Randomly return 'heads' or 'tails'"""
    if random.randint(0, 1) == 0:
        return 'heads'
    else:
        return 'tails'


# If random.randint(0, 1) returns a 0, then coin_flip() returns "heads".
# Otherwise, coin_flip() returns "tails".
# Now we can write a for loop that flips the coin 10,000 times and updates a
# heads or tails tally accordingly:
heads_tally = 0
tails_tally = 0

for trial in range(100000):
    if coin_flip() == 'heads':
        heads_tally += 1
    else:
        tails_tally += 1
# First, two variables heads_tally and tails_tally are created and both
# are initialized to the integer 0.
# Then the for loop runs 10,000 times. Each time, the coin_flip() function
# is called. If it returns the string "heads", then the heads_tally variable
# is incremented by 1. Otherwise tails_tally is incremented by 1.
# Finally, we can print the ratio of heads and tails:
ratio = heads_tally / tails_tally
print(f'The ratio of heads to tails is {ratio:.2f}')
# If you save the above code to a script and run it a few times, you will
# see that the result is usually between .98 and 1.02. If you increase the
# range(10_000) in the for loop to, say, range(50_000), the results should
# get closer to 1.0.
# This behavior makes sense. Since the coin is fair, we should expect
# that after many flips, the number of heads is roughly equal to the
# number of tails.
# In life, things aren’t always fair. A coin may have a slight tendency to
# land on heads instead of tails, or vice versa. So, how do you simulate
# something like an unfair coin?

# Tossing Unfair Coins
# randint() returns a 0 or a 1 with equal probability. If 0 represents tails
# and 1 represents heads, then to simulate an unfair coin we need a way
# to return one of 0 or 1 with a higher probability.
# The random() function can be called without any arguments and returns a
# floating-point number greater than or equal to 0.0 but less
# than 1.0. Each possible return value is equally likely. In probability
# theory, this is known as a uniform probability distribution.
# One consequence of this is that, given a number n between 0 and 1, the
# probability that random() returns a number less than n is just n itself.
# For example, the probability that random() is less than .8 is .8 and the
# probability that random() is less than .25 is .25.
# Using this fact, we can write a function that simulates a coin flip, but
# returns tails with a specified probability:


def unfair_coin_flip(probability_of_tails):
    """Returns 'heads' or 'tails' based on a probability"""
    if random.random() < probability_of_tails:
        return 'tails'
    else:
        return 'heads'


# For example, unfair_coin_flip(.7) has a 70% chance of returning
# "tails".
# Let’s re-write the coin flip experiment from earlier
heads_tally = 0
tails_tally = 0

for trial in range(100_000):
    if unfair_coin_flip(.333333333) == 'heads':
        heads_tally += 1
    else:
        tails_tally += 1

ratio = heads_tally / tails_tally
print(f'The ratio of heads to tails is {ratio:.2f}')

# Running this simulation a few times shows that the ratio of heads to
# tails has gone down from 1 in the experiment with a fair coin to about
# .43.
# In this section you learned about the randint() and random() functions
# in the random module and saw how to use conditional logic and loops to
# write some coin toss simulations. Simulations like these are used in
# numerous disciplines to make predictions and test computer models
# of real world events.
# The random module provides many useful functions for generating random numbers
# and writing simulations. You can learn more about
# random in Real Python’s Generating Random Data in Python (Guide).
# https://realpython.com/python-random/
# Review Exercises
# You can пnd the solutions to these exercises and many other bonus
# resources online at realpython.com/python-basics/resources.
# 1. Write a function called roll() that uses the randint() function to
# simulate rolling a fair die by returning a random integer between
# 1 and 6.


def roll():
    '''Return a random number between 1 to 6'''
    return random.randint(1, 6)


print(f'You roll the dice and gets a {roll()}')
# 2. Write a script that simulates 10,000 rolls of a fair die and displays
# the average number rolled.
sum_dice_number = 0
trials = 10_000
for trial in range(trials):
    sum_dice_number += roll()

avg_dice_number = round(sum_dice_number / trials)
print(f'The average number rolled was {avg_dice_number}')

# Challenge: Simulate a Coin Toss
# Experiment
# Suppose you flip a fair coin repeatedly until it lands on both heads
# and tails at least once each. In other words, after the first flip, you
# continue to flip the coin until it lands on something different.
# Doing this generates a sequence of heads and tails. For example, the
# first time you do this experiment, the sequence might be heads, heads,
# then tails.
# On average, how many flips are needed for the sequence to contain
# both heads and tails?
# Write a simulation that runs 10,000 trials of the experiment and
# prints the average number of flips per trial.
sum_flips = 0

for trial in range(10_000):
    first_flip = coin_flip()
    # first_flip = unfair_coin_flip(.1)
    next_flip = first_flip
    flips_until_both = 1
    while first_flip == next_flip:
        next_flip = coin_flip()
        # next_flip = unfair_coin_flip(.1)
        flips_until_both += 1
    sum_flips += flips_until_both

avg_flips = sum_flips / 10_000
print(
    f'The average number of flips until we get both heads and tails '
    f'was {avg_flips}'
)

# Challenge: Simulate an Election
# With some help from the random module and a little condition logic,
# you can simulate an election between two candidates.
# Suppose two candidates, Candidate A and Candidate B, are running
# for mayor in a city with three voting regions. The most recent polls
# show that Candidate A has the following chances for winning in each
# region:
# • Region 1: 87% chance of winning
# • Region 2: 65% chance of winning
# • Region 3: 17% chance of winning
# Write a program that simulates the election 10,000 times and prints
# the percentage of where Candidate A wins.
# To keep things simple, assume that a candidate wins the election is
# they win in at least two of the three regions.


def election_result(a_wining_chance):
    if random.random() < a_wining_chance:
        return 'A'
    else:
        return 'B'


sum_wins = 0
elections = 10_000
for election in range(elections):
    region_a_result = election_result(.87)
    region_b_result = election_result(.65)
    region_c_result = election_result(.17)
    # print(
    #     f'election {election}: '
    #     f'r_A {region_a_result}, r_B {region_b_result}, r_C {region_c_result}'
    # )

    a_wins_a = region_a_result == 'A'
    a_wins_b = region_b_result == 'A'
    a_wins_c = region_c_result == 'A'

    if sum([a_wins_a, a_wins_b, a_wins_c]) > 1:
        sum_wins += 1

prop_wins = sum_wins / elections
print(
    f'Candidate A wins in {sum_wins} ({prop_wins:.2%}) cenarios of the '
    f'{elections} simulations'
)

# aditional resources
# https://realpython.com/python-operators-expressions/#logical-operators
# https://realpython.com/python-conditional-statements/

# One-Line if Statements
# It is customary to write if <expr> on one line and <statement> indented on
# the following line like this:
# if <expr>:
#     <statement>
# But it is permissible to write an entire if statement on one line.
# The following is functionally equivalent to the example above:
# if <expr>: <statement>
# There can even be more than one <statement> on the same line,
# separated by semicolons:
# if <expr>: <statement_1>; <statement_2>; ...; <statement_n>
# But what does this mean? There are two possible interpretations:
# If <expr> is true, execute <statement_1>.
# Then, execute <statement_2> ... <statement_n> unconditionally, irrespective
# of whether <expr> is true or not.
# If <expr> is true, execute all of <statement_1> ... <statement_n>.
# Otherwise, don’t execute any of them.
# Python takes the latter interpretation.
# The semicolon separating the <statements> has higher precedence than the
# colon following <expr>—in computer lingo, the semicolon is said to bind more
# tightly than the colon. Thus, the <statements> are treated as a suite,
# and either all of them are executed, or none of them are:
# if 'f' in 'foo': print('1'); print('2'); print('3')
# if 'z' in 'foo': print('1'); print('2'); print('3')
# Multiple statements may be specified on the same line as an elif or else
# clause as well:
# >>> x = 2
# >>> if x == 1: print('foo'); print('bar'); print('baz')
# ... elif x == 2: print('qux'); print('quux')
# ... else: print('corge'); print('grault')
# ...
# qux
# quux

# >>> x = 3
# >>> if x == 1: print('foo'); print('bar'); print('baz')
# ... elif x == 2: print('qux'); print('quux')
# ... else: print('corge'); print('grault')
# ...
# corge
# grault
# While all of this works, and the interpreter allows it, it is generally
# discouraged on the grounds that it leads to poor readability,
# particularly for complex if statements. PEP 8 specifically recommends
# against it.
# As usual, it is somewhat a matter of taste. Most people would find the
# following more visually appealing and easier to understand at first glance
# than the example above:
# >>> x = 3
# >>> if x == 1:
# ...     print('foo')
# ...     print('bar')
# ...     print('baz')
# ... elif x == 2:
# ...     print('qux')
# ...     print('quux')
# ... else:
# ...     print('corge')
# ...     print('grault')
# ...
# corge
# grault

# Conditional Expressions (Python’s Ternary Operator)
# Python supports one additional decision-making entity called a conditional
# expression. (It is also referred to as a conditional operator or
# ternary operator in various places in the Python documentation.)
# Conditional expressions were proposed for addition to the language in PEP
# 308 and green-lighted by Guido in 2005.
# In its simplest form, the syntax of the conditional expression is as follows:
# <expr1> if <conditional_expr> else <expr2>
# This is different from the if statement forms listed above because it is not
# a control structure that directs the flow of program execution.
# It acts more like an operator that defines an expression.
# In the above example, <conditional_expr> is evaluated first.
# If it is true, the expression evaluates to <expr1>.
# If it is false, the expression evaluates to <expr2>.
# Notice the non-obvious order: the middle expression is evaluated first,
# and based on that result, one of the expressions on the ends is returned.
# Here are some examples that will hopefully help clarify:
raining = False
print("Let's go to the", "library" if raining else "beach")
raining = True
print("Let's go to the", "library" if raining else "beach")

age = 12
s = 'minor' if age < 18 else 'adult'
print(s)
print('yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no')
# A common use of the conditional expression is to select variable assignment.
# For example, suppose you want to find the larger of two numbers.
# Of course, there is a built-in function, max(), that does just this
# (and more) that you could use. But suppose you want to write your own
# code from scratch.
# You could use a standard if statement with an else clause:
# >>> if a > b:
# ...     m = a
# ... else:
# ...     m = b
# ...
# But a conditional expression is shorter and arguably more readable as well:
# >>> m = a if a > b else b
# Remember that the conditional expression behaves like an expression
# syntactically. It can be used as part of a longer expression.
# The conditional expression has lower precedence than virtually all the other
# operators, so parentheses are needed to group it by itself.
# In the following example, the + operator binds more tightly than the
# conditional expression, so 1 + x and y + 2 are evaluated first,
# followed by the conditional expression. The parentheses in the second case
# are unnecessary and do not change the result:
x = y = 40
z = 1 + x if x > y else y + 2
print(z)
z = (1 + x) if x > y else (y + 2)
print(z)
# If you want the conditional expression to be evaluated first, you need to
# surround it with grouping parentheses. In the next example,
# (x if x > y else y) is evaluated first. The result is y, which is 40,
# so z is assigned 1 + 40 + 2 = 43:
z = 1 + (x if x > y else y) + 2
print(z)
# If you are using a conditional expression as part of a larger expression,
# it probably is a good idea to use grouping parentheses for clarification
# even if they are not needed.
# Conditional expressions also use short-circuit evaluation like compound
# logical expressions. Portions of a conditional expression are not evaluated
# if they don’t need to be.
# In the expression <expr1> if <conditional_expr> else <expr2>:
# If <conditional_expr> is true,
# <expr1> is returned and <expr2> is not evaluated.
# If <conditional_expr> is false,
# <expr2> is returned and <expr1> is not evaluated.
# As before, you can verify this by using terms that would raise an error:
print('foo' if True else 1/0)
print(1/0 if False else 'foo')
# In both cases, the 1/0 terms are not evaluated, so no exception is raised.
# Conditional expressions can also be chained together, as a sort of
# alternative if/elif/else structure, as shown here:
# >>> s = ('foo' if (x == 1) else
# ...      'bar' if (x == 2) else
# ...      'baz' if (x == 3) else
# ...      'qux' if (x == 4) else
# ...      'quux'
# ... )
# >>> s
# 'baz'
# It’s not clear that this has any significant advantage over the
# corresponding if/elif/else statement, but it is syntactically correct Python.

# The Python pass Statement
# Occasionally, you may find that you want to write what is called a code
# stub: a placeholder for where you will eventually put a block of code
# that you haven’t implemented yet.
# In languages where token delimiters are used to define blocks,
# like the curly braces in Perl and C, empty delimiters can be used to
# define a code stub. For example, the following is legitimate Perl or C code:
# # This is not Python
# if (x)
# {
# }
# Here, the empty curly braces define an empty block.
# Perl or C will evaluate the expression x, and then even if it is true,
# quietly do nothing.
# Because Python uses indentation instead of delimiters,
# it is not possible to specify an empty block. If you introduce an
# if statement with if <expr>:, something has to come after it, either on
# the same line or indented on the following line.
# Consider this script foo.py:
# if True:
# print('foo')
# If you try to run foo.py, you’ll get this:
# C:\Users\john\Documents\Python\doc>python foo.py
#   File "foo.py", line 3
#     print('foo')
#         ^
# IndentationError: expected an indented block
# The Python pass statement solves this problem.
# It doesn’t change program behavior at all.
# It is used as a placeholder to keep the interpreter happy in any situation
# where a statement is syntactically required, but you don’t really want
# to do anything:
if True:
    pass
print('foo')
# Now foo.py runs without error.
