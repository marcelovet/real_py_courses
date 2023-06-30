# By definition, a decorator is a function that takes another function and
# extends the behavior of the latter function without explicitly modifying it.
# Functions
# Before you can understand decorators, you must first understand how functions
# work. For our purposes, a function returns a value based on the given
# arguments. Here is a very simple example:
# these imports below were automatically updated to this place by vscode
import functools
import math
import random
from datetime import datetime

import my_decorators as dc
from flask import Flask, g, redirect, request, url_for
from my_decorators import do_twice


def add_one(number):
    return number + 1


print(add_one(2))
# In general, functions in Python may also have side effects rather than just
# turning an input into an output. The print() function is a basic example of
# this: it returns None while having the side effect of outputting something to
# the console. However, to understand decorators, it is enough to think about
# functions as something that turns given arguments into a value.
# Note: In functional programming, you work (almost) only with pure functions
# without side effects. While not a purely functional language, Python supports
# many of the functional programming concepts, including functions as first-class
# objects.
# First-Class Objects
# In Python, functions are first-class objects. This means that functions can be
# passed around and used as arguments, just like any other object (string, int,
# float, list, and so on). Consider the following three functions:


def say_hello(name):
    return f'Hello {name}'


def be_awesome(name):
    return f'Yo {name}, together we are the awesomest!'


def greet_bob(greeter_func):
    return greeter_func('Bob')


# Here, say_hello() and be_awesome() are regular functions that expect a name
# given as a string. The greet_bob() function however, expects a function as its
# argument. We can, for instance, pass it the say_hello() or the be_awesome()
# function:
print(greet_bob(say_hello))
print(greet_bob(be_awesome))
# Note that greet_bob(say_hello) refers to two functions, but in different ways:
# greet_bob() and say_hello. The say_hello function is named without parentheses.
# This means that only a reference to the function is passed. The function is not
# executed. The greet_bob() function, on the other hand, is written with
# parentheses, so it will be called as usual.
# Inner Functions
# It’s possible to define functions inside other functions. Such functions are
# called inner functions. Here’s an example of a function with two inner
# functions:


def parent():
    print('Printing from the parent() function')

    def first_child():
        print('Printing from the first_child() function')

    def second_child():
        print('Printing from the second_child() function')

    second_child()
    first_child()


parent()
# Note that the order in which the inner functions are defined does not matter.
# Like with any other functions, the printing only happens when the inner
# functions are executed.
# Furthermore, the inner functions are not defined until the parent function is
# called. They are locally scoped to parent(): they only exist inside the
# parent() function as local variables. Try calling first_child(). You should get
# an error:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'first_child' is not defined
# Returning Functions From Functions
# Python also allows you to use functions as return values.
# The following example returns one of the inner functions from the outer
# parent() function:


def parent(num):
    def first_child():
        return 'Hi, I am Emma.'

    def second_child():
        return 'Call me Liam.'
    if num == 1:
        return first_child
    else:
        return second_child


# Note that you are returning first_child without the parentheses.
# Recall that this means that you are returning a reference to the
# function first_child. In contrast first_child() with parentheses refers to
# the result of evaluating the function. This can be seen in the
# following example:
first = parent(1)
second = parent(2)
print(first)
print(second)
# The somewhat cryptic output simply means that the first variable refers to the
# local first_child() function inside of parent(), while second points
# to second_child().
# You can now use first and second as if they are regular functions, even
# though the functions they point to can’t be accessed directly:
print(first())
print(second())
# Finally, note that in the earlier example you executed the inner functions
# within the parent function, for instance first_child(). However, in this last
# example, you did not add parentheses to the inner functions—first_child—upon
# returning. That way, you got a reference to each function that you could
# call in the future.
# Simple Decorators
# Now that you’ve seen that functions are just like any other object in Python,
# you’re ready to move on and see the magical beast that is the Python decorator.
# Let’s start with an example:


