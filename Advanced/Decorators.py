# Higher Order functions are functions that accepts a function as a parameter or returns function


# Decorators can be defined by accepting a function, having a wrapper function then returning the same function as below.
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('******************')
        func(*args, **kwargs)
        print('******************')
    return wrap_func


@my_decorator
def hello(name, emoji=':)'):
    print(f'Hello {name} {emoji}')


hello('Gayathri')
hello(name='Chrissy', emoji=';)')
