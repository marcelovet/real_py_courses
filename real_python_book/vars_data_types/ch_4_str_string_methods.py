# Strings and String Methods
# Many programmers, regardless of their specialty, deal with text on
# a daily basis. For example, web developers work with text that gets
# input from web forms. Data scientists process text to extract data and
# perform things like sentiment analysis, which can help identify and
# classify opinions in a body of text.
# Collections of text in Python are called strings. Special functions
# called string methods are used to manipulate strings. There are
# string methods for changing a string from lowercase to uppercase,
# removing whitespace from the beginning or end of a string, or replacing
# parts of a string with different text, and many more.
# In this chapter, you will learn how to:
# • Manipulate strings with string methods
# • Work with user input
# • Deal with strings of numbers
# • Format strings for printing
# The String Data Type
# Strings are one of the fundamental Python data types. The term data
# type refers to what kind of data a value represents. Strings are used
# to represent text.
# We say that strings are a fundamental data type because they can’t
# be broken down into smaller values of a different type. Not all data
# types are fundamental. You’ll learn about compound data types, also
# known as data structures, in Chapter 9.
# The string data type has a special abbreviated name in Python: str.
# You can see this by using the type() function, which is used to
# determine the data type of a given value
print('Hello', type('Hello'))
# The output <class 'str'> indicates that the value "Hello, world" is an
# instance of the str data type. That is, "Hello, world" is a string.
# Strings have three properties that you’ll explore in the coming sections:
# 1. Strings contain characters, which are individual letters or symbols.
# 2. Strings have a length, which is the number of characters
# contained in the string.
# 3. Characters in a string appear in a sequence, meaning each character
# has a numbered position in the string.

# String Literals
# As you’ve already seen, you can create a string by surrounding some
# text with quotation marks:
string1 = 'Hello, world'
string2 = "1234"
# Either single quotes (string1) or double quotes (string2) can be used
# to create a string, as long as both quotation marks are the same type.
# Whenever you create a string by surrounding text with quotation
# marks, the string is called a string literal. The name indicates that
# the string is literally written out in your code. All of the strings you
# have seen thus far are string literals.
# Not every string is a string literal. For example, a string captured as user
# input isn’t a string literal because it isn’t explicitly
# written out in the program’s code.
# The quotes surrounding a string are called delimiters because they
# tell Python where a string begins and where it ends. When one type
# of quotes is used as the delimiter, the other type of quote can be used
# inside of the string:
# string3 = "We're #1!"
# string4 = 'I said, "Put it over by the llama."'
# After Python reads the first delimiter, all of the characters after it are
# considered a part of the string until a second matching delimiter is
# read. This is why you can use a single quote in a string delimited by
# double quotes and vice versa.
# If you try to use double quotes inside of a string that is delimited by
# double quotes, you will get an error:
# >>> text = "She said, "What time is it?""
# File "<stdin>", line 1
# text = "She said, "What time is it?""
#                     ^
# SyntaxError: invalid syntax
# Python throws a SyntaxError because it thinks that the string ends after
# the second " and doesn’t know how to interpret the rest of the line.
# A common pet peeve among programmers is the use of mixed
# quotes as delimiters. When you work on a project, it’s a good
# idea to use only single quotes or only double quotes to delimit
# every string.
# Keep in mind that there isn’t really a right or wrong choice! The
# goal is to be consistent, because consistency helps make your
# code easier to read and understand
# Strings can contain any valid Unicode character. For example, the
# string "We're #1!" contains the pound sign (#)
# and "1234" contains numbers. "×Pýŧħøŋ×" is also a valid Python string
# Determine the Length of a String
# The number of characters contained in a string, including spaces, is
# called the length of the string. For example, the string "abc" has a
# length of 3, and the string "Don't Panic" has a length of 11.
# To determine a string’s length, you use Python’s built-in len() function.
print(len('abc'))
# You can also use len() to get the length of a string that’s assigned to a
# variable:
letters = "abc"
num_letters = len(letters)
print(num_letters)
# First, the string "abc" is assigned to the variable letters. Then len()
# is used to get the length of letters and this value is assigned to the
# num_letters variable. Finally, the value of num_letters, which is 3, is
# displayed.