def my_decorator(func):
    def wrapper():
        print('Something is happening before the function is called')
        func()
        print('Something is happening after the function is called')
    return wrapper


def say_whee():
    print('Whee!')


say_whee = my_decorator(say_whee)
say_whee()
# The so-called decoration happens at the following line:
# say_whee = my_decorator(say_whee)
# In effect, the name say_whee now points to the wrapper() inner function.
# Remember that you return wrapper as a function when you call
# my_decorator(say_whee):
print(say_whee)
# However, wrapper() has a reference to the original say_whee() as func, and
# calls that function between the two calls to print().
# Put simply: decorators wrap a function, modifying its behavior.
# Before moving on, let’s have a look at a second example. Because
# wrapper() is a regular Python function, the way a decorator modifies a function
# can change dynamically. So as not to disturb your neighbors, the following
# example will only run the decorated code during the day:


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            print(f'Now it is {datetime.now().hour}')
            func()
        else:
            print(
                f'Now it is {datetime.now().hour}.',
                'Hush, the neighbors are asleep'
            )
            pass
    return wrapper


def say_whee():
    print('Whee!')


say_whee = not_during_the_night(say_whee)
say_whee()
# Syntactic Sugar!
# The way you decorated say_whee() above is a little clunky. First of all, you
# end up typing the name say_whee three times. In addition, the decoration gets
# a bit hidden away below the definition of the function.
# Instead, Python allows you to use decorators in a simpler way with the @
# symbol, sometimes called the “pie” syntax. The following example does the exact
# same thing as the first decorator example:


def my_decorator(func):
    def wrapper():
        print('Something is happening before the function is called')
        func()
        print('Something is happening after the function is called')
    return wrapper


@my_decorator
def say_woaa():
    print('Woaa!')


say_woaa()
# Reusing Decorators
# Recall that a decorator is just a regular Python function. All the usual tools
# for easy reusability are available. Let’s move the decorator to its own module
# that can be used in many other functions.
# Create a file called my_decorators.py with the following content:
# def do_twice(func):
# def wrapper_do_twice():
#     func()
#     func()
# return wrapper_do_twice


@do_twice
def say_hey():
    print('Hey!')


say_hey()
# Decorating Functions With Arguments
# Say that you have a function that accepts some arguments. Can you still
# decorate it? Let’s try:
# @do_twice
# def greet(name):
#     print('Hello {name}')
# greet('World')
# Traceback (most recent call last):
#   File "c:\Users\marce\Documents\python\real_python\decorators.py", line 230,
#   in <module>
#     greet('World')
# TypeError: do_twice.<locals>.wrapper_do_twice() takes 0 positional arguments
# but 1 was given
# The problem is that the inner function wrapper_do_twice() does not take any
# arguments, but name="World" was passed to it. You could fix this by letting
# wrapper_do_twice() accept one argument, but then it would not work for the
# say_whee() function you created earlier.
# The solution is to use *args and **kwargs in the inner wrapper function.
# Then it will accept an arbitrary number of positional and keyword arguments.
# Rewrite decorators.py as follows:
# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return wrapper_do_twice
# The wrapper_do_twice() inner function now accepts any number of arguments
# and passes them on to the function it decorates. Now both your say_whee() and
# greet() examples works:


@do_twice
def greet(name):
    print(f'Hello {name}!')


greet('World')
# Returning Values From Decorated Functions
# What happens to the return value of decorated functions? Well, that’s up to
# the decorator to decide. Let’s say you decorate a simple function as follows:
# from decorators import do_twice
# @do_twice
# def return_greeting(name):
#     print("Creating greeting")
#     return f"Hi {name}"
# >>> hi_adam = return_greeting("Adam")
# Creating greeting
# Creating greeting
# >>> print(hi_adam)
# None
# Oops, your decorator ate the return value from the function.
# Because the do_twice_wrapper() doesn’t explicitly return a value, the call
# return_greeting("Adam") ended up returning None.
# To fix this, you need to make sure the wrapper function returns the return
# value of the decorated function. Change your decorators.py file:
# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper_do_twice


