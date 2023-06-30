# Tuples, Lists, and Dictionaries
# So far, you have been working with fundamental data types like str,
# int, and float. Many real-world problems are easier to solve when
# simple data types are combined into more complex data structures.
# A data structure models a collection of data, such as a list of numbers,
# a row in a spreadsheet, or a record in a database. Modeling the
# data that your program interacts with using the right data structure is
# often the key to writing simple and effective code.
# Python has three built-in data structures that are the focus of this
# chapter: tuples, lists, and dictionaries.
# In this chapter, you will learn:
# • How to work with tuples, lists, and dictionaries
# • What immutability is and why it is important
# • When to use different data structures

# Tuples Are Immutable Sequences
# Perhaps the simplest compound data structure is a sequence of items.
# A sequence is an ordered list of values. Each element in a sequence
# is assigned an integer, called an index, that determines the order in
# which the values appear. Just like strings, the index of the first value
# in a sequence is 0.
# For example, the letters of the English alphabet form a sequence
# whose first element is A and last element is Z. Strings are also
# sequences. The string "Python" has six elements, starting with "P" at
# index 0, and "n" at index 5.
# Some real-world examples of sequences include the values emitted by
# a sensor every second, the sequence of a student’s test scores, or the
# sequence of daily stock values for some company over a period of time.
# In this section, you’ll learn how to use Python’s built-in tuple data type
# to create sequences of values.

# What is a Tuple?
# The word tuple comes from mathematics, where it is used to describe
# a finite ordered sequence of values.
# Usually, mathematicians write tuples by listing each element, separated
# by a comma, inside a pair of parentheses. (1, 2, 3) is a tuple
# containing three integers.
# Tuples are ordered because their elements appear in an ordered fashion.
# The first element of (1, 2, 3) is 1, the second element is 2, and
# the third is 3.
# Python borrows both the name and the notation for tuples from mathematics
# How to Create a Tuple
# There are a few ways to create a tuple in Python. We will cover two of
# them:
# 1. Tuple literals
# 2. The tuple() built-in
# Tuple Literals
# Just like a string literal is a string that is explicitly created by
# surrounding some text with quotes, a tuple literal is a tuple that is
# written out
# explicitly as a comma-separated list of values surrounded by parentheses.
# Here’s an example of a tuple literal:
import random

my_first_tuple = (1, 2, 3)
# This creates a tuple containing the integers 1, 2, and 3, and assigns it
# to the name my_first_tuple.
# You can check that my_first_tuple is a tuple using type():
print(type(my_first_tuple))
# Unlike strings, which are sequences of characters, tuples may contain
# any type of value, including values of different types. The tuple (1,
# 2.0, "three") is perfectly valid.
# There is a special tuple that doesn’t contain any values. This tuple is
# called the empty tuple and can be created by typing two parentheses
# without anything between them:
empty_tuple = ()
# At first glance, the empty tuple may seem like a strange and useless
# concept, but it is actually quite practical.
# For example, suppose you are asked to provide a tuple containing all
# the integers that are both even and odd. No such integer exists, but
# the empty tuple allows you to provide the requested tuple.
# How do you think you create a tuple with exactly one element? Try
# out the following in IDLE:
x = (1)
print(type(x))
# >>> type(x)
# <class 'int'>
# When you surround a value with parentheses, but don’t include any
# commas, Python interprets the value not as a tuple but as the type of
# value inside the parentheses. So, in this case, (1) is a just a weird way
# of writing the integer 1.
# To create the tuple containing the single value 1, you need to include
# a comma after the 1:
x = (1,)
print(type(x))
# A tuple containing a single element might seem as a strange as the
# empty tuple. Couldn’t you just drop all this tuple business and just
# use the value itself?
# It all depends on the problem you are solving.
# If you are asked to provide a tuple containing all prime numbers that
# are also even, you must provide the tuple (2,) since 2 is the only even
# prime number. The value 2 isn’t a good solution because it isn’t a tuple.
# This might seem overly pedantic, but programming often involves a
# certain amount of pedantry. Computers are, after all, the ultimate
# pedants.
# The tuple() Built-In
# You can also use the tuple() built-in to create a tuple from another
# sequence type, such as a string:
# >>> tuple("Python")
# ('P', 'y', 't', 'h', 'o', 'n')
# tuple() only accepts a single parameter, so you can’t just list the values
# you want in the tuple as individual arguments. If you do, Python raises
# a TypeError:
# >>> tuple(1, 2, 3)
# Traceback (most recent call last):
# File "<pyshell#0>", line 1, in <module>
# tuple(1, 2, 3)
# TypeError: tuple expected at most 1 arguments, got 3
# You will also get a TypeError if the argument passed to tuple() can’t be
# interpreted as a list of values:
# >>> tuple(1)
# Traceback (most recent call last):
# File "<pyshell#1>", line 1, in <module>
# tuple(1)
# TypeError: 'int' object is not iterable
# The word iterable in the error message indicates that a single integer
# can’t be iterated, which is to say that the integer data type doesn’t
# contain multiple values that can be accessed one-by-one.
# The single parameter of tuple() is optional, though, and leaving it out
# produces an empty tuple:
# >>> tuple()
# ()
# However, most Python programmers prefer to use the shorter () for
# creating an empty tuple.

# Similarities Between Tuples and Strings
# Tuples and strings have a lot in common. Both are sequence types
# with a finite length, support indexing and slicing, are immutable, and
# can be iterated over in a loop.
# The main difference between strings and tuples is that the elements
# of tuples can be any kind of value you like, whereas strings can only
# contain characters.
# Let’s look at some of the parallels between strings in tuples in more
# depth.
# Tuples Have a Length
# Both strings and tuples have a length. The length of a string is the
# number of characters in it. The length of a tuple is the number of
# elements it contains.
# Just like strings, the len() function can be used to determine the
# length of a tuple:
numbers = (1, 2, 3)
print(len(numbers))

