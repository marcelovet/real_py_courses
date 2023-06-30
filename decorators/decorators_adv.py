# Fancy Decorators
# So far, you’ve seen how to create simple decorators. You already have a pretty good understanding of what decorators are and how they work. Feel free to take a break from this article to practice everything you’ve learned.
# In the second part of this tutorial, we’ll explore more advanced features, including how to use the following:
# - Decorators on classes
# - Several decorators on one function
# - Decorators with arguments
# - Decorators that can optionally take arguments
# - Stateful decorators
# - Classes as decorators
# Decorating Classes
# There are two different ways you can use decorators on classes.
# The first one is very close to what you have already done with functions:
# you can decorate the methods of a class. This was one of the motivations
# for introducing decorators back in the day.
# Some commonly used decorators that are even built-ins in Python are
# @classmethod, @staticmethod, and @property. The @classmethod and
# @staticmethod decorators are used to define methods inside a class
# namespace that are not connected to a particular instance of that class.
# The @property decorator is used to customize getters and setters for class
# attributes. Expand the box below for an example using these decorators.
# The following definition of a Circle class uses the @classmethod,
# @staticmethod, and @property decorators:
from flask import Flask, abort, request
import functools
import math
from typing import Any

import my_decorators as dc
import pint


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value > 0:
            self._radius = value
        else:
            raise ValueError('Radius must be positive')

    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * (self.radius ** 2)

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535


# In this class:
# - .cylinder_volume() is a regular method.
# - .radius is a mutable property: it can be set to a different value.
# However, by defining a setter method, we can do some error testing to make
# sure it’s not set to a nonsensical negative number. Properties are accessed
# as attributes without parentheses.
# - .area is an immutable property: properties without .setter() methods can’t
# be changed. Even though it is defined as a method, it can be retrieved as an
# attribute without parentheses.
# - .unit_circle() is a class method. It’s not bound to one particular instance
# of Circle. Class methods are often used as factory methods that can create
# specific instances of the class.
# - .pi() is a static method. It’s not really dependent on the Circle
# class, except that it is part of its namespace. Static methods can be called
# on either an instance or the class.
# The Circle class can for example be used as follows:
a_circle = Circle(5)
print(a_circle.radius)
a_circle.radius = 2
print(a_circle.area)
print(a_circle.cylinder_volume(4))
c = Circle.unit_circle()
print(c.radius)
print(c.pi())
print(Circle.pi())

# Let’s define a class where we decorate some of its methods using the
# @debug and @timer decorators from earlier:


class TimeWaster:
    @dc.debug
    def __init__(self, max_num):
        self.max_num = max_num

    @dc.timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i ** 2 for i in range(self.max_num)])


tw = TimeWaster(1000)
tw.waste_time(99)
# The other way to use decorators on classes is to decorate the whole class.
# This is, for example, done in the new dataclasses module in Python 3.7:
# from dataclasses import dataclass
# @dataclass
# class PlayingCard:
#     rank: str
#     suit: str
# The meaning of the syntax is similar to the function decorators.
# In the example above, you could have done the decoration by writing
# PlayingCard = dataclass(PlayingCard).
# A common use of class decorators is to be a simpler alternative to some
# use-cases of metaclasses. In both cases, you are changing the
# definition of a class dynamically.
# Writing a class decorator is very similar to writing a function decorator.
# The only difference is that the decorator will receive a class and not
# a function as an argument. In fact, all the decorators you saw above will
# work as class decorators. When you are using them on a class instead of a
# function, their effect might not be what you want. In the following
# example, the @timer decorator is applied to a class:


@dc.timer
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i ** 2 for i in range(self.max_num)])


tw = TimeWaster(1000)
tw.waste_time(99)
# Decorating a class does not decorate its methods.
# Recall that @timer is just shorthand for TimeWaster = timer(TimeWaster).
# Here, @timer only measures the time it takes to instantiate the class

# Nesting Decorators
# You can apply several decorators to a function by stacking them on top of
# each other:


@dc.debug
@dc.do_twice
def greet(name):
    print(f'Hello {name}')


