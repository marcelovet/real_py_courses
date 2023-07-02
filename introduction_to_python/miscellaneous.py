# https://realpython.com/lessons/functions-miscellaneous/
# exec allows execution of a python code

job = 'print("hello")'
exec(job)

# eval works similarlly and you can define the locals available
# to make it safer
to_eval = input('make some math: ')
print(eval(to_eval, {'pow': pow}))

# hash can be used to compare the contents of two objects
# if they compare to equal, they must have the same hash value