# Tuples Support Indexing and Slicing
# Recall from Chapter 4 that you can access a character in a string using
# index notation:
# >>> name = "David"
# >>> name[1]
# 'a'
# The index notation [1] after the variable name tells Python to get the
# character at index 1 in the string "David". Since counting starts at 0,
# the character at index 1 is the letter "a".
# Tuples also support index notation:
values = (3, 4, 5, 6, 7, 8, 9)
print(values[2])
# Another feature that strings and tuples have in common is slicing.
# Recall that you can extract a substring from a string using slicing notation:
# >>> name = "David"
# >>> name[2:4]
# "vi"
# The slice notation [2:4] after the variable name creates a new string
# containing the characters in name starting at position 2 and up to, but
# not including, the character at position 4.
# Slicing notation also works with tuples:
print(values[2:4])
# The slice values[2:4] creates a new tuple containing the all integers in
# values starting at position 2 and up to, but not including, the integer
# at position 4.
# The same rules governing string slices also apply to tuple slices
# Tuples Are Immutable
# Like strings, tuples are immutable. This means you can’t change the
# value of an element of a tuple once it has been created.
# If you do try to change the value at some index of a tuple, Python will
# raise a TypeError:
# >>> values[0] = 2
# Traceback (most recent call last):
# File "<pyshell#1>", line 1, in <module>
# values[0] = 2
# TypeError: 'tuple' object does not support item assignment

# Tuples Are Iterable
# Just like strings, tuples are iterable, so you can loop over them:
vowels = ('a', 'e', 'i', 'o', 'u')
for vowel in vowels:
    print(vowel.upper())
# The for loop in this example works just like the for loops you saw in
# Chapter 6 that loop over a range() of numbers.
# On the first step of the loop, the value "a" is extracted from the
# tuple vowels. It is converted to an upper case letter using the .upper()
# string method you learned about in Chapter 4, and then displayed
# with print().
# The next step of the loop extracts the value "e", converts it to upper
# case, and prints it. This continues for each of the values "i", ”o", and "u".
# Now that you’ve seen how to create tuples and some of the basic operations
# they support, let’s look at some common use cases.

# Tuple Packing and Unpacking
# There is a third, although less common, way of creating a tuple. You
# can type out a comma-separated list of values and leave off the parentheses:
coordinates = 4.21, 9.29
print(type(coordinates))
# <class 'tuple'>
# It looks like two values are being assigned to the single variable
# coordinates. In a sense, they are, although the result is that both
# values are packed into a single tuple. You can verify that coordinates
# is indeed a tuple with type().
# If you can pack values into a tuple, it only makes sense that you can
# unpack them as well:
x, y = coordinates
print(f'{x=}, {y=}')
# Here the values contained in the single tuple coordinates are unpacked into
# two distinct variables x and y.
# By combining tuple packing and unpacking, you can make multiple
# variable assignments in a single line:
# name, age, occupation = "David", 34, "programmer"
# This works because first, on the right hand side of the assignment, the
# values "David", 34, and "programmer" are packed into a tuple. Then the
# values are unpacked into the three variables name, age, and programmer,
# in that order.
# Keep in mind that the number of variable names on the left of the
# assignment expression must equal the number of values in the tuple
# on the right hand side, otherwise Python will rase a ValueError:
# >>> a, b, c, d = 1, 2, 3
# Traceback (most recent call last):
# File "<pyshell#0>", line 1, in <module>
# a, b, c, d = 1, 2, 3
# ValueError: not enough values to unpack (expected 4, got 3)
# The error message here tells you that the tuple on the right hand side
# doesn’t have enough values to unpack into the four variable names.
# Python also raises a ValueError if the number of values in the tuple
# exceeds the number of variable names:
# >>> a, b, c = 1, 2, 3, 4
# Traceback (most recent call last):
# File "<pyshell#1>", line 1, in <module>
# a, b, c = 1, 2, 3, 4
# ValueError: too many values to unpack (expected 3)
# Now the error message indicates that there are too many values in the
# tuple to unpack into three variables.

# Checking Existence of Values With in
# You can check whether or not a value is contained in a tuple with the
# in keyword.
vowels = ("a", "e", "i", "o", "u")
print("o" in vowels)
# True
# >>> "x" in vowels
# False
# If the value to the left of in is contained in the tuple to the right of in,
# the result is True. Otherwise, the result is False.
# Returning Multiple Values From a Function
# One common use of tuples is to return multiple values from a single
# function.


def adder_subtractor(num1, num2):
    return (num1 + num2, num1 - num2)


print(adder_subtractor(3, 2))
# The function adder_subtractor() has two parameters, num1 and num2, and
# returns a tuple whose first element is the sum of the two numbers, and
# whose second element is the difference.
# Strings and tuples are just two of Python’s built-in sequence types.
# Both are immutable and iterable and can be used with index and
# slicing notation.
# In the next section, you’ll learn about a third sequence type with one
# very big difference from strings and tuples: mutability.

# Review Exercises
# 1. Create a tuple literal named cardinal_numbers that holds the strings
# "first", "second" and "third", in that order.
cardinal_numbers = ('first', 'second', 'third')
# 2. Using index notation and print(), display the string at index 1 in
# cardinal_numbers.
print(cardinal_numbers[1])
# 3. Unpack the values in cardinal_numbers into three new strings
# named position1, position2 and position3 in a single line of code,
# then print each value on a separate line.
position1, position2, position3 = cardinal_numbers
print(position1, position2, position3, sep='\n')
# 4. Create a tuple called my_name that contains the letters of your name
# by using tuple() and a string literal.
my_name = tuple('Marccelo')
# 5. Check whether or not the character "x" is in my_name using the in
# keyword.
print('x' in my_name)
# 6. Create a new tuple containing all but the first letter in my_name using
# slicing notation.
new_tuple = my_name[1:]
print(new_tuple)

# Lists Are Mutable Sequences
# The list data structure is another sequence type in Python. Just like
# strings and tuples, lists contain items that are indexed by integers,
# starting with 0.
# On the surface, lists look and behave a lot like tuples. You can use
# index and slicing notation with lists, check for the existence of an element
# using in, and iterate over lists with a for loop.
# Unlike tuples, however, lists are mutable, meaning you can change
# the value at an index even after the list has been created.
# In this section, you will learn how to create lists and compare them
# with tuples.