# Multiline Strings
# The PEP 8 style guide recommends that each line of Python code contain no
# more than 79 characters—including spaces.
# PEP 8’s 79-character line-length is recommended because,
# among other things, it makes it easier to read two files sideby-side.
# However, many Python programmers believe forcing
# each line to be at most 79 characters sometimes makes code
# harder to read.
# In this book we will strictly follow PEP 8’s recommended linelength.
# Just know that you will encounter lots of code in the
# real world with longer lines
# Whether you decide to follow PEP 8, or choose a larger number of
# characters for your line-length, you will sometimes need to create
# string literals with more characters than your chosen limit.
# To deal with long strings, you can break the string up across multiple
# lines into a multiline string. For example, suppose you need to fit
# the following text into a string literal:
# “This planet has—or rather had—a problem, which was
# this: most of the people living on it were unhappy for
# pretty much of the time. Many solutions were suggested
# for this problem, but most of these were largely concerned with the
# movements of small green pieces of
# paper, which is odd because on the whole it wasn’t the
# small green pieces of paper that were unhappy.”
# — Douglas Adams, The Hitchhiker’s Guide to the Galaxy
# There are a couple of ways to tackle this. One way is to break the string
# up across multiple lines and put a backslash (\) at the end of all but the
# last line. To be PEP 8 compliant, the total length of the line, including
# the backslash, must be 79 characters or less.
# Here’s how you could write the paragraph as a multiline string using
# the backslash method:
paragraph = "This planet has - or rather had - a problem, which was \
this: most of the people living on it were unhappy for pretty much \
of the time. Many solutions were suggested for this problem, but \
most of these were largely concerned with the movements of small \
green pieces of paper, which is odd because on the whole it wasn't \
the small green pieces of paper that were unhappy."
print(paragraph)
# Notice that you don’t have to close each line with a quotation mark.
# Normally, Python would get to the end of the first line and complain
# that you didn’t close the string with a matching double quote. With a
# backslash at the end, however, you can keep writing the same string
# on the next line.
# When you print() a multiline string that is broken up by backslashes,
# the output displayed on a single line:
long_string = "This multiline string is \
displayed on one line"
print(long_string)
# Multiline strings can also be created using triple quotes as delimiters
# (""" or '''). Here is how you might write a long paragraph using this
# approach:
paragraph = """This planet has - or rather had - a problem, which was
this: most of the people living on it were unhappy for pretty much
of the time. Many solutions were suggested for this problem, but
most of these were largely concerned with the movements of small
green pieces of paper, which is odd because on the whole it wasn't
the small green pieces of paper that were unhappy."""
print(paragraph)
# Triple-quoted strings preserve whitespace. This means that running
# print(paragraph) displays the string on multiple lines just like it is in
# the string literal, including newlines. This may or may not be what
# you want, so you’ll need to think about the desired output before you
# choose how to write a multiline string.
# To see how whitespace is preserved in a triple-quoted string, type the
# following:
print("""An example of a
    string that span across multiple lines
        that also preserves whitespace""")
# Notice how the second and third lines in the output are indented exactly
# the same way they are in the string literal.
# Note
# Triple-quoted strings have a special purpose in Python. They
# are used to document code. You’ll often find them at the top
# of a .py with a description of the code’s purpose. They are also
# used to document custom functions.
# When used to document code, triple-quoted strings are called
# docstrings.
# Review Exercises
# 1. Print a string that uses double quotation marks inside the string.
# 2. Print a string that uses an apostrophe inside the string.
# 3. Print a string that spans multiple lines, with whitespace preserved.
# 4. Print a string that is coded on multiple lines but displays on
# a single line.
print(
    'Exercise 1 - "Print a string that uses double quotation marks \
inside the string".'
)
print(
    "Exercise 2 - Print a string that uses an apostrophe (') \
inside the string."
)
print(
    """Exercise 3 - Print a string that spans multiple lines, with 
    whitespace preserved."""
)
print(
    "Exercise 4 - Print a string that is coded on multiple lines \
but displays on a single line."
)

# Concatenation, Indexing, and Slicing
# Now that you know what a string is and how to declare string literals
# in your code, let’s explore some of the things you can do with strings.
# In this section, you’ll learn about three basic string operations:
# 1. Concatenation, which joins two strings together
# 2. Indexing, which gets a single character from a string
# 3. Slicing, which gets several characters from a string at once

# String Concatenation
# Two strings can be combined, or concatenated, using the + operator:
string1 = 'abra'
string2 = 'cadabra'
magic_string = string1 + string2
print(magic_string)
# In this example, string concatenation occurs on the third line. string1
# and string2 are concatenated using + and the result is assigned to the
# variable magic_string. Notice that the two strings are joined without
# any whitespace between them.
# You can use string concatenation to join two related strings, such as
# joining a first and last name into a full name:
first_name = 'Arthur'
last_name = 'Dent'
full_name = first_name + ' ' + last_name
print(full_name)
# Here string concatenation occurs twice on the same line. first_name
# is concatenated with " ", resulting in the string "Arthur ". Then this
# result is concatenated with last_name to produce the full name "Arthur
# Dent".

