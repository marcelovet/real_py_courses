# https://realpython.com/lessons/strings/
# https://realpython.com/lessons/escape-sequences/
# https://realpython.com/lessons/raw-strings/
# https://realpython.com/lessons/triple-quoted-strings/
# string
# sequence of zero or more characters enclosed by ' or "
print(type('asda'))
print(type(""))
a = 'hello world'
b = "I wasn't at school today"
c = f'{a}, {b}'
print(c)

b = "He said \"I wasn't at school today\" to me"
print(b)
d = "This is line 1.\nThis is line 2."
print(d)
e = "One\tTwo\tThree\tFour"
print(e)
# Escape characters
# \' - single quote
# \" - double quote
# \\ - backslash
# \n - newline
# \r - carriege return
# \t - tab
# \b - backspace
# \f - form feed
# \v - vertical tab
# \onn - character with octal value xx
# \xnn - character with hex value nn
raw_character = r"one\ntwo"
print(raw_character)
# raw strings are useful when you have to use some logic in the data
# as when working with regular expression
print("""This is a triple quoted string.
It lets you use any kind of quote inside like " or '.
And also, you can make multiple line strings""")
# but the main use of triple quote is docstring


def foo(val):
    """Takes a value and print a msg"""
    print(f"{val} is a nice value")
    return


foo(1)
