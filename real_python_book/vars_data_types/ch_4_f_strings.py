# # f-Strings: A New and Improved Way to Format Strings in Python
# The good news is that f-strings are here to save the day.
# They slice! They dice! They make julienne fries! Okay, they do none of
# those things, but they do make formatting easier. They joined the party
# in Python 3.6. You can read all about it in PEP 498, which was written
# by Eric V. Smith in August of 2015.
# Also called “formatted string literals,” f-strings are string literals
# that have an f at the beginning and curly braces containing expressions that
# will be replaced with their values. The expressions are evaluated at
# runtime and then formatted using the __format__ protocol.
# As always, the Python docs are your friend when you want to learn more.
# Here are some of the ways f-strings can make your life easier.

# Simple Syntax
# The syntax is similar to the one you used with str.format() but less
# verbose. Look at how easily readable this is:
import timeit

name = 'Eric'
age = 74
print(f'Hello {name}, you are {age}.')

# Arbitrary Expressions
# Because f-strings are evaluated at runtime, you can put any and all
# valid Python expressions in them. This allows you to do some nifty things.
# You could do something pretty straightforward, like this:
print(f'{2 * 3}')
# But you could also call functions. Here’s an example:


def to_lowercase(input):
    return input.lower()


name = 'Eric Idle'
print(f'{to_lowercase(name)} is funny.')
# You also have the option of calling a method directly:
print(f'{name.lower()} is funny.')
# You could even use objects created from classes with f-strings.
# Imagine you had the following class:


class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'{self.first_name} {self.last_name} is {self.age}.'

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is {self.age}. Surprise!'


new_comedian = Comedian('Eric', 'Idle', 74)
print(new_comedian)
# The __str__() and __repr__() methods deal with how objects are presented as
# strings, so you’ll need to make sure you include at least one of those
# methods in your class definition. If you have to pick one,
# go with __repr__() because it can be used in place of __str__().
# The string returned by __str__() is the informal string representation
# of an object and should be readable. The string returned by
# __repr__() is the official representation and should be unambiguous.
# Calling str() and repr() is preferable to using __str__() and __repr__()
# directly.
# By default, f-strings will use __str__(), but you can make sure they
# use __repr__() if you include the conversion flag !r:
print(str(new_comedian))
print(repr(new_comedian))
print(f'{new_comedian!r}')
# Multiline f-Strings
# You can have multiline strings:
name = 'Eric'
profession = 'Comedian'
affiliation = 'Monty Python'
message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"You were in {affiliation}"
)
print(message)
# But remember that you need to place an f in front of each line of a
# multiline string.
# If you don’t put an f in front of each individual line,
# then you’ll just have regular, old, garden-variety strings and not shiny,
# new, fancy f-strings.
# If you want to spread strings over multiple lines,
# you also have the option of escaping a return with a \:
message = f"Hi {name}. " \
    f"You are a {profession}. " \
    f"You were in {affiliation}"
print(message)

# But this is what will happen if you use """:
message = f"""
    Hi {name}.
    You are a {profession}.
    You were in {affiliation}
"""
print(message)

# Read up on indentation guidelines in PEP 8.
# Speed
# The f in f-strings may as well stand for “fast.”
# f-strings are faster than both %-formatting and str.format().
# As you already saw, f-strings are expressions evaluated at runtime rather
# than constant values. Here’s an excerpt from the docs:
# “F-strings provide a way to embed expressions inside string literals,
# using a minimal syntax. It should be noted that an f-string is really an
# expression evaluated at run time, not a constant value.
# In Python source code, an f-string is a literal string,
# prefixed with f, which contains expressions inside braces.
# The expressions are replaced with their values.”
# At runtime, the expression inside the curly braces is evaluated in its
# own scope and then put together with the string literal part of the f-string.
# The resulting string is then returned. That’s all it takes.
# Here’s a speed comparison:

