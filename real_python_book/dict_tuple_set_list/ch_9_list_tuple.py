# Lists and Tuples
# Lists and tuples are arguably Python’s most versatile, useful data types.
# You will find them in virtually every nontrivial Python program.
# Here’s what you’ll learn in this tutorial: You’ll cover the important
# characteristics of lists and tuples.
# You’ll learn how to define them and how to manipulate them.
# When you’re finished, you should have a good feel for when and how to
# use these object types in a Python program.

# Python Lists
# In short, a list is a collection of arbitrary objects,
# somewhat akin to an array in many other programming languages but more
# flexible. Lists are defined in Python by enclosing a
# comma-separated sequence of objects in square brackets ([]), as shown below:
import math

a = ['foo', 'bar', 'baz', 'qux']
print(a)
# The important characteristics of Python lists are as follows:
# Lists are ordered.
# Lists can contain any arbitrary objects.
# List elements can be accessed by index.
# Lists can be nested to arbitrary depth.
# Lists are mutable.
# Lists are dynamic.
# Each of these features is examined in more detail below.

# Lists Are Ordered
# A list is not merely a collection of objects.
# It is an ordered collection of objects.
# The order in which you specify the elements when you define a list is
# an innate characteristic of that list and is maintained for that
# list’s lifetime.
# (You will see a Python data type that is not ordered in the next
# tutorial on dictionaries.)
# Lists that have the same elements in a different order are not the same:
a = ['foo', 'bar', 'baz', 'qux']
b = ['baz', 'qux', 'bar', 'foo']
print(a == b)
print(a is b)
print([1, 2, 3, 4] == [4, 1, 3, 2])

# Lists Can Contain Arbitrary Objects
# A list can contain any assortment of objects.
# The elements of a list can all be the same type:
a = [2, 4, 6, 8]
# Or the elements can be of varying types:
a = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]
# Lists can even contain complex objects, like functions, classes, and modules,
# which you will learn about in upcoming tutorials:


def foo():
    pass


a = [int, len, foo, math]
print(a)

# A list can contain any number of objects, from zero to as many as your
# computer’s memory will allow.
# List objects needn’t be unique. A given object can appear in a list
# multiple times:
a = ['bark', 'meow', 'woof', 'bark', 'cheep', 'bark']

# List Elements Can Be Accessed by Index
# Individual elements in a list can be accessed using an index in square brackets. This is exactly analogous to accessing individual characters in a string. List indexing is zero-based as it is with strings.
# Consider the following list:
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
# Here is Python code to access some elements of a:
a[0]
a[1]
a[2]
a[3]
# Virtually everything about string indexing works similarly for lists.
# For example, a negative list index counts from the end of the list:
a[-1]
a[-2]
a[-5]
# Slicing also works. If a is a list, the expression a[m:n] returns the
# portion of a from index m to, but not including, index n:
a[1:3]
# The [:] syntax works for lists. However, there is an important difference
# between how this operation works with a list and how it works with a string.
# If s is a string, s[:] returns a reference to the same object:
s = 'foobar'
print(s[:])
print(s[:] is s)
# if a is a list, s[:] returns a new object that is a copy of a:
s = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(s[:])
print(s[:] is s)
# Several Python operators and built-in functions can also be used with
# lists in ways that are analogous to strings:
# The in and not in operators:
print('qux' in s)
print('thud' not in s)
# The concatenation (+) and replication (*) operators:
print(s + ['graut', 'garply'])
print(s * 2)
a = s + ['graut', 'garply']
s[0] = 'boo'
print(a, s, sep='\n')
print(len(s), min(s), max(s), sep='\n')
# It’s not an accident that strings and lists behave so similarly.
# They are both special cases of a more general object type called an
# iterable, which you will encounter in more detail in the upcoming
# tutorial on definite iteration.
# By the way, in each example above, the list is always assigned to a variable
# before an operation is performed on it. But you can operate on a list
# literal as well

# Lists Can Be Nested
# You have seen that an element in a list can be any sort of object.
# That includes another list.
# A list can contain sublists, which in turn can contain sublists themselves,
# and so on to arbitrary depth.
# Consider this (admittedly contrived) example:
x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
print(x)
# x[0], x[2], and x[4] are strings, each one character long:
print(x[0], x[2], x[4])
# But x[1] and x[3] are sublists:
print(x[1], x[3], sep='\n', end='\n\n')
# To access the items in a sublist, simply append an additional index:
print(x[1][0], x[1][1], x[1][2], x[1][3], sep='\n', end='\n\n')
# x[1][1] is yet another sublist, so adding one more index accesses
# its elements:
print(x[1][1][0])
# There is no limit, short of the extent of your computer’s memory,
# to the depth or complexity with which lists can be nested in this way.
# All the usual syntax regarding indices and slicing applies to
# sublists as well
print(x[1][1][-1])
print(x[1][1:3])
print(x[3][::-1])
# However, be aware that operators and functions apply to only the list at the level you specify and are not recursive.
# Consider what happens when you query the length of x using len()
print(len(x))
# x has only five elements—three strings and two sublists.
# The individual elements in the sublists don’t count toward x’s length.
# You’d encounter a similar situation when using the in operator:
print('ddd' in x)
print('ddd' in x[1])
print('ddd' in x[1][1])
# 'ddd' is not one of the elements in x or x[1].
# It is only directly an element in the sublist x[1][1].
# An individual element in a sublist does not count as an element
# of the parent list(s).

