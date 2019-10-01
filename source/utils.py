"""
Module for utilities.

"""

from functools import wraps


def cache(function):
    """
    Function to cache function returns. If the function is not executed, the result is stored in a cache dictionary.
    If the function is already executed and is stored in the cache dictionary, it is returned.

    Parameters
    ----------
    function
        The function to be cached

    Returns
    -------
    function
        The result of the function

    """
    cache_dict = {}

    @wraps(function)
    def wrapper(*args, **kwargs):
        if function.__name__ not in cache_dict:
            cache_dict[function.__name__] = function(*args, **kwargs)
        return cache_dict[function.__name__]

    return wrapper
