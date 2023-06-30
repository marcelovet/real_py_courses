# Python provides another composite data type called a dictionary,
# which is similar to a list in that it is a collection of objects.
# Here’s what you’ll learn in this tutorial: You’ll cover the basic
# characteristics of Python dictionaries and learn how to access and
# manage dictionary data. Once you have finished this tutorial, you
# should have a good sense of when a dictionary is the appropriate data
# type to use, and how to do so.
# Dictionaries and lists share the following characteristics:
# Both are mutable.
# Both are dynamic. They can grow and shrink as needed.
# Both can be nested. A list can contain another list.
# A dictionary can contain another dictionary.
# A dictionary can also contain a list, and vice versa.
# Dictionaries differ from lists primarily in how elements are accessed:
# List elements are accessed by their position in the list, via indexing.
# Dictionary elements are accessed via keys.

from operator import itemgetter
# Defining a Dictionary
# Dictionaries are Python’s implementation of a data structure that is more
# generally known as an associative array.
# A dictionary consists of a collection of key-value pairs.
# Each key-value pair maps the key to its associated value.
# You can define a dictionary by enclosing a comma-separated list of
# key-value pairs in curly braces ({}).
# A colon (:) separates each key from its associated value:
# d = {
#     <key>: <value>,
#     <key>: <value>,
#       .
#       .
#       .
#     <key>: <value>
# }
# The following defines a dictionary that maps a location to the name of its
# corresponding Major League Baseball team:
from timeit import timeit

MLB_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}
# You can also construct a dictionary with the built-in dict() function.
# The argument to dict() should be a sequence of key-value pairs.
# A list of tuples works well for this:
# d = dict([
#     (<key>, <value>),
#     (<key>, <value),
#       .
#       .
#       .
#     (<key>, <value>)
# ])
# MLB_team can then also be defined this way:
MLB_team = dict([
    ('Colorado', 'Rockies'),
    ('Boston', 'Red Sox'),
    ('Minnesota', 'Twins'),
    ('Milwaukee', 'Brewers'),
    ('Seattle', 'Mariners')
])
# If the key values are simple strings, they can be specified as
# keyword arguments. So here is yet another way to define MLB_team:
MLB_team = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Mariners'
)
# Once you’ve defined a dictionary, you can display its contents, the same
# as you can do for a list. All three of the definitions shown above appear
# as follows when displayed:
print(type(MLB_team))
print(MLB_team)
# The entries in the dictionary display in the order they were defined.
# But that is irrelevant when it comes to retrieving them.
# Dictionary elements are not accessed by numerical index

# Accessing Dictionary Values
# Of course, dictionary elements must be accessible somehow.
# If you don’t get them by index, then how do you get them?
# A value is retrieved from a dictionary by specifying its corresponding key
# in square brackets ([]):
print(MLB_team['Boston'])
print(MLB_team['Milwaukee'])
# If you refer to a key that is not in the dictionary,
# Python raises an exception:
try:
    print(MLB_team['Chalanga'])
except KeyError as e:
    print('KeyError:', e)
# Adding an entry to an existing dictionary is simply a matter of assigning
# a new key and value:
MLB_team['Kansas City'] = 'Royals'
print(MLB_team)
# If you want to update an entry, you can just assign a new value
# to an existing key:
MLB_team['Kansas City'] = 'Chalanga'
print(MLB_team)
# To delete an entry, use the del statement, specifying the key to delete:
del MLB_team['Kansas City']
print(MLB_team)

# Dictionary Keys vs. List Indices
# You may have noticed that the interpreter raises the same exception,
# KeyError, when a dictionary is accessed with either an undefined key or
# by a numeric index.
# >>> MLB_team['Toronto']
# Traceback (most recent call last):
#   File "<pyshell#8>", line 1, in <module>
#     MLB_team['Toronto']
# KeyError: 'Toronto'
# >>> MLB_team[1]
# Traceback (most recent call last):
#   File "<pyshell#9>", line 1, in <module>
#     MLB_team[1]
# KeyError: 1
# In fact, it’s the same error. In the latter case,
# [1] looks like a numerical index, but it isn’t.
# You will see later in this tutorial that an object of any immutable type
# can be used as a dictionary key. Accordingly, there is no reason you
# can’t use integers:
d = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
print(d[0])
print(d[2])
# In the expressions MLB_team[1], d[0], and d[2], the numbers in square
# brackets appear as though they might be indices.
# But they have nothing to do with the order of the items in the dictionary.
# Python is interpreting them as dictionary keys.
# If you define this same dictionary in reverse order,
# you still get the same values using the same keys:
d = {3: 'd', 2: 'c', 1: 'b', 0: 'a'}
print(d[0])
print(d[2])

# The syntax may look similar, but you can’t treat a dictionary like a list:
# >>> type(d)
# <class 'dict'>
# >>> d[-1]
# Traceback (most recent call last):
#   File "<pyshell#30>", line 1, in <module>
#     d[-1]
# KeyError: -1
# >>> d[0:2]
# Traceback (most recent call last):
#   File "<pyshell#31>", line 1, in <module>
#     d[0:2]
# TypeError: unhashable type: 'slice'
# >>> d.append('e')
# Traceback (most recent call last):
#   File "<pyshell#32>", line 1, in <module>
#     d.append('e')
# AttributeError: 'dict' object has no attribute 'append'
# Note: Although access to items in a dictionary does not depend on order,
# Python does guarantee that the order of items in a dictionary is preserved.
# When displayed, items will appear in the order they were defined,
# and iteration through the keys will occur in that order as well.
# Items added to a dictionary are added at the end.
# If items are deleted, the order of the remaining items is retained.
# You can only count on this preservation of order very recently.
# It was added as a part of the Python language specification in version 3.7.
# However, it was true as of version 3.6 as well—by happenstance as a result
# of the implementation but not guaranteed by the language specification.