# String Indexing
# Each character in a string has a numbered position called an index.
# You can access the character at the Nth position by putting the number N in between two square brackets ([ and ]) immediately after the
# string:
flavor = 'apple pie'
print(flavor[1])
# flavor[1] returns the character at position 1 in "apple pie", which is p.
# Wait, isn’t a the first character of "apple pie"?
# In Python—and most other programming languages—counting
# always starts at zero. To get the character at the beginning of a string,
# you need to access the character at position 0:
print(flavor[0])
# Forgetting that counting starts with zero and trying to access
# the first character in a string with the index 1 results in an oпby-one error.
# Off-by-one errors are a common source of frustration for both
# beginning and experienced programmers alike!
# If you try to access an index beyond the end of a string, Python raises
# an IndexError:
# >>> flavor[9]
# Traceback (most recent call last):
# File "<pyshell#4>", line 1, in <module>
# flavor[9]
# IndexError: string index out of range
# The largest index in a string is always one less than the string’s length.
# Since "apple pie" has a length of nine, the largest index allowed is 8.
# Strings also support negative indices:
print(flavor[-1])
# The last character in a string has index -1, which for "apple pie" is the
# letter e. The second-to-last character i has index -2, and so on.
# Just like positive indices, Python raises an IndexError if you try to access
# a negative index less than the index of the first character in the
# string:
# >>> flavor[-10]
# Traceback (most recent call last):
# File "<pyshell#5>", line 1, in <module>
# flavor[-10]
# IndexError: string index out of range
# Negative indices may not seem useful at first, but sometimes they are
# a better choice than a positive index.
# For example, suppose a string input by a user is assigned to the variable
# user_input. If you need to get the last character of the string, how
# do you know what index to use?
# One way to get the last character of a string is to calculate the final
# index using len():
# final_index = len(user_input) - 1
# last_character = user_input[final_index]
# Getting the final character with the index -1 takes less typing and
# doesn’t require an intermediate step to calculate the final index:
# last_character = user_input[-1]

# String Slicing
# Suppose you need the string containing just the first three letters of
# the string "apple pie". You could access each character by index and
# concatenate them, like this:
first_three_letters = flavor[0] + flavor[1] + flavor[2]
print(first_three_letters)
# If you need more than just the first few letters of a string, getting each
# character individually and concatenating them together is clumsy
# and long-winded. Fortunately, Python provides a way to do this with
# much less typing.
# You can extract a portion of a string, called a substring, by inserting a
# colon between two index numbers inside of square brackets, like this:
first_three_letters = flavor[0:3]
print(first_three_letters)
# flavor[0:3] returns the first three characters of the string assigned to
# flavor, starting with the character with index 0 and going up to, but not
# including, the character with index 3. The [0:3] part of flavor[0:3] is
# called a slice. In this case, it returns a slice of "apple pie". Yum!
# String slices can be confusing because the substring returned by
# the slice includes the character whose index is the first number, but
# doesn’t include the character whose index is the second number.
# To remember how slicing works, you can think of a string as a
# sequence of square slots. The left and right boundary of each slot is
# numbered from zero up to the length of the string, and each slot is
# filled with a character in the string
# The slice [x:y] returns the substring between the boundaries x and y.
# So, for "apple pie", the slice [0:3] returns the string "app", and the slice
# [3:9] returns the string "le pie".
# If you omit the first index in a slice, Python assumes you want to start
# at index 0:
print(flavor[:5])
# Similarly, if you omit the second index in the slice, Python assumes
# you want to return the substring that begins with the character whose
# index is the first number in the slice and ends with the last character
# in the string:
print(flavor[5:])
# If you omit both the first and second numbers in a slice, you get a
# string that starts with the character with index 0 and ends with the last
# character. In other words, omitting both numbers in a slice returns
# the entire string:
print(flavor[:])
# It’s important to note that, unlike string indexing, Python won’t raise
# an IndexError when you try to slice between boundaries before or after
# the beginning and ending boundaries of a string:
print(flavor[:14])
print(flavor[13:15])
# In this example, the first line gets the slice from the beginning of the
# string up to but not including the fourteenth character. The string
# assigned to flavor has length nine, so you might expect Python to throw
# an error. Instead, any non-existent indices are ignored and the entire
# string "apple pie" is returned.
# The second shows what happens when you try to get a slice where
# the entire range is out of bounds. flavor[13:15] attempts to get the
# thirteenth and fourteenth characters, which don’t exist. Instead of
# raising an error, the empty string "" is returned.
# You can use negative numbers in slices. The rules for slices with negative
# numbers are exactly the same as slices with positive numbers
# Just like before, the slice [x:y] returns the substring between the
# boundaries x and y. For instance, the slice [-9:-6] returns the first
# three letters of the string "apple pie":
print(flavor[-9:-6])
# Notice, however, that the right-most boundary does not have a negative index.
# The logical choice for that boundary would seem to be the
# number 0, but that doesn’t work:
# Instead of returning the entire string, [-9:0] returns the empty
# string "". This is because the second number in a slice must correspond
# to a boundary that comes after the boundary corresponding
# to the first number, but both -9 and 0 correspond to the left-most
# boundary in the figure.
# If you need to include the final character of a string in your slice, you
# can omit the second number:
print(flavor[-9:])
# It is possible to slice in steps using a second : and defining the number of
# of characters to jump
print(flavor[::2])
# This make possible to reverse the intire string with a -1 step
print(flavor[::-1])