# Creating Lists
# A list literal looks almost exactly like a tuple literal, except that it is
# surrounded with square brackets ([ and ]) instead of parentheses:
colors = ['red', 'yellow', 'green', 'blue']
print(type(colors))
# When you inspect a list, Python displays it as a list literal:
print(colors)
# Like tuples, lists values are not required to be of the same type. The
# list literal ["one", 2, 3.0] is perfectly valid.
# Aside from list literals, you can also use the list() built-in to create a
# new list object from any other sequence. For instance, the tuple (1,
# 2, 3) can be passed to list() to create the list [1, 2, 3]:
print(list((1, 2, 3)))
# You can even create a list from a string:
print(list('Python'))
# Each letter in the string becomes an element of the list.
# There is more useful way to create a list from a string. You can create
# a list from a string of a comma-separated list of items using the string
# object’s .split() method:
groceries = 'eggs, milk, cheese'
groceries = groceries.split(', ')
print(groceries)
# The string argument passed to .split() is called the separator. By
# changing the separator you can split strings into lists in numerous
# ways:
# Split string on semi-colons
print("a;b;c".split(";"))
# Split string on spaces
print("The quick brown fox".split(" "))
# Split string on multiple characters
print("abbaabba".split("ba"))
# In the last example above, the string is split around occurrences of the
# substring "ba", which occurs first at index 2 and again at index 6. The
# separator has two characters, only the characters at indices 1, 2, 5, and
# 6 become elements of the list.
# .split() always returns a string whose length is one more than the
# number of separators contained in the string. The string "abbaabba"
# contains two instances of the separator "ba" so the list returned by
# split() has three elements. Since the third separator isn’t followed by
# any other characters, the third element of the list is set to the empty
# string.
# If the separator is not contained in the string at all, .split() returns a
# list with the string as its only element:
print("abbaabba".split("c"))
# In all, you’ve seen three ways to create a list:
# 1. A list literal
# 2. The list() built-in
# 3. The string .split() method
# Lists support the all of the same operations supported by tuples.

# Changing Elements in a List
# Think of a list as a sequence of numbered slots. Each slot holds a
# value, and every slot must be filled at all times, but you can swap out
# the value in a given slot with a new one whenever you want.
# The ability to swap values in a list for other values is called mutability.
# Lists are mutable. The elements of tuples may not be swapped
# for new values, so tuples are said to be immutable.
# To swap a value in a list with another, assign the new value to a slot
# using index notation:
colors = ["red", "yellow", "green", "blue"]
colors[0] = "burgundy"
# The value at index 0 changes from "red" to "burgundy":
print(colors)
# You can change several values in a list at once with a slice assignment:
colors[1:3] = ["orange", "magenta"]
print(colors)
# colors[1:3] selects the slots with indices 1 and 2. The values in these
# slots are assigned to "orange" and "magenta", respectively.
# The list assigned to a slice does not need to have the same length as
# the slice. For instance, you can assign a list of three elements to a slice
# with two elements:
colors = ["red", "yellow", "green", "blue"]
colors[1:3] = ["orange", "magenta", "aqua"]
print(colors)
# The values "orange" and "magenta" replace the original values "yellow"
# and "green" in colors at the indices 1 and 2. Then a new slot is created at
# index 4 and "blue" is assigned to this index. Finally, "aqua" is assigned
# to index 3.
# When the length of the list being assigned to the slice is less than the
# length of the slice, the overall length of the original list is reduced:
colors[1:4] = ["yellow", "green"]
print(colors)
# The values "yellow" and "green" replace the values "orange" and
# "magenta" in colors at the indices 1 and 2. Then the value at index 3 is
# replaced with the value "blue". Finally, the slot at index 4 is removed
# from colors entirely.
# The above examples show how to change, or mutate, lists using index
# and slice notation. There are also several list methods that you can use
# to mutate a list.

# List Methods For Adding and Removing Elements
# Although you can add and remove elements with slice notation, list
# methods provide a more natural and readable way to mutate a list.
# We’ll look at several list methods, starting with how to insert a single
# value into a list at a specified index.
# list.insert()
# The list.insert() method is used to insert a single new value into a
# list. It takes two parameters, an index i and a value x, and inserts the
# value x at index i in the list.
colors.insert(1, 'orange')
print(colors)
# There are a couple of important observations to make about this example.
# The first observation applies to all list methods. To use them, you first
# write the name of the list you want to manipulate, followed by a dot
# (.) and then the name of the list method.
# So, to use insert() on the colors list, you must write colors.insert().
# This works just like string and number methods do.
# Next, notice that when the value "orange" is inserted at the index 1, the
# value "yellow" and all following values are shifted to the right.
# If the value for the index parameter of .insert() is larger than the
# greatest index in the list, the value is inserted at the end of the list:
colors.insert(10, 'violet')
print(colors)
# Here the value "violet" is actually inserted at index 5, even though
# .insert() was called with 10 for the index.
# You can also use negative indices with .insert():
colors.insert(-1, 'indigo')
print(colors)
# This inserts "indigo" into the slot at index -1 which is the last element
# of the list. The value "violet" is shifted to the right by one slot.
# When you .insert() an item into a list, you do not need to assign
# the result to the original list.
# For example, the following code actually erases the colors list:
# >>> colors = colors.insert(-1, "indigo")
# >>> print(colors)
# None
# .insert() is said to alter colors in place. This is true for all list
# methods that do not return a value.
# If you can insert a value at a specified index, it only makes sense that
# you can also remove an element at a specified index.
# list.pop()
# The list.pop() method takes one parameter, an index i, and removes
# the value from the list at that index. The value that is removed is returned
# by the method:
color = colors.pop(3)
print(color)
print(colors)
# Here, the value "green" at index 3 is removed and and assigned to the
# variable color. When you inspect the colors list, you can see that the
# string "green" has indeed been removed.
# Unlike .insert(), Python raises an IndexError if you pass to .pop() an
# argument larger than the last index:
try:
    colors.pop(10)
except IndexError as err:
    print(err)