# Building a Dictionary Incrementally
# Defining a dictionary using curly braces and a list of key-value pairs,
# as shown above, is fine if you know all the keys and values in advance.
# But what if you want to build a dictionary on the fly?
# You can start by creating an empty dictionary, which is specified by empty
# curly braces. Then you can add new keys and values one at a time:
person = {}
print(type(person))

person['fname'] = 'Joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
# Once the dictionary is created in this way, its values are accessed the same
# way as any other dictionary:
print(person)
print(person['children'])
# Retrieving the values in the sublist or subdictionary requires an additional
# index or key:
print(person['children'][-1])
print(person['pets']['dog'])
# This example exhibits another feature of dictionaries:
# the values contained in the dictionary don’t need to be the same type.
# In person, some of the values are strings, one is an integer, one is a list,
# and one is another dictionary.
# Just as the values in a dictionary don’t need to be of the same type,
# the keys don’t either:
# >>> foo = {42: 'aaa', 2.78: 'bbb', True: 'ccc'}
# >>> foo
# {42: 'aaa', 2.78: 'bbb', True: 'ccc'}
# >>> foo[42]
# 'aaa'
# >>> foo[2.78]
# 'bbb'
# >>> foo[True]
# 'ccc'
# Here, one of the keys is an integer, one is a float, and one is a Boolean.
# It’s not obvious how this would be useful, but you never know.
# Notice how versatile Python dictionaries are.
# In MLB_team, the same piece of information (the baseball team name) is kept
# for each of several different geographical locations.
# person, on the other hand, stores varying types of data for a single person.
# You can use dictionaries for a wide range of purposes because there are so
# few limitations on the keys and values that are allowed. But there are some.
# Read on!

# Restrictions on Dictionary Keys
# Almost any type of value can be used as a dictionary key in Python.
# You just saw this example, where integer, float, and Boolean objects are
# used as keys
# You can even use built-in objects like types and functions:
# >>> d = {int: 1, float: 2, bool: 3}
# >>> d
# {<class 'int'>: 1, <class 'float'>: 2, <class 'bool'>: 3}
# >>> d[float]
# >>> d = {bin: 1, hex: 2, oct: 3}
# >>> d[oct]
# However, there are a couple restrictions that dictionary keys must abide by.
# First, a given key can appear in a dictionary only once.
# Duplicate keys are not allowed.
# A dictionary maps each key to a corresponding value,
# so it doesn’t make sense to map a particular key more than once.
# You saw above that when you assign a value to an already existing dictionary
# key, it does not add the key a second time, but replaces the existing value
# Secondly, a dictionary key must be of a type that is immutable.
# You have already seen examples where several of the immutable types you
# are familiar with—integer, float, string, and Boolean—have served as
# dictionary keys.
# A tuple can also be a dictionary key, because tuples are immutable:
d = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}
print(d[(1, 1)])
# Technical Note:
# Technically, it is not quite correct to say an object must be immutable to
# be used as a dictionary key. More precisely, an object must be hashable,
# which means it can be passed to a hash function.
# A hash function takes data of arbitrary size and maps it to a relatively
# simpler fixed-size value called a hash value (or simply hash),
# which is used for table lookup and comparison.
# Python’s built-in hash() function returns the hash value for an object
# which is hashable, and raises an exception for an object which isn’t:
print(hash('foo'))
# All of the built-in immutable types you have learned about so far
# are hashable, and the mutable container types (lists and dictionaries)
# are not. So for present purposes, you can think of hashable and immutable
# as more or less synonymous.
# In future tutorials, you will encounter mutable objects which are also
# hashable.

# Restrictions on Dictionary Values
# By contrast, there are no restrictions on dictionary values.
# Literally none at all. A dictionary value can be any type of object
# Python supports, including mutable types like lists and dictionaries,
# and user-defined objects, which you will learn about in upcoming tutorials.
# There is also no restriction against a particular value appearing in a
# dictionary multiple times

# Operators and Built-in Functions
# You have already become familiar with many of the operators and built-in
# functions that can be used with strings, lists, and tuples.
# Some of these work with dictionaries as well.
# For example, the in and not in operators return True or False according to
# whether the specified operand occurs as a key in the dictionary:
print('Milwaukee' in MLB_team)
print('Toronto' in MLB_team)
print('Toronto' not in MLB_team)
# You can use the in operator together with short-circuit evaluation to avoid
# raising an error when trying to access a key that is not in the dictionary:
print('Milwaukee' in MLB_team and MLB_team['Milwaukee'])
print('Toronto' in MLB_team and MLB_team['Toronto'])
# In the second case, due to short-circuit evaluation,
# the expression MLB_team['Toronto'] is not evaluated,
# so the KeyError exception does not occur.
# The len() function returns the number of key-value pairs in a dictionary:
print(len(MLB_team))

# Built-in Dictionary Methods
# As with strings and lists, there are several built-in methods that can be
# invoked on dictionaries.
# In fact, in some cases, the list and dictionary methods share the same name.
# (In the discussion on object-oriented programming, you will see that it
# is perfectly acceptable for different types to have methods with the same
# name.)
# The following is an overview of methods that apply to dictionaries:

# d.clear()
# Clears a dictionary.
# d.clear() empties dictionary d of all key-value pairs:
d = {'a': 10, 'b': 20, 'c': 30}
print(d)
d.clear()
print(d)

# d.get(<key>[, <default>])
# Returns the value for a key if it exists in the dictionary.
# The Python dictionary .get() method provides a convenient way of getting the
# value of a key from a dictionary without checking ahead of time whether the
# key exists, and without raising an error.
# d.get(<key>) searches dictionary d for <key> and returns the associated value
# if it is found. If <key> is not found, it returns None by <default>:
d = {'a': 10, 'b': 20, 'c': 30}
print(d.get('b'))
print(d.get('e'))
print(d.get('e', 'No key with this name'))