# Strings Are Immutable
# To wrap this section up, let’s discuss an important property of string
# objects. Strings are immutable, which means that you can’t change
# them once you’ve created them. For instance, see what happens when
# you try to assign a new letter to one particular character of a string:
# >>> word = "goal"
# >>> word[0] = "f"
# Traceback (most recent call last):
# File "<pyshell#16>", line 1, in <module>
# word[0] = "f"
# TypeError: 'str' object does not support item assignment
# Python throws a TypeError and tells you that str objects don’t support
# item assignment.
# Note
# The term str is Python’s internal name for the string data type.
# If you want to alter a string, you must create an entirely new string.
# To change the string "goal" to the string "foal", you can use a string
# slice to concatenate the letter "f" with everything but the first letter of
# the word "goal":
word = 'goal'
print(word)

word = 'f' + word[1:]
print(word)

# Review Exercises
# 1. Create a string and print its length using the len() function.
# 2. Create two strings, concatenate them, and print the resulting
# string.
# 3. Create two strings and use concatenation to add a space inbetween them.
# Then print the result.
# 4. Print the string "zing" by using slice notation on the string
# "bazinga" to specify the correct range of characters.
exercise_1_string = 'My string'
print(len(exercise_1_string))

exercise_2_string = 'contatenated with a second string'
exercise_2_concatenate = exercise_1_string + exercise_2_string
print(exercise_2_concatenate)

exercise_3_string = exercise_1_string + ' ' + exercise_2_string
print(exercise_3_string)

exercise_4_string = 'bazinga'
print(exercise_4_string[2:6])

# Manipulate Strings With Methods
# Strings come bundled with special functions called string methods
# that can be used to work with and manipulate strings. There are
# numerous string methods available, but we’ll focus on some of the most
# commonly used ones.
# In this section, you will learn how to:
# • Convert a string to upper or lower case
# • Remove whitespace from string
# • Determine if a string begins and ends with certain characters

# Converting String Case
# To convert a string to all lower case letters, you use the string’s .lower()
# method. This is done by tacking .lower() on to the end of the string
# itself:
picard = 'Jean Luc Picard'
print(picard.lower())
# The dot (.) tells Python that what follows is the name of a method—
# the lower() method in this case.
# The opposite of the .lower() method is the .upper() method, which converts
# every character in a string to upper case:
print(picard.upper())
# Compare the .upper() and .lower() string methods to the general
# purpose len() function you saw in the last section. Aside from the
# different results of these functions, the important distinction here is
# how they are used.
# The len() function is a stand-alone function. If you want to determine
# the length of the loud_voice string, you call the len() function directly,
# like this:
print(len(picard))
# On the other hand, .upper() and .lower() must be used in conjunction
# with a string. They do not exist independently.

# Removing Whitespace From a String
# Whitespace is any character that is printed as blank space. This
# includes things like spaces and line feeds, which are special characters
# that move output to a new line.
# Sometimes you need to remove whitespace from the beginning or end
# of a string. This is especially useful when working with strings that
# come from user input, where extra whitespace characters may have
# been introduced by accident.
# There are three string methods that you can use to remove whitespace
# from a string:
# 1. .rstrip()
# 2. .lstrip()
# 3. .strip()
# .rstrip() removes whitespace from the right side of a string:
picard = picard + '    '
print(picard, 'aqui termina a str anterior')
print(picard.rstrip(), 'agora com .rstrip()')
# In this example, the string "Jean-luc Picard " has five trailing
# spaces. Python doesn’t remove any trailing spaces in a string automatically
# when the string is assigned to a variable. The .rstrip() method
# removes trailing spaces from the right-hand side of the string and returns
# a new string "Jean-luc Picard", which no longer has the spaces
# at the end.
# The .lstrip() method works just like .rstrip(), except that it removes
# whitespace from the left-hand side of the string.
# To remove whitespace from both the left and the right sides of the
# string at the same time, use the .strip() method:
picard = '    ' + picard
print(picard, 'aqui termina a str anterior')
print(picard.strip(), 'agora com .strip()')

# Determine if a String Starts or Ends With a
# Particular String
# When you work with text, sometimes you need to determine if a given
# string starts with or ends with certain characters. You can use two
# string methods to solve this problem: .startswith() and .endswith().
# Let’s look at an example. Consider the string "Enterprise". Here’s how
# you use .startswith() to determine if the string starts with the letters
# e and n:
starship = 'Enterprise'
print(starship.startswith('en'))