# Think about this as the decorators being executed in the order they are
# listed. In other words, @debug calls @do_twice, which calls greet(), or
# debug(do_twice(greet())):
greet('Fulano')
# Observe the difference if we change the order of @debug and @do_twice:


@dc.do_twice
@dc.debug
def greet(name):
    print(f'Hello {name}')


greet('Fulano')

# Decorators With Arguments
# Sometimes, it’s useful to pass arguments to your decorators.
# For instance, @do_twice could be extended to a @repeat(num_times) decorator.
# The number of times to execute the decorated function could then be given
# as an argument.
# This would allow you to do something like this:
# @repeat(num_times=4)
# def greet(name):
#     print(f"Hello {name}")
# greet("World")
# Think about how you could achieve this.
# So far, the name written after the @ has referred to a function object that
# can be called with another function. To be consistent, you then need
# repeat(num_times=4) to return a function object that can act as a decorator.
# Luckily, you already know how to return functions! In general, you want
# something like the following:
# def repeat(num_times):
#     def decorator_repeat(func):
#         ...  # Create and return a wrapper function
#     return decorator_repeat
# Typically, the decorator creates and returns an inner wrapper function,
# so writing the example out in full will give you an inner function within
# an inner function. While this might sound like the programming equivalent of
# the Inception movie, we’ll untangle it all in a moment:
# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper_repeat(*args, **kwargs):
#             for _ in range(num_times):
#                 value = func(*args, **kwargs)
#             return value
#         return wrapper_repeat
#     return decorator_repeat
# It looks a little messy, but we have only put the same decorator pattern
# you have seen many times by now inside one additional def that handles the
# arguments to the decorator. Let’s start with the innermost function:
# def wrapper_repeat(*args, **kwargs):
#     for _ in range(num_times):
#         value = func(*args, **kwargs)
#     return value
# This wrapper_repeat() function takes arbitrary arguments and returns the
# value of the decorated function, func(). This wrapper function also contains
# the loop that calls the decorated function num_times times.
# This is no different from the earlier wrapper functions you have seen,
# except that it is using the num_times parameter that must be supplied
# from the outside.
# One step out, you’ll find the decorator function:
# def decorator_repeat(func):
#     @functools.wraps(func)
#     def wrapper_repeat(*args, **kwargs):
#         ...
#     return wrapper_repeat
# Again, decorator_repeat() looks exactly like the decorator functions you
# have written earlier, except that it’s named differently.
# That’s because we reserve the base name—repeat()—for the outermost function,
# which is the one the user will call.
# As you have already seen, the outermost function returns a reference to
# the decorator function:
# def repeat(num_times):
#     def decorator_repeat(func):
#         ...
#     return decorator_repeat
# There are a few subtle things happening in the repeat() function:
# Defining decorator_repeat() as an inner function means that repeat() will
# refer to a function object—decorator_repeat. Earlier, we used repeat without
# parentheses to refer to the function object. The added parentheses are
# necessary when defining decorators that take arguments.
# The num_times argument is seemingly not used in repeat() itself.
# But by passing num_times a closure is created where the value of num_times
# is stored until it will be used later by wrapper_repeat().
# With everything set up, let’s see if the results are as expected:


@dc.repeat(num_times=4)
def greet(name):
    print(f'Hello {name}')


greet('Line')

# Decorator with a default argument that can be called without ()
# With a little bit of care, you can also define decorators that can be used
# both with and without arguments. Most likely, you don’t need this,
# but it is nice to have the flexibility.
# As you saw in the previous section, when a decorator uses arguments, you need
# to add an extra outer function. The challenge is for your code to figure
# out if the decorator has been called with or without arguments.
# Since the function to decorate is only passed in directly if the decorator is
# called without arguments, the function must be an optional argument.
# This means that the decorator arguments must all be specified by keyword.
# You can enforce this with the special * syntax, which means that all
# following parameters are keyword-only:
# def name(_func=None, *, kw1=val1, kw2=val2, ...):  # 1
#     def decorator_name(func):
#         ...  # Create and return a wrapper function.