# d.items()
# Returns a list of key-value pairs in a dictionary.
# d.items() returns a list of tuples containing the key-value pairs in d.
# The first item in each tuple is the key, and the second item is the key’s
# value:
print(d.items())
print(list(d.items()))

# d.keys()
# Returns a list of keys in a dictionary.
# d.keys() returns a list of all keys in d:
print(d.keys())
print(list(d.keys()))

# d.values()
# Returns a list of values in a dictionary.
# d.values() returns a list of all values in d:
print(d.values())
print(list(d.values()))

# Technical Note: The .items(), .keys(), and .values() methods actually return
# something called a view object. A dictionary view object is more or less like
# a window on the keys and values. For practical purposes, you can think of
# these methods as returning lists of the dictionary’s keys and values.

# d.pop(<key>[, <default>])
# Removes a key from a dictionary, if it is present, and returns its value.
# If <key> is present in d, d.pop(<key>) removes <key> and returns its
# associated value:
print(d.pop('b'))
# d.pop(<key>) raises a KeyError exception if <key> is not in d
# If <key> is not in d, and the optional <default> argument is specified,
# then that value is returned, and no exception is raised:
print(d.pop('z', -1))

# d.popitem()
# Removes a key-value pair from a dictionary.
# d.popitem() removes the last key-value pair added from d and returns it as
# a tuple:
d = {'a': 10, 'b': 20, 'c': 30}
print(d.popitem())
# If d is empty, d.popitem() raises a KeyError exception.
# Note: In Python versions less than 3.6, popitem() would return an
# arbitrary (random) key-value pair since Python dictionaries were unordered
# before version 3.6.

# d.update(<obj>)
# Merges a dictionary with another dictionary or with an iterable of
# key-value pairs.
# If <obj> is a dictionary, d.update(<obj>) merges the entries from
# <obj> into d.
# For each key in <obj>:
# If the key is not present in d, the key-value pair from <obj> is added to d.
# If the key is already present in d,
# the corresponding value in d for that key is updated to the value from <obj>.
# Here is an example showing two dictionaries merged together:
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
print(d1)
d1.update(d2)
print(d1)
# In this example, key 'b' already exists in d1, so its value is updated to
# 200, the value for that key from d2. However, there is no key 'd' in d1,
# so that key-value pair is added from d2.
# <obj> may also be a sequence of key-value pairs, similar to when the
# dict() function is used to define a dictionary. For example, <obj> can be
# specified as a list of tuples:
d1 = {'a': 10, 'b': 20, 'c': 30}
d1.update([('b', 200), ('d', 400)])
print(d1)
# Or the values to merge can be specified as a list of keyword arguments:
d1 = {'a': 10, 'b': 20, 'c': 30}
d1.update(b=200, d=400)
print(d1)

# Sorting a Python Dictionary: Values, Keys, and More
# You’ve got a dictionary, but you’d like to sort the key-value pairs.
# Perhaps you’ve tried passing a dictionary to the sorted() function but
# haven’t gotten the results you expected. In this tutorial,
# you’ll go over everything you need to know if you want to
# sort dictionaries in Python.
# In this tutorial, you’ll:
# Review how to use the sorted() function
# Learn how to get dictionary views to iterate over
# Understand how dictionaries are cast to lists during sorting
# Learn how to specify a sort key to sort a dictionary by value, key,
# or nested attribute
# Review dictionary comprehensions and the dict() constructor to rebuild your
# dictionaries
# Consider alternative data structures for your key-value data
# Along the way, you’ll also use the timeit module to time your code and get
# tangible results for comparing the different methods of sorting key-value
# data. You’ll also consider whether a sorted dictionary is really your best
# option, as it’s not a particularly common pattern.
# To get the most out of this tutorial, you should know about dictionaries,
# lists, tuples, and functions. With that knowledge, you’ll be able to sort
# dictionaries by the end of this tutorial.
# Some exposure to higher-order functions, such as lambda functions,
# will also come in handy but isn’t a requirement.

# Rediscovering Dictionary Order in Python
# Before Python 3.6, dictionaries were inherently unordered.
# A Python dictionary is an implementation of the hash table,
# which is traditionally an unordered data structure.
# As a side effect of the compact dictionary implementation in Python 3.6,
# dictionaries started to conserve insertion order.
# From 3.7, that insertion order has been guaranteed.
# If you wanted to keep an ordered dictionary as a data structure before
# compact dictionaries, then you could use OrderedDict from the
# collections module. Similar to the modern compact dictionary, it also keeps
# insertion order, but neither type of dictionary sorts itself.
# Another alternative for storing an ordered key-value pair data is to store
# the pairs as a list of tuples. As you’ll see later in the tutorial,
# using a list of tuples could be the best choice for your data.
# An essential point to understand when sorting dictionaries is that even
# though they conserve insertion order, they’re not considered a sequence.
# A dictionary is like a set of key-value pairs, and sets are unordered.
# Dictionaries also don’t have much reordering functionality.
# They’re not like lists, where you can insert elements at any position.
# In the next section, you’ll explore the consequences of this
# limitation further.

# Understanding What Sorting A Dictionary Really Means
# Because dictionaries don’t have much reordering functionality, when sorting a
# dictionary, it’s rarely done in-place. In fact, there are no methods for
# explicitly moving items in a dictionary.
# If you wanted to sort a dictionary in-place, then you’d have to use the
# del keyword to delete an item from the dictionary and then add it again.
# Deleting and then adding again effectively moves the key-value pair to the
# end The OrderedDict class has a specific method to move an item to the end or
# the start, which may make OrderedDict preferable for keeping a sorted
# dictionary. However, it’s still not very common and isn’t very performant,
# to say the least.
# The typical method for sorting dictionaries is to get a dictionary view,
# sort it, and then cast the resulting list back into a dictionary.
# So you effectively go from a dictionary to a list and back into a dictionary.
# Depending on your use case, you may not need to convert the list back into
# a dictionary.

