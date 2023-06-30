# https://realpython.com/lessons/floats/
# float point numbers
# any number with decimal point
a = 4.2
print(a, type(a))
# a division always returns a float
b = 4 / 2
print(b, type(b))
# integer division
c = 4 // 2
print(c, type(c))
# it returns the integer part of a division
d = 5 // 2
print(d, type(d))
# casting a float
print(float(3))
print(float('3'))
# float can be defined in scientific notation
# 3 * 10 ^ 2 and 3 * 10 ^ -2
print(3e2)
print(3e-2)
# float mathematical operations can result in unexpected results
# because of the way they are represented in the computer
a = 0.2
b = 0.1
c = a + b
print(c)