# You must tell .startswith() what characters to search for by providing
# a string containing those characters. So, to determine if "Enterprise"
# starts with the letters e and n, you call .startswith("en"). This returns
# False. Why do you think that is?
# If you guessed that .startswith("en") returns False because "Enterprise"
# starts with a capital E, you’re absolutely right! The .startswith()
# method is case-sensitive. To get .startswith() to return True, you
# need to provide it with the string "En" or used with .lower()
print(starship.startswith('En'))
print(starship.lower().startswith('en'))

# The .endswith() method is used to determine if a string ends with
# certain characters:
print(starship.endswith('rise'))
# The True and False values are not strings. They are a special kind
# of data type called a Boolean value.

# String Methods and Immutability
# Recall from the previous section that strings are immutable—they
# can’t be changed once they have been created. Most string methods
# that alter a string, like .upper() and .lower(), actually return copies of
# the original string with the appropriate modifications.
# When you call name.upper(), nothing about name actually changes. If
# you need to keep the result, you need to assign it to a variable
name = "Picard"
print(name)

name = name.upper()
print(name)

# 1. Write a script that converts the following strings to lowercase:
# "Animals", "Badger", "Honey Bee", "Honeybadger". Print each lowercase
# string on a separate line.
print('Animals'.lower())
print('Badger'.lower())
print('Honey Bee'.lower())
print('Honeybadger'.lower())
# 2. Repeat Exercise 1, but convert each string to uppercase instead of
# lowercase.
print('Animals'.upper())
print('Badger'.upper())
print('Honey Bee'.upper())
print('Honeybadger'.upper())
# 3. Write a script that removes whitespace from the following strings:
string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "
string1 = string1.strip()
string2 = string2.strip()
string3 = string3.strip()
# Print out the strings with the whitespace removed.
print(string1, string2, string3, sep='\n')
# 4. Write a script that prints out the result of .startswith("be") on each
# of the following strings:
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"
str_list = [string1, string2, string3, string4]
for string in str_list:
    print(string.startswith('be'))
# 5. Using the same four strings from Exercise 4, write a script that
# uses string methods to alter each string so that .startswith("be")
# returns True for all of them.
for string in str_list:
    print(string.strip().lower().startswith('be'))


# 4.4 Interact With User Input
# Now that you’ve seen how to work with string methods, let’s make
# things interactive. In this section, you will learn how to get some input
# from a user with the input() function. You’ll write a program that asks
# a user to input some text and then display that text back to them in
# uppercase.
# input() returns any text entered by the user as a string.
# To make input() a bit more user friendly, you can give it a prompt to
# display to the user. The prompt is just a string that you put in between
# the parentheses of input(). It can be anything you want: a word, a
# symbol, a phrase—anything that is a valid Python string.
# The input() function displays the prompt and waits for the user to type
# something on their keyboard. When the user hits Enter, input()
# returns their input as a string that can be assigned to a variable and
# used to do something in your program.
prompt = "Hey, what's up? "
user_input = input(prompt)
print('You said:', user_input)
# Once you have input from a user, you can do something with it. For
# example, the following script takes user input and converts it to
# uppercase with .upper() and prints the result:
response = input("What should I shout? ")
shouted_response = response.upper()
print("Well, if you insist...", shouted_response)


# Challenge: Pick Apart Your User’s Input
# Write a script named first_letter.py that first prompts the user for
# input by using the string "Tell me your password:" The script should
# then determine the first letter of the user’s input, convert that letter
# to upper-case, and display it back.
# For example, if the user input is "no" then the program should respond
# like this:
# The first letter you entered was: N
# For now, it’s okay if your program crashes when the user enters nothing
# as input—that is, they just hit Enter instead of typing something in.
# You’ll learn about a couple of ways you can deal with this situation in
# an upcoming chapter.
tell_me_secret = 'Tell me your password: '
user_input = input(tell_me_secret)
if not user_input:
    print("Ok it's your choice")
else:
    print('The first letter you entered was:', user_input[0].upper())

# Working With Strings and Numbers
# When you get user input using the input() function, the result is always
# a string. There are many other times when input is given to a program
# as a string. Sometimes those strings contain numbers that need to be
# fed into calculations.
# In this section you will learn how to deal with strings of numbers. You
# will see how arithmetic operations work on strings, and how they often
# lead to surprising results. You will also learn how to convert between
# strings and number types.

# Strings and Arithmetic Operators
# You’ve seen that string objects can hold many types of characters,
# including numbers. However, don’t confuse numerals in a string with
# actual numbers. For instance, try this bit of code out
num = '2'
print(num + num)