# Sorting Dictionaries in Python
# In this section, you’ll be putting together the components of sorting a
# dictionary so that, in the end, you can master the most common way
# of sorting a dictionary:
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
# Sort by key
print(dict(sorted(people.items())))
# Sort by value
print(dict(sorted(people.items(), key=lambda item: item[1])))

# Using the sorted() Function
# The critical function that you’ll use to sort dictionaries is the built-in
# sorted() function. This function takes an iterable as the main argument,
# with two optional keyword-only arguments—a key function and a reverse
# Boolean value.
# To illustrate the sorted() function’s behavior in isolation,
# examine its use on a list of numbers:
numbers = [5, 3, 4, 3, 6, 7, 3, 2, 3, 4, 1]
print(sorted(numbers))
words = ["aa", "ab", "ac", "ba", "cb", "ca"]
print(sorted(words))
# Sorting by numerical or alphabetical precedence is the most common way to
# sort elements, but maybe you need more control.
# Say you want to sort on the second character of each word in the last
# example. To customize what the sorted() function uses to sort the elements,
# you can pass in a callback function to the key parameter.
# A callback function is a function that’s passed as an argument to another
# function. For sorted(), you pass it a function that acts as a sort key.
# The sorted() function will then call back the sort key for every element.
# In the following example, the function passed as the key accepts a string and
# will return the second character of that string:


def select_second_character(word):
    return word[1]


print(sorted(words, key=select_second_character))

# The sorted() function passes every element of the words iterable to the key
# function and uses the return value for comparison. Using the key means that
# the sorted() function will compare the second letter instead of comparing the
# whole string directly.
# More examples and explanations of the key parameter will come later in the
# tutorial when you use it to sort dictionaries by values or nested elements.
# If you take another look at the results of this last sorting, you may notice
# the stability of the sorted() function. The three elements, aa, ba and ca,
# are equivalent when sorted by their second character. Because they’re equal,
# the sorted() function conserves their original order.
# Python guarantees this stability.
# Note: Every list also has a .sort() method, which has the same signature as
# the sorted() function. The main difference is that the .sort() method sorts
# the list in-place. In contrast, the sorted() function returns a new list,
# leaving the original list unmodified.
# You can also pass reverse=True to the sorting function or method to return
# the reverse order. Alternatively, you can use the reversed() function to
# invert the iterable after sorting:
# >>> list(reversed([3, 2, 1]))
# [1, 2, 3]
# If you want to dive deeper into the mechanics of sorting in Python and
# learn how to sort data types other than dictionaries, then check out the
# tutorial on how to use sorted() and .sort()
# So, how about dictionaries? You can actually take the dictionary and feed it
# straight into the sorted() function:
# >>> people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
# >>> sorted(people)
# [1, 2, 3, 4]
# But the default behavior of passing in a dictionary directly to the sorted()
# function is to take the keys of the dictionary, sort them, and return a list
# of the keys only. That’s probably not the behavior you had in mind!
# To preserve all the information in a dictionary, you’ll need to be acquainted
# with dictionary views.


# Getting Keys, Values, or Both From a Dictionary
# If you want to conserve all the information from a dictionary when sorting
# it, the typical first step is to call the .items() method on the dictionary.
# Calling .items() on the dictionary will provide an iterable of tuples
# representing the key-value pairs:
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
print(people.items())
# The .items() method returns a read-only dictionary view object,
# which serves as a window into the dictionary.
# This view is not a copy or a list—it’s a read-only iterable that’s actually
# linked to the dictionary it was generated from:
view = people.items()
people[2] = 'Elvis'
print(people.items())
# You’ll notice that any updates to the dictionary also get reflected in the
# view because they’re linked. A view represents a lightweight way to iterate
# over a dictionary without generating a list first.
# Note: You can use .values() to get a view of the values only and .keys()
# to get one with only the keys.
# Crucially, you can use the sorted() function with dictionary views.
# You call the .items() method and use the result as an argument to the
# sorted() function. Using .items() keeps all the information from the
# dictionary:
print(sorted(view))
# This example results in a sorted list of tuples, with each tuple
# representing a key-value pair of the dictionary.
# If you want to end up with a dictionary sorted by values,
# then you’ve still got two issues.
# The default behavior still seems to sort by key and not value.
# The other issue is that you end up with a list of tuples, not a dictionary.
# First, you’ll figure out how to sort by value.

# Understanding How Python Sorts Tuples
# When using the .items() method on a dictionary and feeding it into the
# sorted() function, you’re passing in an iterable of tuples, and the sorted()
# function compares the entire tuple directly.
# When comparing tuples, Python behaves a lot like it’s sorting strings
# alphabetically. That is, it sorts them lexicographically.
# Lexicographical sorting means that if you have two tuples, (1, 2, 4) and
# (1, 2, 3), then you start by comparing the first item of each tuple.
# The first item is 1 in both cases, which is equal. The second element, 2, is
# also identical in both cases. The third elements are 4 and 3, respectively.
# Since 3 is less than 4, you’ve found which item is less than the other.
# So, to order the tuples (1, 2, 4) and (1, 2, 3) lexicographically, you would
# switch their order to (1, 2, 3) and (1, 2, 4).
# Because of Python’s lexicographic sorting behavior for tuples, using the
# .items() method with the sorted() function will always sort by keys unless
# you use something extra.