#     if _func is None:
#         return decorator_name                      # 2
#     else:
#         return decorator_name(_func)               # 3
# Here, the _func argument acts as a marker, noting whether the decorator has
# been called with arguments or not:
# If name has been called without arguments, the decorated function will be
# passed in as _func. If it has been called with arguments, then _func will be
# None, and some of the keyword arguments may have been changed from their
# default values. The * in the argument list means that the remaining arguments
# can’t be called as positional arguments.
# In this case, the decorator was called with arguments.
# Return a decorator function that can read and return a function.
# In this case, the decorator was called without arguments.
# Apply the decorator to the function immediately.
# Using this boilerplate on the @repeat decorator in the previous section,
# you can write the following:
# def repeat(_func=None, *, num_times=2):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper_repeat(*args, **kwargs):
#             for _ in range(num_times):
#                 value = func(*args, **kwargs)
#             return value
#         return wrapper_repeat

#     if _func is None:
#         return decorator_repeat
#     else:
#         return decorator_repeat(_func)
# Compare this with the original @repeat.
# The only changes are the added _func parameter and the if-else at the end.
# Recipe 9.6 of the excellent Python Cookbook shows an alternative solution
# using functools.partial().
# These examples show that @repeat can now be used with or without arguments:
# @repeat
# def say_whee():
#     print("Whee!")

# @repeat(num_times=3)
# def greet(name):
#     print(f"Hello {name}")
# Recall that the default value of num_times is 2:
# >>> say_whee()
# >>> greet("Penny")


@dc.repeat
def say_whee():
    print("Whee!")


@dc.repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")


say_whee()
greet('Alan')

# Stateful Decorators
# Sometimes, it’s useful to have a decorator that can keep track of state.
# As a simple example, we will create a decorator that counts the number of
# times a function is called.
# Note: In the beginning of this guide, we talked about pure functions returning
# a value based on given arguments. Stateful decorators are quite the opposite,
# where the return value will depend on the current state, as well
# as the given arguments.
# In the next section, you will see how to use classes to keep state.
# But in simple cases, you can also get away with using function attributes:
# import functools
# def count_calls(func):
#     @functools.wraps(func)
#     def wrapper_count_calls(*args, **kwargs):
#         wrapper_count_calls.num_calls += 1
#         print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
#         return func(*args, **kwargs)
#     wrapper_count_calls.num_calls = 0
#     return wrapper_count_calls
# @count_calls
# def say_whee():
#     print("Whee!")
# The state—the number of calls to the function—is stored in the function
# attribute .num_calls on the wrapper function.


@dc.repeat
@dc.count_calls
def say_whee():
    print("Whee!")


@dc.repeat(num_times=3)
@dc.count_calls
def greet(name):
    print(f"Hello {name}")


say_whee()
greet('Alan')
greet('Alan')

# Classes as Decorators
# The typical way to maintain state is by using classes.
# In this section, you’ll see how to rewrite the @count_calls example from
# the previous section using a class as a decorator.
# Recall that the decorator syntax @my_decorator is just an easier way
# of saying func = my_decorator(func). Therefore, if my_decorator is a class,
# it needs to take func as an argument in its .__init__() method.
# Furthermore, the class instance needs to be callable so that it can stand
# in for the decorated function.
# For a class instance to be callable, you implement the special
# .__call__() method:
# class Counter:
#     def __init__(self, start=0):
#         self.count = start

#     def __call__(self):
#         self.count += 1
#         print(f"Current count is {self.count}")
# The .__call__() method is executed each time you try to call an instance
# of the class:
# >>> counter = Counter()
# >>> counter()
# Current count is 1
# >>> counter()
# Current count is 2
# >>> counter.count
# 2
# Therefore, a typical implementation of a decorator class needs to implement
# .__init__() and .__call__():


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.num_calls += 1
        print(f'Call {self.num_calls} of {self.func.__name__!r}')
        return self.func(*args, **kwargs)


@CountCalls
def say_haha():
    print('HAHA!')