# Lists Are Mutable
# Most of the data types you have encountered so far have been atomic types.
# Integer or float objects, for example, are primitive units that can’t be
# further broken down. These types are immutable, meaning that they can’t be
# changed once they have been assigned. It doesn’t make much sense to think of
# changing the value of an integer. If you want a different integer, you just
# assign a different one.
# By contrast, the string type is a composite type.
# Strings are reducible to smaller parts—the component characters.
# It might make sense to think of changing the characters in a string.
# But you can’t. In Python, strings are also immutable.
# The list is the first mutable data type you have encountered.
# Once a list has been created, elements can be added, deleted, shifted,
# and moved around at will. Python provides a wide range of ways
# to modify lists.

# Modifying a Single List Value
# A single value in a list can be replaced by indexing and simple assignment:
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[2] = 10
a[-1] = 20
print(a)
# You may recall from the tutorial Strings and Character Data in Python that
# you can’t do this with a string.
# A list item can be deleted with the del command:
del a[3]
print(a)

# Modifying Multiple List Values
# What if you want to change several contiguous elements in a list at one time?
# Python allows this with slice assignment, which has the following syntax:
# a[m:n] = <iterable>
# Again, for the moment, think of an iterable as a list.
# This assignment replaces the specified slice of a with <iterable>:
print(a)
print(a[1:4])
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a)
print(a[1:6])
a[1:6] = ['Bark!']
print(a)

# The number of elements inserted need not be equal to the number replaced.
# Python just grows or shrinks the list as needed.
# You can insert multiple elements in place of a single element—just use a
# slice that denotes only one element:
a = [1, 2, 3]
a[1:2] = [2.1, 2.2, 2.3]
print(a)
# Note that this is not the same as replacing the single element with a list:
a = [1, 2, 3]
a[1] = [2.1, 2.2, 2.3]
print(a)
# You can also insert elements into a list without removing anything.
# Simply specify a slice of the form [n:n] (a zero-length slice)
# at the desired index:
a = [1, 2, 3]
a[0:0] = [-3, -2, -1, 0]
print(a)
# You can delete multiple elements out of the middle of a list by assigning the
# appropriate slice to an empty list. You can also use the del statement with
# the same slice:
print(a[2:5])
a[2:5] = []
print(a)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
del a[1:5]
print(a)

# Prepending or Appending Items to a List
# Additional items can be added to the start or end of a list using the +
# concatenation operator or the += augmented assignment operator:
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a)
a += ['grault', 'garply']
print(a)
a = [10, 20] + a
print(a)
# Note that a list must be concatenated with another list, so if you want to
# add only one element, you need to specify it as a singleton list:
a += [20]
print(a)
# Note: Technically, it isn’t quite correct to say a list must be concatenated
# with another list. More precisely, a list must be concatenated with an
# object that is iterable. Of course, lists are iterable, so it works to
# concatenate a list with another list.
# Strings are iterable also. But watch what happens when you concatenate a
# string onto a list:
a = ['foo', 'bar', 'baz', 'qux', 'quux']
a += 'corge'
print(a)

# Methods That Modify a List
# Finally, Python supplies several built-in methods that can be used to modify
# lists. Information on these methods is detailed below.
# Because lists are mutable, the list methods shown here modify the
# target list in place.

# a.append(<obj>)
# Appends an object to a list.
# a.append(<obj>) appends object <obj> to the end of list a:
a = ['a', 'b']
a.append(123)
print(a)

# Remember that when the + operator is used to concatenate to a list,
# if the target operand is an iterable, then its elements are broken out
# and appended to the list individually
a = ['a', 'b']
print(a + [1, 2, 3])
# The .append() method does not work that way! If an iterable is appended to a
# list with .append(), it is added as a single object:
a = ['a', 'b']
a.append([1, 2, 3])
print(a)
# Thus, with .append(), you can append a string as a single entity:
a = ['a', 'b']
a.append('foo')
print(a)

# a.extend(<iterable>)
# Extends a list with the objects from an iterable.
# Yes, this is probably what you think it is. .extend() also adds to the end
# of a list, but the argument is expected
# to be an iterable. The items in <iterable> are added individually:
a = ['a', 'b']
a.extend([1, 2, 3])
print(a)