# Using the key Parameter and Lambda Functions
# For example, if you want to sort by value, then you have to specify a sort
# key. A sort key is a way to extract a comparable value. For instance, if
# you have a pile of books, then you might use the author surname as the sort
# key. With the sorted() function, you can specify a sort key by passing a
# callback function as a key argument.
# Note: The key argument has nothing to do with a dictionary key!
# To see a sort key in action, take a look at this example, which is similar
# to the one you saw in the section introducing the sorted() function:


def value_getter(item):
    return item[1]


# with normal function
print(sorted(people.items(), key=value_getter))
# or lambda function
print(sorted(people.items(), key=lambda item: item[1]))

# In this example, you try out two ways of passing a key parameter.
# The key parameter accepts a callback function.
# The function can be a normal function identifier or a lambda function.
# The lambda function in the example is the exact equivalent of the
# value_getter() function.
# Note: Lambda functions are also known as anonymous functions because they don’t
# have a name. Lambda functions are standard for functions that you’re only
# using once in your code.
# Lambda functions confer no benefit apart from making things more compact,
# eliminating the need to define a function separately.
# They keep things nicely contained on the same line:
# For basic getter functions like the one in the example,
# lambdas can come in handy. But lambdas can make your code less readable for
# anything more complex, so use them with care.
# Lambdas can also only ever contain exactly one expression, making any
# multiline statements like if statements or for loops off limits.
# You can work around this by using comprehensions and if expressions,
# for example, but those can make for long and cryptic one-liners.
# The key callback function will receive each element of the iterable that
# it’s sorting. The callback function’s job is to return something that can
# be compared, such as a number or a string. In this example, you named the
# function value_getter() because all it does is get the value from a
# key-value tuple.
# Since the default behavior of sorted() with tuples is to sort
# lexicographically, the key parameter allows you to select a value from the
# element that it’s comparing.
# In the next section, you’ll take sort keys a bit further and use them to
# sort by a nested value.

# Selecting a Nested Value With a Sort Key
# You can also go further and use a sort key to select nested values that may
# or may not be present and return a default value if they’re not present:
data = {
    193: {"name": "John", "age": 30, "skills": {"python": 8, "js": 7}},
    209: {"name": "Bill", "age": 15, "skills": {"python": 6}},
    746: {"name": "Jane", "age": 58, "skills": {"js": 2, "python": 5}},
    109: {"name": "Jill", "age": 83, "skills": {"java": 10}},
    984: {"name": "Jack", "age": 28, "skills": {"c": 8, "assembly": 7}},
    765: {"name": "Penelope", "age": 76, "skills": {"python": 8, "go": 5}},
    598: {"name": "Sylvia", "age": 62, "skills": {"bash": 8, "java": 7}},
    483: {"name": "Anna", "age": 24, "skills": {"js": 10}},
    277: {"name": "Beatriz", "age": 26, "skills": {"python": 2, "js": 4}},
}


def get_relevant_skills(item):
    """Get the sum of Python and JavaScript skill"""
    skills = item[1]["skills"]

    # Return default value that is equivalent to no skill
    return skills.get("python", 0) + skills.get("js", 0)


print(sorted(data.items(), key=get_relevant_skills, reverse=True))
# In this example, you have a dictionary with numeric keys and a nested
# dictionary as a value. You want to sort by the combined Python and
# JavaScript skills, attributes found in the skills subdictionary.
# Part of what makes sorting by the combined skill tricky is that the python
# and js keys aren’t present in the skills dictionary for all people.
# The skills dictionary is also nested. You use .get() to read the keys and
# provide 0 as a default value that’s used for missing skills.
# You’ve also used the reverse argument because you want the top Python skills
# to appear first.
# Note: You didn’t use a lambda function in this example.
# While it’s possible, it would make for a long line of potentially
# cryptic code:
# sorted(
#     data.items(),
#     key=lambda item: (
#         item[1]["skills"].get("python", 0)
#         + item[1]["skills"].get("js", 0)
#     ),
#     reverse=True,
# )
# A lambda function can only contain one expression,
# so you repeat the full look-up in the nested skills subdictionary.
# This inflates the line length considerably.
# The lambda function also requires multiple chained
# square bracket ([]) indices, making it harder to read than necessary.
# Using a lambda in this example only saves a few lines of code, and the
# performance difference is negligible. So, in these cases, it usually makes
# more sense to use a normal function.
# You’ve successfully used a higher-order function as a sort key to sort a
# dictionary view by value. That was the hard part.
# Now there’s only one issue left to solve—converting the list that sorted()
# yields back into a dictionary.

# Converting Back to a Dictionary
# The only issue left to address with the default behavior of sorted() is that
# it returns a list, not a dictionary.
# There are a few ways to convert a list of tuples back into a dictionary.
# You can iterate over the result with a for loop and populate a
# dictionary on each iteration:
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
sorted_people = sorted(people.items(), key=lambda item: item[1])
sorted_people_dict = {}
for key, value in sorted_people:
    sorted_people_dict[key] = value
print(sorted_people_dict)
# This method gives you absolute control and flexibility in deciding how you
# want to construct your dictionary. This method can be quite lengthy to type
# out, though. If you don’t have any special requirements for constructing
# your dictionary, then you may want to go for a dictionary constructor
# instead:
print(dict(sorted_people))
# That’s nice and compact! You could also use a dictionary comprehension,
# but that only makes sense if you want to change the shape of the dictionary
# or swap the keys and values, for example.
# In the following comprehension, you swap the keys and values:
print({value: key for key, value in sorted_people})
# Depending on how familiar you or your team are with comprehensions, this may
# be less readable than just using a normal for loop.
# Congratulations, you’ve got your sorted dictionary!
# You can now sort it by any criteria that you’d like.
# Now that you can sort your dictionary,
# you might be interested in knowing if there are any performance implications
# to using a sorted dictionary, or whether there are alternative data
# structures for key-value data.