say_haha()
say_haha()
print(say_haha.num_calls)
# The .__init__() method must store a reference to the function and can do any
# other necessary initialization. The .__call__() method will be called instead
# of the decorated function. It does essentially the same thing as the
# wrapper() function in our earlier examples. Note that you need to use the
# functools.update_wrapper() function instead of @functools.wraps.
# This @CountCalls decorator works the same as the one in the previous section.

# More Real World Examples
# We’ve come a far way now, having figured out how to create all kinds of
# decorators. Let’s wrap it up, putting our newfound knowledge into creating a
# few more examples that might actually be useful in the real world.
# Slowing Down Code, Revisited
# As noted earlier, our previous implementation of @slow_down always sleeps
# for one second. Now you know how to add parameters to decorators, so
# let’s rewrite @slow_down using an optional rate argument that controls how
# long it sleeps:
# import functools
# import time
# def slow_down(_func=None, *, rate=1):
#     """Sleep given amount of seconds before calling the function"""
#     def decorator_slow_down(func):
#         @functools.wraps(func)
#         def wrapper_slow_down(*args, **kwargs):
#             time.sleep(rate)
#             return func(*args, **kwargs)
#         return wrapper_slow_down
#     if _func is None:
#         return decorator_slow_down
#     else:
#         return decorator_slow_down(_func)
# We’re using the boilerplate introduced in the Both Please,
# But Never Mind the Bread section to make @slow_down callable both with and
# without arguments.
# The same recursive countdown() function as earlier now sleeps two seconds
# between each count:


@dc.slow_down(secs=.1)
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(f'Count: {from_number}')
        countdown(from_number - 1)


countdown(3)

# Creating Singletons
# A singleton is a class with only one instance.
# There are several singletons in Python that you use frequently,
# including None, True, and False. It is the fact that None is a singleton that
# allows you to compare for None using the is keyword,
# like you saw in the Both Please section:
# if _func is None:
#     return decorator_name
# else:
#     return decorator_name(_func)
# Using is returns True only for objects that are the exact same instance.
# The following @singleton decorator turns a class into a singleton by storing
# the first instance of the class as an attribute.
# Later attempts at creating an instance simply return the stored instance:


def singleton(cls):
    """Make a class a singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class TheOne:
    pass


# As you see, this class decorator follows the same template as our function
# decorators. The only difference is that we are using cls instead of func
# as the parameter name to indicate that it is meant to be a class decorator.
# Let’s see if it works:
first_one = TheOne()
another_one = TheOne()
print(id(first_one))
print(id(another_one))
print(first_one is another_one)
# It seems clear that first_one is indeed the exact same instance as
# another_one.
# Note: Singleton classes are not really used as often in Python as in
# other languages. The effect of a singleton is usually better implemented as
# a global variable in a module.

# Caching Return Values
# Decorators can provide a nice mechanism for caching and memorization.
# As an example, let’s look at a recursive definition of the Fibonacci
# sequence:


@dc.count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


# While the implementation is simple, its runtime performance is terrible:
print(fibonacci(10))
print(fibonacci.num_calls)

# To calculate the tenth Fibonacci number, you should really only need to
# calculate the preceding Fibonacci numbers, but this implementation somehow
# needs a whopping 177 calculations. It gets worse quickly: 21891 calculations
# are needed for fibonacci(20) and almost 2.7 million calculations for
# the 30th number. This is because the code keeps recalculating Fibonacci
# numbers that are already known.
# The usual solution is to implement Fibonacci numbers using a for
# loop and a lookup table. However, simple caching of the calculations will
# also do the trick:


def cache(func):
    """Keep a cache of previous functions calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache


@cache
@dc.count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(10))
print(fibonacci(8))
print(fibonacci.cache)
# Note that in the final call to fibonacci(8), no new calculations were needed,
# since the eighth Fibonacci number had already been calculated
# for fibonacci(10).
# In the standard library, a Least Recently Used (LRU) cache is available
# as @functools.lru_cache.
# This decorator has more features than the one you saw above.
# You should use @functools.lru_cache instead of writing your own
# cache decorator:


@functools.lru_cache(maxsize=4)
def fibonacci(num):
    print(f'Calculating fibonacci {num}')
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

