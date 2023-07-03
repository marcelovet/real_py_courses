import math

a = ['spam', 'egg', 'bacon', 'tomato']
b = ['egg', 'bacon', 'tomato', 'spam']
# order matter
print(a == b)
print(a is b)
print([1, 2, 3, 4] == [4, 1, 3, 2])

# lists can contain any object
a = [2, 4, 6, 8]
print(type(a))
a = [21.42, 'spam', 3, 4, 'egg', False, 3.14159]
print(type(a))


def foo():
    pass


a = [int, len, foo, math]
print(a)

# and can contain any number of objects
a = []
a = ['spam']
a = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
    40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50
]
# also objects don't have to be unique
a = ['bark', 'meow', 'woof', 'bark', 'cheep', 'bark']

# indexing and slicing
b = ['egg', 'bacon', 'tomato', 'spam']
print(b[0])
print(b[len(b) - 1])
print(b[-1])
print(b[2:4])
print(b[::2])
# copy to a list
print(b[:] is b)
# which is different from strings
string = 'mybacon'
print(string is string[:])

# operators and built-ins
# in
print('bacon' in b)
print('kiwi' not in b)
# concatenation
print(b + ['kiwi', 'banana'])
print(b * 2)
print(2 * b)
# length, min, max
print(len(b))
print(min(b))
print(max(b))
# for the use of min and max the list has to have methods to compare the
# instances (int and float is ok, only str, never str and int/float)
c = [1, 2, 3, 4, 4.5]
print(len(c))
print(min(c))
print(max(c))

# nested lists
nested_list = [
    'a', [
        'bb', ['ccc', 'ddd'], 'ee', 'ff'
    ], 'g', [
        'hh', 'ii'
    ], 'j'
]
print(nested_list)
print('level 1:', nested_list[0], nested_list[2], nested_list[4])
print(
    'level 2:',
    nested_list[1][0],
    nested_list[1][2], nested_list[1][3],
    nested_list[3][0], nested_list[3][1]
)
print('level 3:', nested_list[1][1][0], nested_list[1][1][1])
print('ddd' in nested_list)
print('ddd' in nested_list[1])
print('ddd' in nested_list[1][1])

# The list is a data type that is mutable. Once a list has been created:
# Elements can be modified.
# Individual values can be replaced.
# The order of elements can be changed.
print(a)
a[1] = 'ionnn'
print(a)

a[3:] = [a[3]]
print(a)
a[1:3] = [1, 2, 3, 4, 5]
print(a)

# append items
print(b)
# augmented operator with we have another iterable
b += ['item1', 'item2', 'item3']
print(b)
# or append method if we have a non iterable
b.append('item4')
print(b)

# most list methods modify in place the list and returns None
b.extend('iterable')
print(b)
b.insert(2, 'new_item')
print(b)
b.remove('new_item')
# remove raises ValueError if the item is not in the list
print(b)
c = [1, 2, 3, 4, 5]
print(c)
c.clear()
print(c)
b.sort()
print(b)
b.sort(reverse=True)
print(b)
b += ['A', 'B', 'C']
b.sort(key=str.upper)
print(b)
b.reverse()
print(b)

# methods with return values
# remove and the last index (-1) by default
print(b.pop())
print(b.pop(1))
# search and return the index of the item
# raises ValueError if the item is not in the list
print(b.index('item1'))
b *= 3
print(b.count('item1'))
# copy returns a shallow copy of the list
# means that for sublists (mutable types) inside a list
# only the references to the values are copied
b = b[:7]
c = b.copy()
print(b)
print(c)
c[0] = 'bacon'
print(b)
print(c)

print()

b[2] = [2, 1]
c = b.copy()
print(b)
print(c)
c[2][1] = 'bacon'
print(b)
print(c)