# Considering Strategic and Performance Issues
# In this section, you’ll be taking a quick peek at some performance tweaks,
# strategic considerations, and questions to ask yourself about how you’ll
# use your key-value data.
# Note: If you decide to go for an ordered collection, check out the Sorted
# Containers package, which includes a SortedDict.
# You’ll be leveraging the timeit module to get some metrics to work with.
# It’s important to bear in mind that to make any solid conclusions about
# performance, you need to test on a variety of hardware, and with a variety
# of sample types and sizes.
# Finally, note that you won’t be going into detail about how to use timeit.
# For that, check out the tutorial on Python timers.
# You’ll have some examples to play with, though.

# Using Special Getter Functions to Increase Performance and Readability
# You may have noticed that most of the sort key functions that you’ve used
# so far aren’t doing very much. All the function does is get a value from
# a tuple. Making a getter function is such a common pattern that Python has
# a special way to create special functions that get values more quickly than
# regular functions.
# The itemgetter() function can produce highly efficient versions of
# getter functions.
# You pass itemgetter() an argument, which is typically the key or index
# position that you want to select. The itemgetter() function will then return
# a getter object that you call like a function.
# That’s right, it’s a function that returns a function.
# Using the itemgetter() function is another example of working with
# higher-order functions.

# The getter object from itemgetter() will call the .__getitem__() method
# on the item that’s passed to it.
# When something makes a call to .__getitem__(),
# it needs to pass in the key or index of what to get.
# The argument that’s used for .__getitem__() is the same argument that you
# passed to itemgetter():
item = ('name', 'Guido')
getter = itemgetter(0)
print(getter(item))
getter = itemgetter(1)
print(getter(item))

# In the example, you start off with a tuple, similar to one that you might
# get as part of a dictionary view.
# You make the first getter by passing 0 as an argument to itemgetter().
# When the resultant getter receives the tuple,
# it returns the first item in the tuple—the value at index 0.
# If you call itemgetter() with an argument of 1,
# then it gets the value at index position 1.
# You can use this itemgetter as a key for the sorted() function:
fruit_inventory = [
    ("banana", 5), ("orange", 15), ("apple", 3), ("kiwi", 0)
]
print(sorted(fruit_inventory, key=itemgetter(0)))
print(sorted(fruit_inventory, key=itemgetter(1)))
# >>> sorted(fruit_inventory, key=itemgetter(2))
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#     sorted(fruit_inventory, key=itemgetter(2))
# IndexError: tuple index out of range
# In this example, you start by using itemgetter() with 0 as an argument.
# Since it’s operating on each tuple from the fruit_inventory variable,
# it gets the first element from each tuple. Then the example demonstrates
# initializing an itemgetter with 1 as an argument, which selects the second
# item in the tuple.
# Finally, the example shows what would happen if you used itemgetter() with
# 2 as an argument. Since these tuples only have two index positions,
# trying to get the third element, with index 2, results in a IndexError.
# You can use the function produced by itemgetter() in place of the getter
# functions that you’ve been using up until now:
print(sorted(people.items(), key=itemgetter(1)))
# The itemgetter() function produces a function that has exactly the same
# effect as the value_getter() function from previous sections.
# The main reason you’d want to use the function from itemgetter()
# is because it’s more efficient.
# In the next section, you’ll start to put some numbers on just how much
# more efficient it is.

# Measuring Performance When Using itemgetter()
# So, you end up with a function that behaves like the original value_getter()
# from the previous sections, except that the version returned from
# itemgetter() is more efficient. You can use the timeit module to compare
# their performance:
dict_to_order = {
    1: "requests",
    2: "pip",
    3: "jinja",
    4: "setuptools",
    5: "pandas",
    6: "numpy",
    7: "black",
    8: "pillow",
    9: "pyparsing",
    10: "boto3",
    11: "botocore",
    12: "urllib3",
    13: "s3transfer",
    14: "six",
    15: "python-dateutil",
    16: "pyyaml",
    17: "idna",
    18: "certifi",
    19: "typing-extensions",
    20: "charset-normalizer",
    21: "awscli",
    22: "wheel",
    23: "rsa",
}

sorted_with_lambda = "sorted(dict_to_order.items(), key=lambda item: item[1])"
sorted_with_itemgetter = "sorted(dict_to_order.items(), key=itemgetter(1))"

sorted_with_lambda_time = timeit(stmt=sorted_with_lambda, globals=globals())
sorted_with_itemgetter_time = timeit(
    stmt=sorted_with_itemgetter,
    setup="from operator import itemgetter",
    globals=globals(),
)

print(
    f"""\
{sorted_with_lambda_time=:.2f} seconds
{sorted_with_itemgetter_time=:.2f} seconds
itemgetter is {(
    sorted_with_lambda_time / sorted_with_itemgetter_time
):.2f} times faster"""
)

# This code uses the timeit module to compare the sorting processes of the
# function from itemgetter() and a lambda function.
# Running this script from the shell should give you similar results to what’s
# below:
# $ python compare_lambda_vs_getter.py
# sorted_with_lambda_time=1.81 seconds
# sorted_with_itemgetter_time=1.29 seconds
# itemgetter is 1.41 times faster
# A savings of around 40 percent is significant!
# Bear in mind that when timing code execution, times can vary significantly
# between systems. That said, in this case, the ratio should be relatively
# stable across systems.
# From the results of this test, you can see that using itemgetter()
# is preferable from a performance standpoint. Plus, it’s part of the Python
# standard library, so there’s no cost to using it.
# Note: The difference between using a lambda and a normal function as the
# sort key is negligible in this test.
# Do you want to compare the performance of some operations that you haven’t
# covered here? Be sure to share the results by posting them in the comments!
# Now you can squeeze a bit more performance out of your dictionary sorting,
# but it’s worth taking a step back and considering whether using a sorted
# dictionary as your preferred data structure is the best choice.
# A sorted dictionary isn’t a very common pattern, after all.
# Coming up, you’ll be asking yourself some questions about what you what you
# want to do with your sorted dictionary and whether it’s the best data
# structure for your use case.

