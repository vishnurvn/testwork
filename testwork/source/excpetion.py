"""
Module for all the custom exceptions.

"""


class TestCaseFailed(Exception):
    """
    Exception raised to notify that the test has failed with message

    """

    def __init__(self, message):
        super(TestCaseFailed, self).__init__(message)
