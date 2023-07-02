# https://realpython.com/lessons/string-operators/
# https://realpython.com/lessons/built-in-string-functions/
# https://realpython.com/lessons/string-indexing/
# https://realpython.com/lessons/string-slicing/
# https://realpython.com/lessons/interpolating-variables-string/
# https://realpython.com/lessons/modifying-strings/
# string operators
# + * in
s = 'spam'
t = 'egg'
u = 'bacon'

print(s + ' ' + t + ' ' + u)
print(s * 5)
print(s * -5)
print(s * 0)
print(s + "-" * 5)

# in is a membership operator
print(s in "I saw spamalot")
print(s in "I saw the holly grail")
print(s not in "I saw the holly grail")

# built-in functions for strings
# ord(), chr(), len(), str()
# ord() returns the unicode point
print(ord('a'))
print(ord(' '))
print(ord('#'))
# while chr() do the reverse
print(chr(8364))
print(chr(8721))
print(chr(129363))
# len returns de length of a container
print(len(s))
# str make casting to string
n = 2032.23432
print(f'{n}, type(n): {type(n)}')
print(f'{str(n)}, len(str(n)): {len(str(n))}')

# string indexing
print(u[0])
print(u[0:2])
print(u[-1])
print(u[::2])
print(u[::-1])

u = 'mybacon'
print(u[:2] + ' ' + u[2:])
t = u[:]
print(id(u), id(t))
print(id(u) == id(t))

# interpolating variables into strings
# f-strings
item = 'clothes'
n = 1
person = 'king'
location = 'rome'
print(f'A mouse bites the {item} of {n} {person} on {location}')

# modifying strings
# strings are immutable, so the way is making a modified copy
print(s)
print(s.replace('m', 'mator'))