@do_twice
def return_greeting(name):
    print('Creating greeting')
    return f'Hi {name}'


print(return_greeting('Adam'))

# Who Are You, Really?
# A great convenience when working with Python, especially in the interactive
# shell, is its powerful introspection ability. Introspection is the ability of
# an object to know about its own attributes at runtime. For instance, a
# function knows its own name and documentation:
print(print)
print(print.__name__)
# help(print)
# The introspection works for functions you define yourself as well:
print(say_hey)
print(say_hey.__name__)
# However, after being decorated, say_hey() has gotten very confused about its
# identity. It now reports being the wrapper_do_twice() inner function inside
# the do_twice() decorator. Although technically true, this is not very useful
# information.
# To fix this, decorators should use the @functools.wraps decorator, which will
# preserve information about the original function. Update decorators.py again:
# Technical Detail: The @functools.wraps decorator uses the function
# functools.update_wrapper() to update special attributes like
# __name__ and __doc__ that are used in the introspection.
# A Few Real World Examples
# Let’s look at a few more useful examples of decorators.
# You’ll notice that they’ll mainly follow the same pattern
# that you’ve learned so far:
# import functools
# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator
# Timing Functions
# Let’s start by creating a @timer decorator. It will measure the time a
# function takes to execute and print the duration to the console.
# Here’s the code:
# import functools
# import time
# def timer(func):
#     """Print the runtime of the decorated function"""
#     @functools.wraps(func)
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter()    # 1
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()      # 2
#         run_time = end_time - start_time    # 3
#         print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
#         return value
#     return wrapper_timer
# @timer
# def waste_some_time(num_times):
#     for _ in range(num_times):
#         sum([i**2 for i in range(10000)])


@dc.timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i ** 2 for i in range(10000)])


waste_some_time(1)
waste_some_time(100)
# This decorator works by storing the time just before the function starts
# running (at the line marked # 1) and just after the function finishes
# (at # 2). The time the function takes is then the difference between the two
# (at # 3). We use the time.perf_counter() function, which does a good job of
# measuring time intervals.
# Note: The @timer decorator is great if you just want to get an idea about the
# runtime of your functions. If you want to do more precise measurements of
# code, you should instead consider the timeit module in the standard library.
# It temporarily disables garbage collection and runs multiple trials to strip
# out noise from quick function calls.

# Debugging Code
# The following @debug decorator will print the arguments a function is
# called with as well as its return value every time the function is called:
# import functools

# def debug(func):
#     """Print the function signature and return value"""
#     @functools.wraps(func)
#     def wrapper_debug(*args, **kwargs):
#         args_repr = [repr(a) for a in args]                      # 1
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
#         signature = ", ".join(args_repr + kwargs_repr)           # 3
#         print(f"Calling {func.__name__}({signature})")
#         value = func(*args, **kwargs)
#         print(f"{func.__name__!r} returned {value!r}")           # 4
#         return value
#     return wrapper_debug
# The signature is created by joining the string representations of all the
# arguments. The numbers in the following list correspond to the numbered
# comments in the code:
# 1. Create a list of the positional arguments. Use repr() to get a nice string
# representing each argument.
# 2. Create a list of the keyword arguments. The f-string formats each argument
# as key=value where the !r specifier means that repr() is used to represent
# the value.
# 3. The lists of positional and keyword arguments is joined together to one
# signature string with each argument separated by a comma.
# 4. The return value is printed after the function is executed.
# Let’s see how the decorator works in practice by applying it to a simple
# function with one position and one keyword argument:


@dc.debug
def make_greeting(name, age=None):
    if age is None:
        return f'Howdy {name}!'
    else:
        return f'Whoa {name}! {age} already, you are growing up!'