# In other words, .extend() behaves like the + operator. More precisely, since
# it modifies the list in place, it behaves like the += operator:
a = ['a', 'b']
a += [1, 2, 3]
print(a)

# a.insert(<index>, <obj>)
# Inserts an object into a list.
# a.insert(<index>, <obj>) inserts object <obj> into list a at the
# specified <index>. Following the method call, a[<index>] is <obj>,
# and the remaining list elements are pushed to the right:
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a.insert(3, 3.14159)
print(a[3])
print(a)

# a.remove(<obj>)
# Removes an object from a list.
# a.remove(<obj>) removes object <obj> from list a. If <obj> isn’t in a,
# an exception is raised:
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a.remove('baz')
print(a)
try:
    a.remove('Bark!')
except ValueError as e:
    print(e)

# a.pop(index=-1)
# Removes an element from a list.
# This method differs from .remove() in two ways:
# You specify the index of the item to remove, rather than the object itself.
# The method returns a value: the item that was removed.
# a.pop() simply removes the last item in the list:
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a.pop())
print(a)
print(a.pop())
print(a)
# If the optional <index> parameter is specified, the item at that index is
# removed and returned. <index> may be negative, as with string and list
# indexing:
print(a.pop(1))
print(a)

# Lists Are Dynamic
# This tutorial began with a list of six defining characteristics of Python
# lists. The last one is that lists are dynamic. You have seen many examples
# of this in the sections above. When items are added to a list, it grows
# as needed. Similarly, a list shrinks to accommodate the removal of items.

# Python Tuples
# Python provides another type that is an ordered collection of objects,
# called a tuple.
# Defining and Using Tuples
# Tuples are identical to lists in all respects, except for the following
# properties:
# Tuples are defined by enclosing the elements in parentheses (()) instead
# of square brackets ([]).
# Tuples are immutable.
# Here is a short example showing a tuple definition, indexing, and slicing:
t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t[1::2])
print(t[::-1])
# Why use a tuple instead of a list?
# Program execution is faster when manipulating a tuple than it is for the
# equivalent list. (This is probably not going to be noticeable when the list
# or tuple is small.)
# Sometimes you don’t want data to be modified. If the values in the collection
# are meant to remain constant for the life of the program, using a tuple
# instead of a list guards against accidental modification.
# There is another Python data type that you will encounter shortly called a
# dictionary, which requires as one of its components a value that is of an
# immutable type. A tuple can be used for this purpose,
# whereas a list can’t be.
# In a Python REPL session, you can display the values of several objects
# simultaneously by entering them directly at the >>> prompt,
# separated by commas:
# >>> a = 'foo'
# >>> b = 42
# >>> a, 3.14159, b
# ('foo', 3.14159, 42)
a = 1, 2, 3
print(a)
# Python displays the response in parentheses because it is implicitly
# interpreting the input as a tuple.
# There is one peculiarity regarding tuple definition that you should be
# aware of. There is no ambiguity when defining an empty tuple,
# nor one with two or more elements. Python knows you are defining a tuple:
t = ()
print(type(t))
t = (1, 2)
print(type(t))
t = (1, 2, 3, 4)
print(type(t))
# But what happens when you try to define a tuple with one item:
t = (1)
print(type(t))
# Doh! Since parentheses are also used to define operator precedence in
# expressions, Python evaluates the expression (2) as simply the integer 2
# and creates an int object. To tell Python that you really want to define a
# singleton tuple, include a trailing comma (,) just before the
# closing parenthesis:
t = (1,)
print(type(t), t)
# When you display a singleton tuple, Python includes the comma, to remind you
# that it’s a tuple

# Tuple Assignment, Packing, and Unpacking
# As you have already seen above, a literal tuple containing several items can
# be assigned to a single object:
t = ('foo', 'bar', 'baz', 'qux')
# When this occurs, it is as though the items in the tuple have been “packed”
# into the object
# If that “packed” object is subsequently assigned to a new tuple, the
# individual items are “unpacked” into the objects in the tuple
s1, s2, s3, s4 = t
print(s1, s4)
# When unpacking, the number of variables on the left must match the number of
# values in the tuple
# Tuple assignment allows for a curious bit of idiomatic Python.
# Frequently when programming, you have two variables whose values you
# need to swap. In most programming languages, it is necessary to store
# one of the values in a temporary variable while the swap occurs like this:
a = 'foo'
b = 'bar'
print((a, b))
# We need to define a temp variable to accomplish the swap.
temp = a
a = b
b = temp
print((a, b))

# In Python, the swap can be done with a single tuple assignment:
a = 'foo'
b = 'bar'
print((a, b))
a, b = b, a
print((a, b))

# As anyone who has ever had to swap values using a temporary variable knows,
# being able to do it this way in Python is the pinnacle of modern
# technological achievement. It will never get better than this.