# >>> colors.pop(10)
# Traceback (most recent call last):
# File "<pyshell#0>", line 1, in <module>
# colors.pop(10)
# IndexError: pop index out of range
# Negative indices also work with .pop()
print(colors.pop(-1))
# If you do not pass a value to .pop(), it removes the last item in the list:
print(colors.pop())
print(colors)
# This way of removing the final element, by calling .pop() with no
# specified index, is generally considered the most Pythonic.
# list.append()
# The list.append() method is used to append an new element to the end
# of a list:
colors.append('indigo')
print(colors)
# After calling .append(), the length of the list increases by one and the
# value "indigo" is inserted into the final slot. Note that .append() alters
# the list in place, just like .insert().
# .append() is equivalent to inserting an element at an index greater than
# or equal to the length of the list. The above example could also have
# been written as follows:
# >>> colors.insert(len(colors), "indigo")
# .append() is both shorter and more descriptive than using .insert()
# this way, and is generally considered the more Pythonic way of added
# an element to the end of a list.
# list.extend()
# The list.extend() method is used to add several new elements to the
# end of a list:
colors.extend(['violet', 'ultraviolet'])
print(colors)
# .extend() takes a single parameter that must be an iterable type. The
# elements of the iterable are appended to the list in the same order that
# they appear in the argument passed to .extend().
# Just like .insert() and .append(), .extend() alters the list in place.
# Typically, the argument passed to .extend() is another list, but it could
# also be a tuple or any other iterable.
# In addition to list methods, Python has a couple of useful built-in
# functions for working with lists of numbers.

# Lists of Numbers
# One very common operation with lists of numbers is to add up all the
# values to get the total.
# You can do this with a for loop:
nums = [1, 2, 3, 4, 5, 6]
total = 0
for num in nums:
    total += num
print(total)
# First you initialize the variable total to 0, and then loop over each number
# is nums and add it to total, finally arriving at the value 15.
# Although this for loop is straightforward, there is a much more succinct
# way of doing this in Python:
print(sum(nums))
# The built-in sum() function takes a list as an argument and returns the
# total of all the values in the list.
# If the list passed to sum() contains any values that aren’t numeric, a
# TypeError is raised:
# >>> sum([1, 2, 3, "four", 5])
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Besides sum(), there are two other useful built-in functions for working
# with lists of numbers: min() and max(). These functions return the
# minimum and maximum values in the list, respectively:
print(min(nums))
print(max(nums))
# Note that sum(), min(), and max() also work with tuples:
nums = tuple(nums)
print(nums)
print(sum(nums))
print(min(nums))
print(max(nums))
# The fact that sum(), min(), and max() are all built-in to Python tells you
# that they are used frequently. Chances are, you’ll find yourself using
# them quite a bit in your own programs!

# List Comprehensions
# Yet another way to create a list from an existing iterable is with a list
# comprehension:
numbers = (1, 2, 3, 4, 5)
squares = [num ** 2 for num in numbers]
print(squares)
# A list comprehension is a short-hand for a for loop. In the example
# above, a tuple literal containing five numbers is created and assigned
# to the numbers variable. On the second line, a list comprehension loops
# over each number in numbers, squares each number, and adds it to a
# new list called squares.
# To create the sqaures list using a traditional for loop involves first
# creating an empty list, looping over the numbers in numbers, and appending
# the square of each number to the list:
trad_list = []
for num in numbers:
    trad_list.append(num ** 2)
print(trad_list)
# List comprehensions are commonly used to convert values in one list
# to a different type.
# For instance, suppose you needed to convert a list of strings containing
# floating point values to a list of float objects. The following list
# comprehensions achieves this:
str_numbers = ["1.5", "2.3", "5.25"]
float_numbers = [float(val) for val in str_numbers]
print(str_numbers)
print(float_numbers)
# List comprehensions are not unique to Python, but they are one of
# its many beloved features. If you find yourself creating an empty list,
# looping over some other iterable, and appending new items to the list,
# then chances are you can replace your code with a list comprehension!

# Review Exercises
# 1. Create a list named food with two elements "rice" and "beans".
food = ['rice', 'beans']
# 2. Append the string "broccoli" to food using .append().
food.append('broccoli')
# 3. Add the string "bread" and "pizza" to "food" using .extend().
food.extend(['bread', 'pizza'])
# 4. Print the first two items in the food list using print() and slicing
# notation.
print(*food[:2])
# 5. Print the last item in food using print() and index notation.
print(food[-1])
# 6. Create a list called breakfast from the string "eggs, fruit, orange
# juice" using the string .split() method.
breakfast = "eggs, fruit, orange juice".split(', ')
# 7. Verify that breakfast has three items using len().
print(len(breakfast))
# 8. Create a new list called lengths using a list comprehension that
# contains the lengths of each string in the breakfast list.
lengths = [len(string) for string in breakfast]
print(lengths)

# Nesting, Copying, and Sorting
# Tuples and Lists
# Now that you have learned what tuples and lists are, how to create
# them, and some basic operations with them, let’s look at three more
# concepts:
# 1. Nesting
# 2. Copying
# 3. Sorting

# Nesting Lists and Tuples
# Lists and tuples can contain values of any type. That means lists and
# tuples can contain lists and tuples as values. A nested list, or nested
# tuple, is a list or tuple that is contained as a value in another list or
# tuple.
# For example, the following list has two values, both of which are other
# lists:
two_by_two = [[1, 2], [3, 4]]
print(len(two_by_two))
print(two_by_two)
print(two_by_two[0])
print(two_by_two[1])
# Since two_by_two[1] returns the list [3, 4], you can use double index
# notation to access an element in the nested list:
print(two_by_two[1][0])
# First, Python evaluates two_by_two[1] and returns [3, 4]. Then Python
# evaluates [3, 4][0] and returns the first element 3.
# In very loose terms, you can think of a list of lists or a tuple of tuples
# as a sort of table with rows and columns.
# The two_by_two list has two rows, [1, 2] and [3, 4]. The columns
# are made of of the corresponding elements of each row, so the first
# columns contains the elements 1 and 3, and the second column contains
# the elements 2 and 4.
# This table analogy is only an informal way of thinking about a list of
# lists, though. For example, there is no requirement that all the lists
# in a list of lists have the same length, in which case this table analogy
# starts to break down.
# Readers interested in data analysis or scientific computing may
# recognize lists of lists as a sort of matrix of values.
# While you can use the built in list and tuple types for matrices,
# better alternatives exist. To learn how to work with matrices in
# Python, check out Chapter 17.

