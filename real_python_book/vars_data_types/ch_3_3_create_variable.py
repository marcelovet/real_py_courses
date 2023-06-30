# Create a Variable
# In Python, variables are names that can be assigned a value and used
# to reference that value throughout your code. Variables are fundamental to
# programming for two reasons:
# 1. Variables keep values accessible: For example, the result of
# some time-consuming operation can be assigned to a variable so
# that the operation does not need to be performed each time you
# need to use the result.
# 2. Variables give values context: The number 28 could mean lots
# of different things, such as the number of students in a class, or the
# number of times a user has accessed a website, and so on. Naming
# the value 28 something like num_students makes the meaning of the
# value clear.
# The Assignment Operator
# Values are assigned to a variable using a special symbol = called the
# assignment operator. An operator is a symbol, like = or +, that
# performs some operation on one or more values.
# For example, the + operator takes two numbers, one to the left of the
# operator and one to the right, and adds them together. Likewise, the
# = operator takes a value to the right of the operator and assigns it to
# the name on the left of the operator.
phrase = 'Hello world'
print(phrase)
# In the first line, a variable named phrase is created and assigned the
# value "Hello, world" using the = operator. The string "Hello, world" that
# was originally used inside of the parentheses in the print() function is
# replaced with the variable phrase.
# The output Hello, world is displayed when you execute print(phrase)
# because Python looks up the name phrase and finds it has been assigned
# the value "Hello, world".
# If you hadn’t executed phrase = "Hello, world" before executing
# print(phrase), you would have seen a NameError like you did when
# trying to execute print(Hello, world) in the previous section.
# Variable names are case-sensitive, so a variable named phrase is distinct
# from a variable named Phrase (note the capital P).
# Rules for Valid Variable Names
# Variable names can be as long or as short as you like, but there are a
# couple of rules that you must follow. Variable names can only contain
# uppercase and lowercase letters (A–Z, a–z), digits (0–9), and underscores (_).
# However, variable names cannot begin with a digit.
# For example, phrase, string1, _a1p4a, and list_of_names are all valid
# variable names, but 9lives is not
# Python variable names can contain many different valid Unicode
# characters. Unicode is a standard for digitally representing text used
# in most of the world’s writing systems.
# That means variable names can contain letters from non-English alphabets,
# such as decorated letters like é and ü, and
# even Chinese, Japanese, and Arabic symbols.
# However, not every system can display decorated characters, so
# it is a good idea to avoid them if your code is going to be shared
# with people in many different regions.
# You can learn more about Unicode on Wikipedia.
# Python’s support for Unicode is covered in the official Python documentation.
# https://en.wikipedia.org/wiki/Unicode
# Descriptive Names Are Better Than Short Names
# Descriptive variable names are essential, especially for complex programs.
# Often, descriptive names require using multiple words. Don’t
# be afraid to use long variable names.
# In the following example, the value 3600 is assigned to the variable s:
s = 3600
# The name s is totally ambiguous. Using a full word makes it a lot easier
# to understand what the code means:
seconds = 3600
# seconds is a better name than s because it provides more context. But
# it still doesn’t convey the full meaning of the code. Is 3600 the number
# of seconds it takes for some process to finish, or the length of a movie?
# There’s no way to tell.
# The following name leaves no doubt about what the code means:
seconds_per_hour = 3600
# When you read the above code, there is no question that 3600 is the
# number of seconds in one hour. Although seconds_per_hour takes
# longer to type than both the single letter s and the word seconds, the
# pay-off in clarity is massive.
# Although naming variables descriptively means using longer variable
# names, you should avoid names that are excessively long. What “excessively
# long” really means is subjective, but a good rule of thumb is
# to keep variable names to fewer than three or four words.
# Python Variable Naming Conventions
# In many programming languages, it is common to write variable
# names in camelCase like numStudents and listOfNames. The first letter
# of every word, except the first, is capitalized, and all other letters are
# lowercase. The juxtaposition of lower-case and upper-case letters
# look like humps on a camel.
# In Python, however, it is more common to write variable names in
# snake case like num_students and list_of_names. Every letter is lower
# case, and each word is separated by an underscore.
# While there is no hard-and-fast rule mandating that you write your
# variable names in snake case, the practice is codified in a document
# called PEP 8, which is widely regarded as the official style guide for
# writing Python.
# Following the standards outlined in PEP 8 ensures that your Python
# code is readable by a large number of Python programmers. This
# makes sharing and collaborating on code easier for everyone involved.
# Review Exercises
# 1. Using the interactive window, display some text on the screen by
# using the print() function.
print('some text')
# 2. Using the interactive window, display a string of text by saving the
# string to a variable, then reference the string in a print() function
# using the variable name.
some_text = 'Some text'
print(some_text)
# 3. Do each of the first two exercises again by first saving your code in
# a script and running it
# How to Write a Comment
# The most common way to write a comment is to begin a new line in
# your code with the # character. When your code is run, any lines starting
# with # are ignored. Comments that start on a new line are called
# block comments.
# You can also write in-line comments, which are comments that appear on the
# same line as some code. Just put a # at the end of the line
# of code, followed by the text in your comment.
# Here is an example of the hello_world.py script with both kinds of comments
# added in:
# This is a block comment.
phrase = "Hello, world."
print(phrase)  # This is an in-line comment.
# Of course, you can still use the # symbol inside of a string. For instance,
# Python won’t mistake the following for the start of a comment:
print("#1")
# In general, it’s a good idea to keep comments as short as possible, but
# sometimes you need to write more than will reasonably fit on a single
# line. In that case, you can continue your comment on a new line that
# also begins with a # symbol:
# This is my first script.
# It prints the phrase "Hello, world."
# The comments are longer than the script!
phrase = "Hello, world."
print(phrase)
# Besides leaving yourself notes, comments can also be used to comment out code
# while you’re testing a program. In other words,
# adding a # at the beginning of a line of code lets you run your program
# as if that line of code didn’t exist without having to delete any code.
# Conventions and Pet Peeves
# According to PEP 8, comments should always be written in complete
# sentences with a single space between the # and the first word of the
# comment:
# # This comment is formatted to PEP 8.
# #don't do this
# For in-line comments, PEP 8 recommends at least two spaces between
# the code and the # symbol:
# phrase = "Hello, world" # This comment is PEP 8 compliant.
# print(phrase)# This comment isn't.
# A major pet peeve among programmers are comments that describe
# what is already obvious from reading the code. For example, the following
# comment is unnecessary:
# Print "Hello, world"
# print("Hello, world")