print(timeit.timeit("""name = "Eric"
age = 74
"%s is %s" % (name, age)""", number=10000))

print(timeit.timeit("""name = "Eric"
age = 74
"{} is {}".format(name, age)""", number=10000))

print(timeit.timeit("""name = "Eric"
age = 74
f'{name} is {age}'""", number=10000))

# As you can see, f-strings come out on top.
# However, that wasn’t always the case.
# When they were first implemented, they had some speed issues and needed to
# be made faster than str.format().
# A special BUILD_STRING opcode was introduced.

# Python f-Strings: The Pesky Details
# Now that you’ve learned all about why f-strings are great,
# I’m sure you want to get out there and start using them.
# Here are a few details to keep in mind as you venture off into
# this brave new world.
# Quotation Marks
# You can use various types of quotation marks inside the expressions.
# Just make sure you are not using the same type of quotation mark on the
# outside of the f-string as you are using in the expression.
# This code will work:
print(f"{'Eric Idle'}")
print(f'{"Eric Idle"}')
print(f"""Eric Idle""")
print(f'''Eric Idle''')
# If you find you need to use the same type of quotation mark on both the
# inside and the outside of the string, then you can escape with \:
print(f"The \"comedian\" is {name}, aged {age}")

# Dictionaries
# Speaking of quotation marks, watch out when you are working with dictionaries.
# If you are going to use single quotation marks for the keys of the
# dictionary, then remember to make sure you’re using double quotation marks
# for the f-strings containing the keys.
# This will work:
comedian = {'name': 'Eric', 'age': 74}
print(f'The comedian is {comedian["name"]}, aged {comedian["age"]}')
# But this will be a hot mess with a syntax error:
# >>> comedian = {'name': 'Eric Idle', 'age': 74}
# >>> f'The comedian is {comedian['name']}, aged {comedian['age']}.'
#   File "<stdin>", line 1
#     f'The comedian is {comedian['name']}, aged {comedian['age']}.'
#                                     ^
# SyntaxError: invalid syntax
# If you use the same type of quotation mark around the dictionary keys
# as you do on the outside of the f-string, then the quotation mark at
# the beginning of the first dictionary key will be interpreted as the end
# of the string.

# Braces
# In order to make a brace appear in your string, you must use double braces:
print(f'{{2 + 3}}')
# Note that using triple braces will result in there being only single braces
# in your string:
print(f'{{{2 + 3}}}')
print(f'{{2 + 3 = {2 + 3}}}')
# However, you can get more braces to show if you use more than triple braces:
print(f'{{{{2 + 3}}}}')

# Backslashes
# As you saw earlier, it is possible for you to use backslash escapes in the
# string portion of an f-string. However, you can’t use backslashes to escape
# in the expression part of an f-string:
# >>> f"{\"Eric Idle\"}"
#   File "<stdin>", line 1
#     f"{\"Eric Idle\"}"
#                       ^
# SyntaxError: f-string expression part cannot include a backslash
# You can work around this by evaluating the expression beforehand and using
# the result in the f-string:
# >>> name = "Eric Idle"
# >>> f"{name}"
# 'Eric Idle'
# Inline Comments
# Expressions should not include comments using the # symbol. You’ll get a
# syntax error:
# >>> f"Eric is {2 * 37 #Oh my!}."
#   File "<stdin>", line 1
#     f"Eric is {2 * 37 #Oh my!}."
#                                 ^
# SyntaxError: f-string expression part cannot include '#'
print(f'Eric is {2 * 3} #Oh my!')

SECRET = 'this-is-a-secret'


class Error:
    def __init__(self):
        pass


# A malicious user can craft a format string that
# can read data from the global namespace:
user_input = '{error.__init__.__globals__[SECRET]}'

# This allows them to exfiltrate sensitive information,
# like the secret key:
err = Error()
print(user_input.format(error=err))
# This wouldn't happen with f-strings
print(f'{user_input}')
