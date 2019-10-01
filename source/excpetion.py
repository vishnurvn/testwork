"""
Module for all the custom exceptions.

"""


class InvalidBrowser(Exception):
    """
    Exception when an invalid browser is specified.

    """
    def __init__(self, message):
        super(InvalidBrowser, self).__init__(message)


class TestCaseFailed(Exception):
    """
    Exception raised to notify that the test has failed with message

    """
    def __init__(self, message):
        super(TestCaseFailed, self).__init__(message)