make_greeting('Ze')
make_greeting('Ze', 91)
make_greeting(name='Ze', age=91)

# This example might not seem immediately useful since the @debug decorator just
# repeats what you just wrote. It’s more powerful when applied to small
# convenience functions that you don’t call directly yourself.
# The following example calculates an approximation to the mathematical
# constant e:

math.factorial = dc.debug(math.factorial)


def aproximate_e(terms=18):
    return sum([1 / math.factorial(n) for n in range(terms)])


print(aproximate_e(10))
# This example also shows how you can apply a decorator to a function that has
# already been defined. The approximation of e is based on the series
# expansion defined like aproximate_e() where terms=infinity.
# When calling the approximate_e() function, you can see the @debug decorator
# at work
# Slowing Down Code
# This next example might not seem very useful. Why would you want to slow down
# your Python code? Probably the most common use case is that you want to
# rate-limit a function that continuously checks whether a resource—like a
# web page—has changed. The @slow_down decorator will sleep one second before it
# calls the decorated function:
# import functools
# import time
# def slow_down(func):
#     """Sleep 1 second before calling the function"""
#     @functools.wraps(func)
#     def wrapper_slow_down(*args, **kwargs):
#         time.sleep(1)
#         return func(*args, **kwargs)
#     return wrapper_slow_down
# @slow_down
# def countdown(from_number):
#     if from_number < 1:
#         print("Liftoff!")
#     else:
#         print(from_number)
#         countdown(from_number - 1)


@dc.slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff")
    else:
        print(from_number)
        countdown(from_number - 1)


countdown(4)
# Note: The countdown() function is a recursive function.
# In other words, it’s a function calling itself. To learn more about recursive
# functions in Python, see the guide on
# https://realpython.com/python-thinking-recursively/
# The @slow_down decorator always sleeps for one second.
# Later, you’ll see how to control the rate by passing an argument to the
# decorator.
# Registering Plugins
# Decorators don’t have to wrap the function they’re decorating.
# They can also simply register that a function exists and return it unwrapped.
# This can be used, for instance, to create a light-weight plug-in
# architecture:
# import random
PLUGINS = dict()


def register(func):
    """Register a function as a plug-in

    Args:
        func (function): function to be registered as plug-in
    """
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name):
    return f'Hello {name}'


@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f'Using {greeter!r}')
    return greeter_func(name)


# The @register decorator simply stores a reference to the decorated function
# in the global PLUGINS dict. Note that you do not have to write an inner
# function or use @functools.wraps in this example because you are returning
# the original function unmodified.
# The randomly_greet() function randomly chooses one of the registered
# functions to use. Note that the PLUGINS dictionary already contains references
# to each function object that is registered as a plugin:
print(PLUGINS)
print(randomly_greet('Line'))
# The main benefit of this simple plugin architecture is that you do not
# need to maintain a list of which plugins exist. That list is created when
# the plugins register themselves. This makes it trivial to add a new plugin:
# just define the function and decorate it with @register.
# If you are familiar with globals() in Python, you might see some similarities
# to how the plugin architecture works. globals() gives access to all global
# variables in the current scope, including your plugins:
print(globals())
# Using the @register decorator, you can create your own curated list of
# interesting variables, effectively hand-picking some functions from globals()

# Is the User Logged In?
# The final example before moving on to some fancier decorators is commonly
# used when working with a web framework. In this example, we are using Flask
# to set up a /secret web page that should only be visible to users that are
# logged in or otherwise authenticated:
# from flask import Flask, g, request, redirect, url_for
app = Flask(__name__)


def login_required(func):
    """Make sure user is logged in before proceeding

    Args:
        func (function): a _description_
    """
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required


@app.route('/secret')
@login_required
def secret():
    ...
# While this gives an idea about how to add authentication to your web
# framework, you should usually not write these types of decorators yourself.
# For Flask, you can use the Flask-Login extension instead, which adds more
# security and functionality.
