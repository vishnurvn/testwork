"""
Module for all the custom web-driver exceptions.

"""


class InvalidBrowser(Exception):
    """
    Exception when an invalid browser is specified.

    """

    def __init__(self, message):
        super(InvalidBrowser, self).__init__(message)
