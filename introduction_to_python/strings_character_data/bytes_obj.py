# A bytes object is an immutable sequence of single byte values. Each element
# in a bytes object is a small integer in the range of 0 to 255.
# only ASCII characters are allowed
a = b'spam egg bacon'
print(type(a))
print(a)
print(a[1])
a = rb'spam \negg bacon'
print(a)
a = b'spam \negg bacon'
print(a)
a = bytes('spam eggs', 'utf-8')
print(a)
print(list(a))
# creates 8 null bytes values
a = bytes(8)
print(a)
a = bytes([115, 112, 97, 109])
print(a)

# operations on bytes objects
print(b'a' in a)
print(b'b' in a)
print(b'aaaa' + a)
print(a * 3)
print(len(a))
print(max(a))
print(chr(max(a)))
print(a.count(b'sp'))
print(a.startswith(b'sp'))
print(a.endswith(b'am'))
a += b','
a *= 5
print(a)
print(a.split(b','))
print(a.center(40, b'-'))
print(hex(a[0]))
b = bytes.fromhex(' aa 68 32 af ')
print(b)
print(b.hex())

# bytearray
# bytearray are mutable
ba = bytearray('spam, egg, bacon', 'utf8')
print(ba, type(ba))
ba = bytearray([97, 98, 99, 100, 101])
print(ba)
ba[4] = 0xee
print(ba)
ba[:3] = b'egg'
print(ba)