# Copying a List
# Sometimes you need to copy one list into another list. However, you
# can’t just reassign one list object to another list object, because you’ll
# get this (possibly surprising) result:
animals = ["lion", "tiger", "frumious Bandersnatch"]
large_cats = animals
large_cats.append('Tigger')
print(animals)
# In this example, you first assign the list stored in the animals variable
# to the variable large_cats, and then we add a new string to the large_-
# cats list. But, when the contents of animals are displayed you can see
# that the original list has also been changed.
# This is a quirk of object-oriented programming, but it’s by design.
# When you say large_cats = animals, the large_cats and animals variables
# both refer to the same object.
# A variable name is really just a reference to a specific location in
# computer memory. Instead of copying all the contents of the list object
# and creating a new list, large_cats = animals assigns the memory location
# referenced by animals to large_cats. That is, both variables now
# refer to the same object in memory, and any changes made to one will
# affect the other.
# To get an independent copy of the animals list, you can use slicing notation
# to return a new list with the same values:
animals = ["lion", "tiger", "frumious Bandersnatch"]
large_cats = animals[:]
large_cats.append('Tigger')
print(animals)
print(large_cats)
# Since no index numbers are specified in the [:] slice, every element
# of the list is returned from beginning to end. The large_cats list now
# has the same elements as animals, and in the same order, but you can
# .append() items to it without changing the list assigned to animals.
# If you want to make a copy of a list of lists, you can do so using the [:]
# notation you saw earlier:
matrix1 = [[1, 2], [3, 4]]
matrix2 = matrix1[:]
matrix2[0] = [5, 6]
matrix1 = [[1, 2], [3, 4]]
print(matrix1)
print(matrix2)
# Let’s see what happens when you change the first element of the
# second list in matrix2:
matrix2[1][0] = 1
print(matrix2)
print(matrix1)
# Notice that the second list in matrix1 was also altered!
# This happens because a list does not really contain objects themselves,
# but references to those objects in memory. When you make a copy
# of the list using the [:] notation, a new list is returned containing
# the same references as the original list. In programming jargon, this
# method of copying a list is called a shallow copy.
# To make a copy of both the list and all of the elements it contains, you
# must use what is known as a deep copy. This method of copying is
# beyond the scope of this course. For more information on shallow and
# deep copies, check out the Shallow vs Deep Copying of Python Objects
# article on realpython.com.
# https://realpython.com/copying-python-objects/

# Sorting Lists
# Lists have a .sort() method that sorts all of the items in ascending
# order. By default, the list is sorted in alphabetical or numerical order,
# depending on the type of elements in the list:
# Lists of strings are sorted alphabetically
colors = ["red", "yellow", "green", "blue"]
colors.sort()
print(colors)
# Lists of numbers are sorted numerically
numbers = [1, 10, 5, 3]
numbers.sort()
print(numbers)
# Notice that .sort() sorts the list in place, so you don’t need to assign
# it’s result to anything.
# .sort() has an option parameter called key that can be used to adjust
# how the list gets sorted. The key parameter accepts a function, and the
# list is sorted based on the return value of that function.
# For example, to sort a list of strings by the length of each string, you
# can pass the len function to key:
colors.sort(key=len)
print(colors)
# You don’t need to call the function when you pass it to key. Pass the
# name of the function without any parentheses. For instance, in the
# previous example the name len is passed to key, and not len().
# The function that gets passed to key must only accept a single argument.
# You can also pass user defined functions to key. In the following example,
# a function called get_second_element() is used to sort a list of tuples
# by their second elements:


def get_second_element(item):
    return item[1]


items = [(4, 1), (1, 2), (-9, 0)]
items.sort(key=get_second_element)
print(items)

# with lambda function
items.sort(key=lambda item: item[0])
print(items)
# Keep in mind that any function that you pass to key must accept only
# a single argument.

# Review Exercises
# 1. Create a tuple data with two values. The first value should be the
# tuple (1, 2) and the second value should be the tuple (3, 4).
data = ((1, 2), (3, 4))
# 2. Write a for loop that loops over data and prints the sum of each
# nested tuple. The output should look like this:
# Row 1 sum: 3
# Row 2 sum: 7
for row in data:
    print(f'Row {data.index(row) + 1} sum: {sum(row)}')
# 3. Create the following list [4, 3, 2, 1] and assign it to the variable
# numbers.
numbers = [4, 3, 2, 1]
# 4. Create a copy of the numbers list using the [:] slicing notation.
numbers_copy = numbers[:]
# 5. Sort the numbers list in numerical order using the .sort() method.
numbers.sort()
print(numbers)

# Challenge: List of lists
# Write a program that contains the following lists of lists:
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

# Define a function, enrollment_stats(), that takes, as an input, a list of
# lists where each individual list contains three elements: (a) the name
# of a university, (b) the total number of enrolled students, and (c) the
# annual tuition fees.
# enrollment_stats() should return two lists: the first containing all of
# the student enrollment values and the second containing all of the
# tuition fees.


def enrollment_stats(universities_list):
    stats_list = [
        [university[1] for university in universities_list],
        [university[2] for university in universities_list]
    ]
    return stats_list


print(enrollment_stats(universities))
# Next, define a mean() and a median() function. Both functions should
# take a single list as an argument and return the mean and median of
# the values in each list.


def mean(items):
    return sum(items) / len(items)


def median(items):
    if len(items) == 1:
        return items[0]
    list_num = items[:]
    list_num.sort()
    items_is_odd = (len(items) % 2) > 0

    if items_is_odd:
        md_idx = int((len(list_num) / 2) - 0.5)
        return list_num[md_idx]

    md_idx = [int((len(list_num) / 2) - 1), int(len(list_num) / 2)]
    md_even = sum([list_num[md_idx[0]], list_num[md_idx[1]]]) / 2
    return md_even


# Using universities, enrollment_stats(), mean(), and median(), calculate
# the total number of students, the total tuition, the mean and median
# of the number of students, and the mean and median tuition values.
# Finally, output all values, and format the output so that it looks like
# this:
# ******************************
# Total students: 77,285
# Total tuition: $ 271,905
# Student mean: 11,040.71
# Student median: 10,566
# Tuition mean: $ 38,843.57
# Tuition median: $ 39,849
# ******************************
universities_data = enrollment_stats(universities)
students = universities_data[0]
tuitons = universities_data[1]
print('*' * 30)
print(f'Total students: {sum(students):,.0f}')
print(f'Total tuition: $ {sum(tuitons):,.0f}')
print(f'Student mean: {mean(students):,.2f}')
print(f'Student median: {median(students):,.0f}')
print(f'Tuition mean: $ {mean(tuitons):,.2f}')
print(f'Tuition median: $ {median(tuitons):,.0f}')
print('*' * 30)

