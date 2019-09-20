from functools import wraps


def cache(function):
    cache_dict = {}

    @wraps(function)
    def wrapper(*args, **kwargs):
        if function.__name__ not in cache_dict:
            cache_dict[function.__name__] = function(*args, **kwargs)
        return cache_dict[function.__name__]

    return wrapper
