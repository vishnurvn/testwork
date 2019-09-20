class InvalidBrowser(Exception):
    def __init__(self, message):
        super(InvalidBrowser, self).__init__(message)


class TestCaseFailed(Exception):
    def __init__(self, message, driver):
        super(TestCaseFailed, self).__init__(message)
        driver().quit()
