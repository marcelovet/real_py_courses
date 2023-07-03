a = ('spam', 'egg', 'bacon', 'tomato')
print(a)
print(a[0])
print(a[1:3])
print(a[-1])
print(a[::-1])
# for singleton tuples
t = (1, )
t = tuple([1])

# tuple pack and unpack
a1, a2, a3, a4 = a
# same as
(a1, a2, a3, a4) = a
print(a1)
# pack all remaining values on a3
a1, a2, *a3 = a
print(a3)

# swapping
print((a1, a2))
a1, a2 = a2, a1
print((a1, a2))

# fibonnaci sequence (F(n) = F(n-1) + F(n-2) for n>1)
num1, num2 = 0, 1
print(num1, end=", ", sep=', ')
while num1 < 30:
    print(num2, end=", ", sep=', ')
    num1, num2 = num2, num1 + num2