# Strings can be “multiplied” by a number as long as that number is
# an integer, or whole number. Type the following
num = '12'
print(num * 3)

# num * 3 concatenates the string "12" with itself three times and returns
# the string "121212". To compare this operation to arithmetic with
# numbers, notice that "12" * 3 = "12" + "12" + "12". In other words,
# multiplying a string by an integer n concatenates that string with itself n
# times.
# What do you think happens if you use the * operator between two
# strings? Type "12" * "3" in the interactive window and press Enter:
# >>> "12" * "3"
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: can't multiply sequence by non-int of type 'str'
# Python raises a TypeError and tells you that you can’t multiply a
# sequence by a non-integer. When the * operator is used with a string
# on either the left or the right side, it always expects an integer on the
# other side.
# A sequence is any Python object that supports accessing
# elements by index. Strings are sequences.
# What do you think happens when you try to add a string and a number?
# >>> "3" + 3
# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str
# Again, Python throws a TypeError because the + operator expects both
# things on either side of it to be of the same type. If any one of the
# objects on either side of + is a string, Python tries to perform string
# concatenation. Addition will only be performed if both objects are
# numbers. So, to add "3" + 3 and get 6, you must first convert the
# string "3" to a number.
# Again, Python throws a TypeError because the + operator expects both
# things on either side of it to be of the same type. If any one of the
# objects on either side of + is a string, Python tries to perform string
# concatenation. Addition will only be performed if both objects are
# numbers. So, to add "3" + 3 and get 6, you must first convert the
# string "3" to a number.

# Converting Strings to Numbers
# The TypeError errors you saw in the previous section highlight a
# common problem encountered when working with user input: type
# mismatches when trying to use the input in an operation that requires a
# number and not a string.
# Let’s look at an example.
num = input("Enter a number to be doubled: ")
doubled_num = num * 2
print(doubled_num)

# When you enter a number, such as 2, you expect the output to be 4, but
# in this case, you get 22. Remember, input() always returns a string, so
# if you input 2, then num is assigned the string "2", not the integer 2.
# Therefore, the expression num * 2 returns the string "2" concatenated
# with itself, which is "22".
# To perform arithmetic on numbers that are contained in a string, you
# must first convert them from a string type to a number type. There
# are two ways to do this: int() and float().
# int() stands for integer and converts objects into whole numbers,
# while float() stands for сoating-point number and converts objects
# into numbers with decimal points
print(int('12'))
print(float('12'))
# Notice how float() adds a decimal point to the number. Floating-point
# numbers always have at least one decimal place of precision. For
# this reason, you can’t change a string that looks like a floating-point
# number into an integer because you would lose everything after the
# decimal point:
# >>> int("12.0")
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '12.0'
# Even though the extra 0 after the decimal place doesn’t add any value
# to the number, Python won’t change 12.0 into 12 because it would
# result in the loss of precision.
# Let’s revisit the script from the beginning of this section and see how
# to fix it. Here’s the script again:
# num = input("Enter a number to be doubled: ")
# doubled_num = num * 2
# print(doubled_num)
# The issue lies in the line doubled_num = num * 2 because num references
# a string and 2 is an integer. You can fix the problem by wrapping num
# with either int() or float(). Since the prompts asks the user to input a
# number, and not specifically an integer, let’s convert num to a floating
# point number:
num = input("Enter a number to be doubled: ")
doubled_num = float(num) * 2
print(doubled_num)
# Now when you run this script and input 2, you get 4.0 as expected. Try
# it out!

# Converting Numbers to Strings
# Sometimes you need to convert a number to a string. You might do
# this, for example, if you need to build a string from some pre-existing
# variables that are assigned to numeric values.
# As you’ve already seen, the following produces a TypeError:
# >>> num_pancakes = 10
# >>> "I am going to eat " + num_pancakes + " pancakes."
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str

# Since num_pancakes is a number, Python can’t concatenate it with the
# string "I'm going to eat". To build the string, you need to convert
# num_pancakes to a string using str():
num_pancakes = 10
print("I am going to eat " + str(num_pancakes) + " pancakes")
# You can also call str() on a number literal:
print("I am going to eat " + str(10) + " pancakes")
# str() can even handle arithmetic expressions:
total_pancakes = 10
pancakes_eaten = 5
print("Only " + str(total_pancakes - pancakes_eaten) + " pancakes")
# You’re not limited to numbers when using str(). You can pass it all
# sorts of objects to get their string representations:
# >>> str(print)
# '<built-in function print>'
# >>> str(int)
# "<class 'int'>"
# >>> str(float)
# "<class 'float'>"
# These examples may not seem very useful, but they illustrate how
# flexible str() is
# 1. Create a string containing an integer, then convert that string into
# an actual integer object using int(). Test that your new object is
# a number by multiplying it by another number and displaying the
# result.
str_integer = '2'
my_integer = int(str_integer)
print(my_integer * 4)
# 2. Repeat the previous exercise, but use a floating-point number and
# float().
str_float = '2.2'
my_float = float(str_float)
print(my_float * 8)
# 3. Create a string object and an integer object, then display them side
# by-side with a single print statement by using the str() function.
my_int = 23
print(str_integer, my_int)
# 4. Write a script that gets two numbers from the user using the
# input() function twice, multiplies the numbers together, and
# displays the result. If the user enters 2 and 4, your program should
# print the following text:
# The product of 2 and 4 is 8.0.
first_num = input('Type your first number: ')
first_num = int(first_num)
second_num = input('Type your second number: ')
second_num = int(second_num)
product = first_num * second_num
print('The product of', first_num, 'and', second_num, 'is', product)

