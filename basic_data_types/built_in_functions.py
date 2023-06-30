# https://realpython.com/lessons/functions-composite-data-types/
# https://realpython.com/lessons/functions-math/
# https://realpython.com/lessons/functions-type-conversion/
# built-in functions
# Composite data types
# list, tuple
a = [1, 2, 3, 4]
b = (1, 2, 3, 4, )
# this composite elements has indexes, begining in 0
print(a[0])
print(a[1:3])
print(a[-1])
print(a[::2])
a[3] = 1
print(a)
# the main difference between the two is that tuples are immutable
# and this means you can't changes its values, remove or add new elements

# Other composite data type is set, which only have unique values
c = {1, 2, 3, 4, 5, 5, 5, 5, 8, 9}
print(c, type(c))
# but sets does not have index

# dictionary can be seen as lookup tables
d = {}
d['name'] = 'fulano'
d['age'] = 12
print(d)
# when you dont have the name called in the dict, it raises a error
# print(d['ag'])
# so the better way to know if a key exists in a dict is using the .get
# method
print(d.get('street'))

# math
# absolute value
print(abs(-3))
# modulo
print(15 % 4)
# divmod returns int division and modulo
print(divmod(15, 4))
# max and min works on iterables
print(max((1, 2, 13, 4,)))
print(max([1, 2, 13, 4]))
print(max('ABCDER'))
print(min((1, 2, 13, 4,)))
print(min([1, 2, 13, 4]))
print(min('ABCDER'))
# pow makes power and power to remainder
# same as 2 ** 2
print(pow(2, 2))
# same as (3 ** 2) % 2
print(pow(3, 2, 2))
# round returns the integer
# but remember tha it takes into acount the internal representation of floats
# round is different from int, since it make floor or upper from the float
# and int just ignores the decimal part
print(round(3.4))
print(round(3.5))
print(round(3.6))
# sum takes the summation of a iterable
print(sum((1, 2, 3, 4, 5,)))
# sum also accepts one start value
print(sum((1, 2, 3, 4, 5,), 10))

# type conversition
# ascii representation of a unicode str
print(ascii('Hello'))
print(ascii('そしてポジティブな経験'))
# chr returns unicode string from a character
print(chr(97))
print(chr(98))
print(chr(65))
print(chr(0x06a4))
print(chr(0x305d))
# ord returns unicode point
print(ord('そ'))

# iterables and iterators
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(len(my_list))

print([v == 1 for v in my_list])
print(any([v == 1 for v in my_list]))
print(all([v == 1 for v in my_list]))
# is True if at least one element is True
print([v == 9 for v in my_list])
print(any([v == 9 for v in my_list]))

# reversed returns an iterator
rev_list = reversed(my_list)
for i in rev_list:
    print(i)
print(rev_list)
print(list(rev_list))

# sort list
sort_list = sorted(rev_list)
print(sort_list)

# range
print(range(1, 10))
print(list(range(1, 10)))