# Challenge: Wax Poetic
# In this challenge, you’ll write a program that generates poetry.
# Create five lists for different word types:
# • Nouns: ["fossil", "horse", "aardvark", "judge", "chef", "mango",
# "extrovert", "gorilla"]
# • Verbs: ["kicks", "jingles", "bounces", "slurps", "meows",
# "explodes", "curdles"]
# • Adjectives: ["furry", "balding", "incredulous", "fragrant",
# "exuberant", "glistening"]
# • Prepositions: ["against", "after", "into", "beneath", "upon",
# "for", "in", "like", "over", "within"]
# • Adverbs: ["curiously", "extravagantly", "tantalizingly",
# "furiously", "sensuously"]
# Randomly select the following number of elements from each list:
# • 3 nouns
# • 3 verbs
# • 3 adjectives
# • 2 prepositions
# • 1 adverb
# You can do this with the choice() function in the random module. This
# function takes a list as input and returns a randomly selected element
# of the list.
# For example, here’s how you use random.choice() to get random element
# from the list ["a", "b", "c"]:
# import random
# random_element = random.choice(["a", "b", "c"])
# Using the randomly selected words, generate and display a poem with
# the following structure inspired by Clifford Pickover:

# {A/An} {adj1} {noun1}
#
# {A/An} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
# {adverb1}, the {noun1} {verb2}
# the {noun2} {verb3} {prep2} a {adj3} {noun3}

# Here, adj stands for adjective and prep for preposition.
# Here’s an example of the kind of poem your program might generate:
# A furry horse
# A furry horse curdles within the fragrant mango
# extravagantly, the horse slurps
# the mango meows beneath a balding extrovert
# Every time your program runs, it should generate a new poem.
nouns = [
    "fossil", "horse", "aardvark", "judge",
    "chef", "mango", "extrovert", "gorilla"
]
verbs = [
    "kicks", "jingles", "bounces", "slurps", "meows",
    "explodes", "curdles"
]
adjectives = [
    "furry", "balding", "incredulous", "fragrant",
    "exuberant", "glistening"
]
prepositions = [
    "against", "after", "into", "beneath", "upon",
    "for", "in", "like", "over", "within"
]
adverbs = [
    "curiously", "extravagantly", "tantalizingly",
    "furiously", "sensuously"
]

# • 3 nouns
noun_lst = random.choices(nouns, k=3)
# • 3 verbs
verb_lst = random.choices(verbs, k=3)
# • 3 adjectives
adj_lst = random.choices(adjectives, k=3)
# • 2 prepositions
prep_lst = random.choices(prepositions, k=2)
# • 1 adverb
adverb = random.choice(adverbs)

begin_phrase = 'An' if adj_lst[0][0] in vowels else 'A'

print(
    f'{begin_phrase} {adj_lst[0]} {noun_lst[0]}',
    '',
    f'{begin_phrase} {adj_lst[0]} {noun_lst[0]} {verb_lst[0]} '
    f'{prep_lst[0]} the {adj_lst[1]} {noun_lst[1]}',
    f'{adverb}, the {noun_lst[0]} {verb_lst[1]}',
    f'the {noun_lst[1]} {verb_lst[2]} {prep_lst[1]} a {adj_lst[2]}'
    f' {noun_lst[2]}',
    sep='\n'
)

# Store Relationships in Dictionaries
# One of the most useful data structures in Python is the dictionary.
# In this section, you’ll learn what a dictionary is, how dictionaries differ
# from lists and tuples, and how to define and use dictionaries in your
# own code.
# What is a Dictionary?
# In plain English, a dictionary is a book containing the definitions of
# words. Each entry in a dictionary has two parts: the word being defined,
# and its definition.
# Python dictionaries, like lists and tuples, store a collection of objects.
# However, instead of storing objects in a sequence, dictionaries hold
# information in pairs of data called key-value pairs. That is, each
# object in a dictionary has two parts: a key and a value.
# The key in a key-value pair is a unique name that identifies the value
# part of the pair. Comparing this to an English dictionary, the key is
# like the word being defined and the value is like the definition of the
# word.
# The difference between an English dictionary and a Python dictionary
# is that the relationship between a key and its value is completely arbitrary.
# Any key can be assigned to any value.
# In this sense, a Python dictionary is much more like a map than it
# is an English dictionary. The term map here comes from mathematics.
# It is used to describe a relation between two sets of values, not a
# geographical map.
# In practice, it is this idea of dictionaries as a map that is particularly
# useful. Under this lens, the English dictionary is a special case of a
# map that relates words to their definitions.
# So in summary, a Python dictionary is a data structure that relates a
# set of keys to a set of values. Each key is assigned a single value, which
# defines a relationship between the two sets.
# Creating Dictionaries
# The following code creates a dictionary literal containing names of
# states and their capitals:
capitals = {
    "California": "Sacramento",
    "New York": "Albany",
    "Texas": "Austin",
}
# Notice that each key is separated from its value by a colon (:), each
# key-value pair is separated by a comma (,), and the entire dictionary
# is enclosed in curly braces ({ and }).
# You can also create a dictionary from a sequence of tuples using the
# dict() built-in:
key_value_pairs = (
    ("California", "Sacramento"),
    ("New York", "Albany"),
    ("Texas", "Austin"),
)
capitals = dict(key_value_pairs)
# When you inspect a dictionary, it is displayed as a dictionary literal,
# regardless of how it was created:
print(capitals)
print(type({}))
# You can create an empty dictionary using either a literal or dict():
print(type(dict()))
# To access a value in a dictionary, enclose the corresponding key in
# square brackets ([ and ]) at the end of dictionary or a variable name
# assigned to a dictionary:
print(capitals["Texas"])
# The bracket notation used to access a dictionary value looks similar
# to the index notation used to get values from strings, lists, and tuples.
# However, dictionaries are a fundamentally different data structure than
# sequence types like lists and tuples.
# To see the difference, let’s step back for a second and notice that we
# could just as well define the capitals dictionary as a list:
capitals_list = ["Sacramento", "Albany", "Austin"]
# You can use index notation to get the capital of each of the three states
# from the capitals dictionary:
# >>> capitals_list[0] # Capital of California
# 'Sacramento'
# >>> capitals_list[2] # Capital of Texas
# 'Austin'
# One nice thing about dictionaries is that they can be used to provide
# context to the values they contain. Typing capitals["Texas"] is easier
# to understand than capitals_list[2], and you don’t have to remember
# the order of data in a long list or tuple.
# This idea of ordering is really the main difference between how items
# in a sequence type are accessed compared to a dictionary.
# Values in a sequence type are accessed by index, which is an integer
# value expressing the order of items in the sequence.
# On the other hand, items in a dictionary are accessed by a key, which
# doesn’t define any kind of order, but just provides a label that can be
# used to reference the value.

