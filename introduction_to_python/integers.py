# https://realpython.com/lessons/integers/
# integers
# a whole number of any length up to memory limit
a = 1
b = 10
print(a)
print(b)
print(a + b)
print(a - b)
# it can be defined in binary, hexa or octal digits
# binary
c = 0b101010111
print(c)
# octal
d = 0o454312
print(d)
# hexa
e = 0xac4d
print(e)
# it can be casted from strings
my_num = '123'
print(int(my_num) + 4, type(my_num), type(int(my_num)))

# binary representation of an int
print(bin(12))
# octal
print(oct(12))
# hexa
print(hex(12))