# Judging Whether You Want to Use a Sorted Dictionary
# If you’re considering making a sorted key-value data structure,
# then there are a few things you might want to take into consideration.
# If you’re going to be adding data to a dictionary, and you want it to stay
# sorted, then you might be better off using a structure like a list of tuples
# or a list of dictionaries:
# Dictionary
# people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
# # List of tuples
# people = [
#     (3, "Jim"),
#     (2, "Jack"),
#     (4, "Jane"),
#     (1, "Jill")
# ]
# # List of dictionaries
# people = [
#     {"id": 3, "name": "Jim"},
#     {"id": 2, "name": "Jack"},
#     {"id": 4, "name": "Jane"},
#     {"id": 1, "name": "Jill"},
# ]
# A list of dictionaries is the most widespread pattern because of its
# cross-language compatibility, known as language interoperability.
# Language interoperability is especially relevant if you create an
# HTTP REST API, for instance. Making your data available over the Internet
# will likely mean serializing it in JSON.
# If someone using JavaScript were to consume JSON data from a REST API,
# then the equivalent data structure would be an object.
# The kicker is that JavaScript objects are not ordered, so the order would
# end up scrambled!
# This scrambling behavior would be true for many languages, and objects are
# even defined in the JSON specification as an unordered data structure.
# So, if you took care to order your dictionary before serializing to JSON,
# it wouldn’t matter by the time it got into most other environments.
# Note: Signposting an ordered sequence of key-value pairs may not only be
# relevant for serializing Python dictionaries into JSON. Imagine you have
# people on your team who are used to other languages.
# An ordered dictionary might be a foreign concept to them, so you may need to
# be explicit about the fact that you’ve created an ordered data structure.
# One way to be explicit about having an ordered dictionary in Python is to
# use the aptly named OrderedDict.
# Another option is to simply not worry about ordering the data if you don’t
# need to. Including id, priority, or other equivalent attributes for each
# object can be enough to express order.
# If the ordering gets mixed up for any reason, then there’ll always be an
# unambiguous way to sort it:
# people = {
#     3: {"priority": 2, "name": "Jim"},
#     2: {"priority": 4, "name": "Jack"},
#     4: {"priority": 1, "name": "Jane"},
#     1: {"priority": 2, "name": "Jill"}
# }
# With a priority attribute, for instance, it’s clear that Jane should be
# first in line. Being clear about your intended ordering is nicely in
# agreement with the old Python adage of explicit is better than implicit,
# from the Zen of Python.
# What are the performance trade-offs with using a list of dictionaries versus
# a dictionary of dictionaries, though? In the next section, you’ll start to
# get some data on just that very question.

# Comparing the Performance of Different Data Structures
# If performance is a consideration—maybe you’ll be working with large
# datasets, for example—then you should carefully consider what you’ll be
# doing with the dictionary.
# The two main questions you’ll seek to answer in the next few sections are:
# Will you be sorting once and then making lots of lookups?
# Will you be sorting many times and making very few lookups?
# Once you’ve decided what usage patterns you’ll be subjecting your data
# structure to, then you can use the timeit module to test the performance.
# These measurements can vary a lot with the exact shape and size of the data
# being tested.
# In this example, you’ll be pitting a dictionary of dictionaries against a
# list of dictionaries to see how they differ in terms of performance.
# You’ll be timing sorting operations and lookup operations with the following
# sample data:
dictionary_of_dictionaries = {
    1: {"first_name": "Dorthea", "last_name": "Emmanuele", "age": 29},
    2: {"first_name": "Evelina", "last_name": "Ferras", "age": 91},
    3: {"first_name": "Frederica", "last_name": "Livesay", "age": 99},
    4: {"first_name": "Murray", "last_name": "Linning", "age": 36},
    5: {"first_name": "Annette", "last_name": "Garioch", "age": 93},
    6: {"first_name": "Rozamond", "last_name": "Todd", "age": 36},
    7: {"first_name": "Tiffi", "last_name": "Varian", "age": 28},
    8: {"first_name": "Noland", "last_name": "Cowterd", "age": 51},
    9: {"first_name": "Dyana", "last_name": "Fallows", "age": 100},
    10: {"first_name": "Diahann", "last_name": "Cutchey", "age": 44},
    11: {"first_name": "Georgianne", "last_name": "Steinor", "age": 32},
    12: {"first_name": "Sabina", "last_name": "Lourens", "age": 31},
    13: {"first_name": "Lynde", "last_name": "Colbeck", "age": 35},
    14: {"first_name": "Abdul", "last_name": "Crisall", "age": 84},
    15: {"first_name": "Quintus", "last_name": "Brando", "age": 95},
    16: {"first_name": "Rowena", "last_name": "Geraud", "age": 21},
    17: {"first_name": "Maurice", "last_name": "MacAindreis", "age": 83},
    18: {"first_name": "Pall", "last_name": "O'Cullinane", "age": 79},
    19: {"first_name": "Kermie", "last_name": "Willshere", "age": 20},
    20: {"first_name": "Holli", "last_name": "Tattoo", "age": 88}
}