# Adding and Removing Values in a Dictionary
# Like lists, dictionaries are mutable data structures. This means you
# can add and remove items from a dictionary.
# Let’s add the capital of Colorado to the capitals dictionary:
capitals["Colorado"] = "Denver"
print(capitals)
# First you use the square bracket notation with "Colorado" as the key,
# as if you were looking up the value. Then you use the assignment operator
# = to assign the value "Denver" to the new key.
# Each key in a dictionary can only be assigned a single value. If a key
# is given a new value, Python just overwrites the old one:
capitals["Texas"] = "Houston"
print(capitals)
# To remove an item from a dictionary, use the del keyword with the key
# for the value you want to delete:
del capitals["Texas"]
print(capitals)
# or You can use .pop() to remove the last key: value in the dictionary
# If you try to access a value in a dictionary using a key that doesn’t exist,
# Python raises a KeyError:
# >>> capitals["Arizona"]
# Traceback (most recent call last):
# File "<pyshell#1>", line 1, in <module>
# capitals["Arizona"]
# KeyError: 'Arizona'
# The KeyError is the most common error encountered when working
# with dictionaries. Whenever you see it, it means that an attempt was
# made to access a value using a key that doesn’t exist.
# You can check that a key exists in a dictionary using the in keyword:
print("Arizona" in capitals)
print("California" in capitals)
# or you can use the .get() method with the key as argument
# get returns None if no key exists with the specified name
print(capitals.get('key', 'return this if not in dict'))
# Iterating Over Dictionaries
# Like lists and tuples, dictionaries are iterable. However, looping over
# a dictionary is a bit different than looping over a list or tuple.
# When you loop over a dictionary with a for loop, you iterate over the
# dictionary’s keys:
for key in capitals:
    print(key)
# So, if you want to loop over the capitals dictionary and print “The
# capital of X is Y”, where X is the name of the state and Y is the state’s
# capital, you can do the following:
for state in capitals:
    print(f'The capital of {state} is {capitals[state]}')
# However, there is a slightly more succinct way to do this using the
# .items() dictionary method. .items() returns a list-like object containing
# tuples of key-value pairs. For example, capitals.items() returns a
# list of tuples of states and their corresponding capitals:
print(capitals.items())
# The object returned by .items() isn’t really a list. It has a special type
# called a dict_items:
print(type(capitals.items()))
# You don’t need to worry about what dict_items really is, because you
# usually won’t work with it directly. The important thing to know about
# it is that you can use .items() to loop over a dictionary’s keys and
# values simultaneously.
# Let’s rewrite the previous loop using .items()
for state, capital in capitals.items():
    print(f'The capital of {state} is {capital}')
# When you loop over capitals.items(), each iteration of the loop
# produces a tuple containing the state name and the corresponding capital
# city name. By assigning this tuple to state, capital, the components
# of the tuple are unpacked into the two variable state and capital.

# Dictionary Keys and Immutability
# In the capitals dictionary you’ve been working with throughout this
# section, each key is a string. However, there is no rule that says
# dictionary keys must all be of the same type.
# For instance, you can add an integer key to capitals:
capitals[50] = "Honolulu"
print(capitals)
# There is only one restriction on what constitutes a valid dictionary key.
# Only immutable types are allowed. This means, for example, that a
# list cannot be a dictionary key.
# Consider this: what should happen if a list were used as a key in a
# dictionary and, somewhere later in the code, the list is changed?
# Should the list be associated to the same value as the old list in the
# dictionary? Or should the value for the old key be removed from the
# dictionary all together?
# Rather than make a guess about what should be done, Python raises
# an exception:
# >>> capitals[[1, 2, 3]] = "Bad"
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'
# It might not seem fair that some types can be keys and others can’t, but
# it’s important that a programming language always has well-defined
# behavior. It should never make guesses about what the author intended.
# Unlike keys, dictionary values can be any valid Python type, including
# other dictionaries!

# Nested Dictionaries
# Just as you can nest lists inside of other lists, and tuples inside of other
# tuples, you can create nested dictionaries.
# Let’s alter the capitals dictionary to illustrate this idea. Instead of
# mapping state names to their capital cities, we’ll create a dictionary
# that maps each state name to a dictionary containing the capital city
# and the state flower
states = {
    "California": {
        "capital": "Sacramento",
        "flower": "California Poppy"
    },
    "New York": {
        "capital": "Albany",
        "flower": "Rose"
    },
    "Texas": {
        "capital": "Austin",
        "flower": "Bluebonnet"
    },
}
# The value of each key is a dictionary:
print(states["Texas"])
# To get the Texas state flower, first get the value at the key "Texas", and
# then the value at the key "flower":
print(states["Texas"]["flower"])
# Nested dictionaries come up more often than you might expect. They
# are particularly useful when working with data transmitted over the
# web. Nested dictionaries are also great for modeling structured data,
# such as spreadsheets or relational databases.

# Review Exercises
# 1. Create an empty dictionary named captains.
captains = {}
# 2. Using the square bracket notation, enter the following data into
# the dictionary, one item at a time:
# 'Enterprise': 'Picard'
# 'Voyager': 'Janeway'
# 'Defiant': 'Sisko'
captains['Enterprise'] = 'Picard'
captains['Voyager'] = 'Janeway'
captains['Defiant'] = 'Sisko'
print(captains)
# 3. Write two if statements that check if "Enterprise" and "Discovery"
# exist as keys in the dictionary. Set their values to "unknown" if the
# key does not exist.
if "Enterprise" not in captains:
    captains["Enterprise"] = "unknown"
if "Discovery" not in captains:
    captains["Discovery"] = "unknown"
