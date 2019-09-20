class InvalidBrowserException(Exception):
    def __init__(self, message):
        super(InvalidBrowserException, self).__init__(message)
