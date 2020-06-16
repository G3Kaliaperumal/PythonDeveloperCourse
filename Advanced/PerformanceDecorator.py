from time import time


def performance(func):
    def wrap_func(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f'Time taken: {end_time - start_time}s')
        return result
    return wrap_func


@performance
def test_function():
    for i in range(1, 100000):
        i*5


test_function()