# Streamline Your Print Statements
# Suppose you have a string name = "Zaphod" and two integers heads = 2
# and arms = 3. You want to display them in the following line: Zaphod
# has 2 heads and 3 arms. This is called string interpolation, which is
# just a fancy way of saying that you want to insert some variables into
# specific locations in a string.
# You’ve already seen two ways of doing this. The first involves using
# commas to insert spaces between each part of the string inside of a
# print() function
# Another way to do this is by concatenating the strings with
# the + operator:
name = 'Zaphod'
heads = 2
arms = 3
print(name + " has " + str(heads) + " heads and " + str(arms) + " arms")
# Both techniques produce code that can be hard to read. Trying to keep
# track of what goes inside or outside of the quotes can be tough.
# Fortunately, there’s a third way of combining strings: formatted string
# literals, more commonly known as f-strings.
# The easiest way to understand f-strings is to see them in action. Here’s
# what the above string looks like when written as an f-string:
print(f"{name} has {heads} heads and {arms} arms")
# There are two important things to notice about the above examples:
# 1. The string literal starts with the letter f before the opening
# quotation mark
# 2. Variable names surrounded by curly braces ({and }) are replaced
# with their corresponding values without using str()
# You can also insert Python expressions in between the curly braces.
# The expressions are replaced with their result in the string:
n = 3
m = 4
print(f"{n} times {m} is {n * m}")
# It is a good idea to keep any expressions used in an f-string as
# simple as possible. Packing in a bunch of complicated expressions into a
# string literal can result in code that is difficult to read and difficult to
# maintain.
# f-strings are only available in Python version 3.6 and above.
# In earlier versions of Python, the .format() method can be used to get the
# same results. Returning to the Zaphod example, you can use .format()
# method to format the string like this:
# "{} has {} heads and {} arms".format(name, heads, arms)
# f-strings are shorter, and sometimes more readable, than using .format().
# You will see f-strings used throughout this book.
# For an in-depth guide to f-strings and comparisons to other string
# formatting techniques, check out the Python 3’s f-Strings: An Improved
# String Formatting Syntax(Guide) on realpython.com
# https://realpython.com/python-f-strings/
# There is also another way to print formatted strings: using the
# % operator. You might see this in code that you find elsewhere,
# and you can read about how it works here if you’re curious.
# Keep in mind that this style has been phased out entirely in
# Python 3. Just be aware that it exists and you may see it in
# legacy Python code bases.
# https://docs.python.org/3/library/stdtypes.html#old-string-formatting
# 1. Create a float object named weight with the value 0.2, and create
# a string object named animal with the value "newt". Then use these
# objects to print the following string using only string concatenation:
# 0.2 kg is the weight of the newt.
weight = 0.2
animal = 'newt'
print(weight, 'kg is the weight of the', animal)
# 2. Display the same string by using the .format() method and empty
# {} place-holders.
print("{} kg is the weight of the {}".format(weight, animal))
# 3. Display the same string using an f-string.
print(f'{weight} kg is the weight of the {animal}')


