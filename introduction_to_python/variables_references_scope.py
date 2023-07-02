# variables, references and scope
# https://realpython.com/lessons/functions-variables-references-and-scope-part-1/
# https://realpython.com/lessons/functions-variables-references-and-scope-part-2/
# dir allows to see all methods from a object
print(dir('string'))

# scope
a = 1
b = 'global'
c = 'another global'


def function():
    a = 2
    b = 'local'
    print(a, b)
    print(
        'vars() shows the variables available in local scope',
        'which is similar to locals() when no argument is defined'
    )
    print(vars(), locals())
    # print(globals())
    print(
        'if you use a variable not defined in the local scope',
        'python will seek for it in the scope above until it hits the global',
        'scope and, if no variable named is find then raise an error'
    )
    print(f'A global variable called in the local scope: {c}')


print(a, b)
function()
print(a, b)