# 4. Write a for loop to display the ship and captain names contained
# in the dictionary. For example, the output should look something
# like this:
# The Enterprise is captained by Picard.
# print(dict(sorted(states.items(), key=lambda x: x[1]['capital'])))
for ship, captain in sorted(captains.items(), key=lambda x: x[0]):
    print(f"The {ship} is captained by {captain}")
# 5. Delete "Discovery" from the dictionary.
del captains["Discovery"]
# 6. Bonus: Make the same dictionary by using dict() and passing in
# the initial values when you first create the dictionary
# Enterprise='Picard'
# Voyager='Janeway'
# Defiant='Sisko'
new_captains = dict(
    Enterprise='Picard',
    Voyager='Janeway',
    Defiant='Sisko'
)
print(new_captains)
new_new_captains = dict([
    ('Enterprise', 'Picard'),
    ('Voyager', 'Janeway'),
    ('Defiant', 'Sisko'),
])
print(new_new_captains)

# Challenge: Capital City Loop
# Review your state capitals along with dictionaries and while loops!
# First, finish filling out the following dictionary with the remaining
# states and their associated capitals in a file called capitals.py.
# capitals_dict = {
# 'Alabama': 'Montgomery',
# 'Alaska': 'Juneau',
# 'Arizona': 'Phoenix',
# 'Arkansas': 'Little Rock',
# 'California': 'Sacramento',
# 'Colorado': 'Denver',
# 'Connecticut': 'Hartford',
# 'Delaware': 'Dover',
# 'Florida': 'Tallahassee',
# 'Georgia': 'Atlanta',
# }
# Next, pick a random state name from the dictionary, and assign both
# the state and it’s capital to two variables. You’ll need to import the
# random module at the top of your program.
# Then display the name of the state to the user and ask them to enter
# the capital. If the user answers, incorrectly, repeatedly ask them for
# the capital name until they either enter the correct answer or type the
# word “exit”.
# If the user answers correctly, display "Correct" and end the program.
# However, if the user exits without guessing correctly, display the correct
# answer and the word "Goodbye".
# Note
# Make sure the user is not punished for case sensitivity. In other
# words, a guess of "Denver" is the same as "denver". Do the same
# for exiting—"EXIT" and "Exit" should work the same as "exit".
# capitals_dict = {
#     'Alabama': 'Montgomery',
#     'Alaska': 'Juneau',
#     'Arizona': 'Phoenix',
#     'Arkansas': 'Little Rock',
#     'California': 'Sacramento',
#     'Colorado': 'Denver',
#     'Connecticut': 'Hartford',
#     'Delaware': 'Dover',
#     'Florida': 'Tallahassee',
#     'Georgia': 'Atlanta',
# }
# state, capital = random.choice(list(capitals_dict.items()))
# exit_game = False
# print('^' * 30)
# print('Welcome to the "Who wnats to be millionaire game"!!!!')
# print('^' * 30)

# while not exit_game:
#     print(f'What is the capital of {state}?')
#     usr_input = input(
#         'Enter your answer or "Exit" to finish the game: '
#     ).lower()

#     if capital.lower() == usr_input:
#         print('Correct')
#         print('You won $USD 1,000,000!')
#         exit_game = True
#     elif 'exit' == usr_input:
#         print(f'The answer was {capital}')
#         exit_game = True
#     else:
#         print('Try again')
# print('Goodbye')

# How to Pick a Data Structure
# In this chapter, you’ve learned about three data structures native to
# Python: lists, tuples, and dictionaries.
# You might be wondering, “How do I know when to use which data
# structure?” It’s a great question, and one many new Python programmers
# struggle with.
# The type of data structure you use depends on the problem you are
# solving, and there is no hard and fast rule you can use to pick the right
# data structure every time. You’ll always need to spend a little time
# thinking about the problem, and which structure works best for it.
# Fortunately, there are some guidelines you can use to help you make
# the right choice. These are presented below:
# Use a list when:
# • Data has a natural order to it
# • You will need to update or alter the data during the program
# • The primary purpose of the data structure is iteration
# Use a tuple when:
# • Data has a natural order to it
# • You will not need to update or alter the data during the program
# • The primary purpose of the data structure is iteration
# Use a dictionary when:
# • The data is unordered, or the order does not matter
# • You will need to update or alter the data during the program
# • The primary purpose of the data structure is looking up values

# Challenge: Cats With Hats
# You have 100 cats.
# One day you decide to arrange all your cats in a giant circle. Initially,
# none of your cats have any hats on. You walk around the circle 100
# times, always starting at the same spot, with the first cat (cat # 1).
# Every time you stop at a cat, you either put a hat on it if it doesn’t have
# one on, or you take its hat off if it has one on.
# 1. The first round, you stop at every cat, placing a hat on each one.
# 2. The second round, you only stop at every second cat (#2, #4, #6,
# #8, etc.).
# 3. The third round, you only stop at every third cat (#3, #6, #9, #12,
# etc.).
# 4. You continue this process until you’ve made 100 rounds around
# the cats (e.g., you only visit the 100th cat).
# Write a program that simply outputs which cats have hats at the end.
# This is not an easy problem by any means. Honestly, the code is
# simple. This problem is often seen on job interviews as it tests
# your ability to reason your way through a difficult problem. Stay
# calm. Start with a diagram, and then write pseudo code. Find
# a pattern. Then code!
cats_without_hats = list(range(1, 101))
cats_with_hats = []
for i in range(1, 101):
    if i == 1:
        cats_with_hats = [cat for cat in cats_without_hats]
        cats_without_hats = []
        continue

    cats_visited = [cat for cat in range(i, 101, i)]

    for cat in cats_visited:
        if cat in cats_with_hats:
            idx = cats_with_hats.index(cat)
            cat_removed = cats_with_hats.pop(idx)
            cats_without_hats.append(cat_removed)
        else:
            idx = cats_without_hats.index(cat)
            cat_removed = cats_without_hats.pop(idx)
            cats_with_hats.append(cat_removed)

print(f'Cats with hats: {cats_with_hats}')

theCats = {}
for i in range(1, 101):
    theCats[i] = False

for i in range(1, 101):
    for cats, hats in theCats.items():
        if cats % i == 0:
            if theCats[cats]:
                theCats[cats] = False
            else:
                theCats[cats] = True

for cats, hats in theCats.items():
    if theCats[cats]:
        print(f"Cat {cats} has a hat.")