# Find a String in a String
# One of the most useful string methods is .find(). As its name implies,
# you can use this method to find the location of one string in another
# string—commonly referred to as a substring.
# To use .find(), tack it to the end of a variable or a string literal and
# pass the string you want to find in between the parentheses:
phrase = "the surprise is in here somewhere"
print(phrase.find("surprise"))
# The value that .find() returns is the index of the first occurrence of the
# string you pass to it. In this case, "surprise" starts at the fifth character
# of the string "the surprise is in here somewhere" which has index 4
# because counting starts at 0.
print(phrase[phrase.find("surprise"):])
# If .find() doesn’t find the desired substring, it will return -1 instead
phrase = "the surprise is in here somewhere"
print(phrase.find("eyjafjallajökull"))
# You can call string methods on a string literal directly, so in this case,
# you don’t need to create a new string
# "the surprise is in here somewhere".find("surprise")
# Keep in mind that this matching is done exactly, character by character,
# and is case-sensitive. For example, if you try to find "SURPRISE",
# the .find() method returns - 1:
print("the surprise is in here somewhere".find("SURPRISE"))
# If a substring appears more than once in a string, .find() only returns
# the index of the first appearance, starting from the beginning of the
# string
print("I put a string in your string".find("string"))
# There are two instances of the "string" in "I put a string in your
# string". The first starts at index 8, and the second at index 23. .find()
# returns 8, which is the index of the first instance of "string".
# The .find() method only accepts a string as its input. If you want to
# find an integer in a string, you need to pass the integer to .find() as a
# string. If you do pass something other than a string to .find(), Python
# raises a TypeError:
# >> > "My number is 555-555-5555".find(5)
# Traceback(most recent call last):
# File "<stdin>", line 1, in <module >
# TypeError: must be str, not int
print("My number is 555-555-5555".find("5"))
# Sometimes you need to find all occurrences of a particular substring
# and replace them with a different string.
# Since .find() only returns the index of the first occurrence of a substring,
# you can’t easily use it to perform this operation.
# Fortunately, string objects have a .replace()
# method that replaces each instance of a substring with another string.
# Just like .find(), you tack .replace() on to the end of a variable or
# string literal. In this case, though, you need to put two strings inside
# of the parentheses in .replace() and separate them with a comma. The
# first string is the substring to find, and the second string is the string
# to replace each occurrence of the substring with .
# For example, the following code shows how to replace each
# occurrence of "the truth" in the string "I'm telling you the truth
# nothing but the truth" with the string "lies":
my_story = "I'm telling you the truth; nothing but the truth!"
print(my_story.replace("the truth", "lies"))
# Since strings are immutable objects, .replace() doesn’t alter my_story.
# If you immediately type my_story into the interactive window after
# running the above example, you’ll see the original string, unaltered:
print(my_story)
# To change the value of my_story, you need to reassign to it the new
# value returned by .replace():
my_story = my_story.replace("the truth", "lies")
print(my_story)
# "I'm telling you lies; nothing but lies!"
# .replace() can only replace one substring at a time, so if you want to
# replace multiple substrings in a string you need to use .replace()
# multiple times:
text = "some of the stuff"
new_text = text.replace("some of", "all")
new_text = new_text.replace("stuff", "things")
print(new_text)
# 'all the things'
# You’ll have some fun with .replace() in the challenge in the next section.
# 1. In one line of code, display the result of trying to .find() the
# substring "a" in the string "AAA". The result should be - 1.
print('AAA'.find('a'))
# 2. Replace every occurrence of the character "s" with "x" in the string
# "Somebody said something to Samantha.".
print("Somebody said something to Samantha.".lower().replace('s', 'x'))
# 3. Write and test a script that accepts user input using the input()
# function and displays the result of trying to .find() a particular
# letter in that input.
print('Location of the first occurrence')
user_phrase = input('Enter your phrase: ')
input_text = "Enter the letter and I will find it's first occurrence in the" \
    " phrase: "
letter_to_locate = input(input_text)
location = user_phrase.find(letter_to_locate)
if location == -1:
    new_txt = f'{letter_to_locate} not found in the phrase'
else:
    new_txt = f'The first occurrence of {letter_to_locate} in the phrase' \
        f' was in {location} index'
print(new_txt)

# Challenge: Turn Your User Into a
# L33t H4x0r
# Write a script called translate.py that asks the user for some input
# with the following prompt:
user_input = input('Enter some text: ')
#     Enter some text: . Then use the .replace()
# method to convert the text entered by the user into “leetspeak” by
# making the following changes to lower-case letters:
# • The letter a becomes 4
# • The letter b becomes 8
# • The letter e becomes 3
# • The letter l becomes 1
# • The letter o becomes 0
# • The letter s becomes 5
# • The letter t becomes 7
letters_to_replace = ['a', 'b', 'e', 'l', 'o', 's', 't']
replacement = ['4', '8', '3', '1', '0', '5', '7']
text = user_input
for idx in range(len(letters_to_replace)):
    text = text.replace(letters_to_replace[idx], replacement[idx])
print(text)
# Your program should then display the resulting string as output.
# Below is a sample run of the program
# Enter some text: I like to eat eggs and spam.
# I 1ik3 70 347 3gg5 4nd 5p4m.
# Additional Resources
# To learn more, check out the following resources:
# • Python String Formatting Best Practices
# https://realpython.com/python-string-formatting/
# • Splitting, Concatenating, and Joining Strings in Python
# https://realpython.com/python-string-split-concatenate-join/
# • Recommended resources on realpython.com
# https://realpython.com/python-basics/resources/#recommended-resources
