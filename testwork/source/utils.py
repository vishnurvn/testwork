"""
Module for utilities.

"""

from functools import wraps

import yaml


def cache(function):
    # TODO write tests
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


@cache
def yaml_config(yaml_file: str) -> dict:
    """
    Converts a yaml file into a config - a dictionary object. The function takes the yaml file, safe loads it using
    PyYaml package and returns a dict object.

    Parameters
    ----------
    yaml_file: string
        Path to the config yaml file

    Returns
    -------
    config: dict
        Returns the yaml config as a dict

    """
    with open(yaml_file) as file:
        config = yaml.safe_load(file)
    return config