# The maxsize parameter specifies how many recent calls are cached.
# The default value is 128, but you can specify maxsize=None to cache all
# function calls. However, be aware that this can cause memory problems
# if you are caching many large objects.
# You can use the .cache_info() method to see how the cache performs,
# and you can tune it if needed. In our example, we used an artificially
# small maxsize to see the effect of elements being removed from the cache:


print(fibonacci(10))
print(fibonacci(8))
print(fibonacci(5))
print(fibonacci(8))
print(fibonacci.cache_info())

# Adding Information About Units
# The following example is somewhat similar to the Registering Plugins example
# from earlier, in that it does not really change the behavior of the
# decorated function. Instead, it simply adds unit as a function attribute:


def set_unit(unit):
    """Register a unit on a function"""
    def decorator_set_unit(func):
        func.unit = unit
        return func
    return decorator_set_unit


@set_unit('cm^3')
def volume_of_cylinder(radius, height):
    return math.pi * (radius ** 2) * height


print(
    f'Volume of a cylinder with radius 3 and height 4:',
    f'{volume_of_cylinder(3, 4):.3f} {volume_of_cylinder.unit}'
)

# However, since annotations are used for type hints, it would be hard to
# combine such units as annotations with static type checking.
# Units become even more powerful and fun when connected with a library that
# can convert between units. One such library is pint. With pint
# installed (pip install Pint), you can for instance convert the volume to
# cubic inches or gallons:
ureg = pint.UnitRegistry()
vol = volume_of_cylinder(3, 4) * ureg(volume_of_cylinder.unit)
print(vol)
print(vol.to('cubic inches'))
print(vol.to('gallons').m)

# You could also modify the decorator to return a pint Quantity directly.
# Such a Quantity is made by multiplying a value with the unit.
# In pint, units must be looked up in a UnitRegistry. The registry is stored as
# a function attribute to avoid cluttering the namespace:


def use_unit(unit):
    """Have a function return a Quantity with given unit"""
    use_unit.ureg = pint.UnitRegistry()

    def decorator_use_unit(func):
        @functools.wraps(func)
        def wrapper_use_unit(*args, **kwargs):
            value = func(*args, **kwargs)
            return value * use_unit.ureg(unit)
        return wrapper_use_unit
    return decorator_use_unit


@use_unit('meters per second')
def average_speed(distance, duration):
    return distance / duration


speed_car_ms = average_speed(100, 10)
print(speed_car_ms)
print(speed_car_ms.to('km per hour'))

# Validating JSON
# Let’s look at one last use case.
# Take a quick look at the following Flask route handler:
# @app.route("/grade", methods=["POST"])
# def update_grade():
#     json_data = request.get_json()
#     if "student_id" not in json_data:
#         abort(400)
#     # Update database
#     return "success!"
# Here we ensure that the key student_id is part of the request.
# Although this validation works, it really does not belong in the function
# itself. Plus, perhaps there are other routes that use the exact same
# validation. So, let’s keep it DRY and abstract out any unnecessary
# logic with a decorator. The following @validate_json decorator will do
# the job:

app = Flask(__name__)


def validate_json(*expected_args):
    def decorator_validate_json(func):
        @functools.wraps(func)
        def wrapper_validate_json(*args, **kwargs):
            json_object = request.get_json()
            for expected_arg in expected_args:
                if expected_arg not in json_object:
                    abort(400)
            return func(*args, **kwargs)
        return wrapper_validate_json
    return decorator_validate_json
# In the above code, the decorator takes a variable length list as an argument
# so that we can pass in as many string arguments as necessary, each
# representing a key used to validate the JSON data:
# 1- The list of keys that must be present in the JSON is given as arguments
# to the decorator.
# 2- The wrapper function validates that each expected key is present
# in the JSON data.
# The route handler can then focus on its real job—updating
# grades—as it can safely assume that JSON data are valid:


@app.route("/grade", methods=["POST"])
@validate_json("student_id")
def update_grade():
    json_data = request.get_json()
    # Update database.
    return "success!"