list_of_dictionaries = [
    {"id": 1, "first_name": "Dorthea", "last_name": "Emmanuele", "age": 29},
    {"id": 2, "first_name": "Evelina", "last_name": "Ferras", "age": 91},
    {"id": 3, "first_name": "Frederica", "last_name": "Livesay", "age": 99},
    {"id": 4, "first_name": "Murray", "last_name": "Linning", "age": 36},
    {"id": 5, "first_name": "Annette", "last_name": "Garioch", "age": 93},
    {"id": 6, "first_name": "Rozamond", "last_name": "Todd", "age": 36},
    {"id": 7, "first_name": "Tiffi", "last_name": "Varian", "age": 28},
    {"id": 8, "first_name": "Noland", "last_name": "Cowterd", "age": 51},
    {"id": 9, "first_name": "Dyana", "last_name": "Fallows", "age": 100},
    {"id": 10, "first_name": "Diahann", "last_name": "Cutchey", "age": 44},
    {"id": 11, "first_name": "Georgianne", "last_name": "Steinor", "age": 32},
    {"id": 12, "first_name": "Sabina", "last_name": "Lourens", "age": 31},
    {"id": 13, "first_name": "Lynde", "last_name": "Colbeck", "age": 35},
    {"id": 14, "first_name": "Abdul", "last_name": "Crisall", "age": 84},
    {"id": 15, "first_name": "Quintus", "last_name": "Brando", "age": 95},
    {"id": 16, "first_name": "Rowena", "last_name": "Geraud", "age": 21},
    {"id": 17, "first_name": "Maurice", "last_name": "MacAindreis", "age": 83},
    {"id": 18, "first_name": "Pall", "last_name": "O'Cullinane", "age": 79},
    {"id": 19, "first_name": "Kermie", "last_name": "Willshere", "age": 20},
    {"id": 20, "first_name": "Holli", "last_name": "Tattoo", "age": 88}
]
# Each data structure has the same information, except one is structured as a
# dictionary of dictionaries, and the other is a list of dictionaries.
# First up, you’ll be getting some metrics on the performance of sorting these
# two data structures.
sorting_list = "sorted(list_of_dictionaries, key=lambda item:item['age'])"
sorting_dict = """
dict(
    sorted(
        dictionary_of_dictionaries.items(), key=lambda item: item[1]['age']
    )
)
"""

sorting_list_time = timeit(stmt=sorting_list, globals=globals())
sorting_dict_time = timeit(stmt=sorting_dict, globals=globals())

print(
    f"""\
{sorting_list_time=:.2f} seconds
{sorting_dict_time=:.2f} seconds
list is {(sorting_dict_time/sorting_list_time):.2f} times faster"""
)

# This code imports the sample data structures for sorting on the age
# attribute. It may seem like you aren’t using the imports from samples,
# but it’s necessary for these samples to be in the global namespace so
# that the timeit context has access to them.
# Running the code for this test on the command line should provide you
# with some interesting results:
# Sorting a list can be almost twice as fast as the process required to sort
# a dictionary view and then create a new sorted dictionary.
# So, if you plan on sorting your data very regularly, then a list of tuples
# might be better than a dictionary for you.
# Note: Not many solid conclusions can be drawn from a single dataset like
# this. Additionally, results can vary wildly with differently sized or
# shaped data.
# These examples are a way for you to dip your toes into the timeit module
# and start to see how and why you might use it. This will give you some of
# the tools necessary to benchmark your data structures, to help you decide
# which data structure to settle on for your key-value pairs.
# If you need the extra performance, then go ahead and time your specific data
# structures. That said, beware of premature optimization!
# One of the main overheads when sorting a dictionary, as opposed to a list,
# is reconstructing the dictionary after sorting it.
# If you were to take out the outer dict() constructor,
# then you’d significantly cut the execution time.
# In the next section, you’ll be looking at the time it takes to look up
# values in a dictionary of dictionaries versus in a list of dictionaries.

# Comparing the Performance of Lookups
# However, if you plan to use the dictionary to sort your data once and use
# that dictionary mainly for lookups, then a dictionary will definitely make
# more sense than a list:
lookups = [15, 18, 19, 16, 6, 12, 5, 3, 9, 20, 2, 10, 13, 17, 4, 14, 11, 7, 8]

list_setup = """
def get_key_from_list(key):
    for item in list_of_dictionaries:
        if item["id"] == key:
            return item
"""

lookup_list = """
for key in lookups:
    get_key_from_list(key)
"""

lookup_dict = """
for key in lookups:
    dictionary_of_dictionaries[key]
"""

lookup_list_time = timeit(
    stmt=lookup_list, setup=list_setup, globals=globals()
)
lookup_dict_time = timeit(stmt=lookup_dict, globals=globals())

print(
    f"""\
{lookup_list_time=:.2f} seconds
{lookup_dict_time=:.2f} seconds
dict is {(lookup_list_time / lookup_dict_time):.2f} times faster"""
)
# This code makes a series of lookups to both the list and the dictionary.
# You’ll note that with the list, you have to write a special function to make
# a lookup. The function to make the list lookup involves going through all
# the list elements one by one until you find the target element, which isn’t
# ideal.
# Running this comparison script from the command line should yield a result
# showing that dictionary lookups are significantly faster.
# Nearly eighteen times faster! That’s a whole bunch.
# So, you certainly want to weigh the blazing speed of dictionary lookups
# against the data structure’s slower sorting. Bear in mind that this ratio
# can vary significantly from system to system, not to mention the variation
# that might come from differently sized dictionaries or lists.
# Dictionary lookups are certainly faster, though, no matter how you slice it.
# That said, if you’re just doing lookups, then you could just as easily do
# that with a regular unsorted dictionary.
# Note: You could try and optimize list lookups, for example by implementing a
# binary search algorithm to cut time off the list lookup. However, any
# benefit will only become noticeable at substantial list sizes.
# With list sizes like the ones tested here, using a binary search with the
# bisect module is significantly slower than a regular for loop.
# Now you should have a relatively good idea of some trade-offs between two
# ways to store your key-value data. The conclusion that you can reach is that,
# most of the time, if you want a sorted data structure, then you should
# probably steer clear of the dictionary, mainly for language interoperability
# reasons.
# That said, give Grant Jenks’ aforementioned sorted dictionary a try.
# It uses some ingenious strategies to get around typical performance
# drawbacks.
