# https://realpython.com/lessons/case-conversion/
# built-in string methods
# A method is a specialized type of callable procedure that is tightly
# associated with an object.
s = 'egG BacOn sAuSAGe LoBSTER'
# case conversion
print(s.capitalize())
print(s.lower())
print(s.upper())
print('EGG bacon sausage LOBSTER'.swapcase())
print(s.swapcase())
print(s.title())
# find and seek
s = 'spam ham jam clam'
print(s.count('am'))
# from index 0 to 9 (not included)
print(s.count('am', 0, 9))
print(s.endswith('am'))
print(s.endswith('clam'))
print(s.endswith('bam'))
print(s.endswith('ham', 0, 8))
print(s.startswith('ham'))
print(s.startswith('sp'))
print(s.startswith('jam', 9))

s = 'spam bacon egg sausage'
# returns -1 if not found
# give de index of first found
print(s.find('jam'))
print(s.find('bacon'))
s = 'spam bacon spam egg spam sausage'
# search from right to left
print(s.rfind('spam'))

indexes = []
n = len(s)
while True:
    n = s.rfind('spam', 0, n)
    if n == -1:
        break
    indexes.append(n)
print(indexes)
# string.index('sub') an string.rindex('sub') search for the first value too,
# but if not found it raises an exception

# classification
# all values are alphanumeric?
print(s.isalnum())
s = 'adssgs12312'
print(s.isalnum())
s = 'adssgs 12312'
print(s.isalnum())
s = 'adss$312'
print(s.isalnum())

# all alphabetic
s = 'adss$312'
print(s.isalpha())
s = 'adss$'
print(s.isalpha())
s = 'adss'
print(s.isalpha())
s = 'adss '
print(s.isalpha())

# all digits
s = 'adss$312'
print(s.isdigit())
s = '312'
print(s.isdigit())
s = '312.0'
print(s.isdigit())

# str.isidentifier() returns True if the string is a valid name for identifiers
# in python (names of variables, functions, classes ...)
# iskeyword(str) from keyword module returns True if the string is a
# reserved keyword

# all withe spaces
s = '\n\t  '
print(s.isspace())
s = 'a\n\t  '
print(s.isspace())

#  is title, is lower, is upper
s = 'Spam Bacon'
print(s.istitle())
s = 'Spam BacoN'
print(s.istitle())
s = 'spam bacon'
print(s.islower())
s = 'BACON 123#'
print(s.isupper())


# formating
s = 'spam'
print(s.center(10))
# if uses the length of string nothing changes
print(s.center(4))
print(s.center(11, '-'))
print(s.ljust(10, '.'))
print(s.rjust(10, '.'))

s = '\tspam\tbancon'
print(s.expandtabs(tabsize=10))

s = '   a   bcd  e   '
print(s.strip())
print(s.rstrip())
print(s, '.')
print(s.lstrip(), '.')

s = 'https://realpython.com/lessons/case-conversion/'
print(s.lstrip('/:htps'))
s = 'spam$$.;'
print(s.rstrip('$.;'))
s = '<h1>fulano<h1/>'
print(s.strip('<h1/>'))

s = 'spam bacon spam egg spam sausage'
print(s.replace('spam', 'tomato'))
# defining the number of replacements (count start at the beginning)
print(s.replace('spam', 'tomato', 2))

s = '42'
print(s.zfill(10))
s = '+42'
print(s.zfill(10))
s = '-42'
print(s.zfill(10))

# converting between string and list
# for lists or tuple, must be literal str
# join
my_list = ['spam', 'egg', 'sausage', 'bacon']
print('; '.join(my_list))
word = 'lobster'
print(':'.join(word))
# partition returs a len=3 tuple
s = 'egg.spam'
print(s.partition('.'))
s = 'egg.spam.bacon.'
print(s.partition('.'))
s = 'egg-spam'
print(s.partition('.'))

# beginning from right
s = 'egg.spam.bacon'
print(s.rpartition('.'))

# split
s = 'a phrase for\npythonistas'
print(s.split())
s = 'a$phrase$for pythonistas'
print(s.split('$'))
s = 'www.realpython.com'
print(s.split('.'))
s = 'www.realpython.com'
print(s.split('.', 1))

moby = 'Call me Ishmael.\nSome years ago- never mind how long precisely-' \
    '\nhaving little or no money in my purse,\nand nothing particular to ' \
    'interest me on shore,\nI thought I would sail about a little and see ' \
    'the watery part of the world.\n'
mobysplit = moby.splitlines()
print(mobysplit)
