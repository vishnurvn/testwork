import unittest

from selenium.webdriver import Remote

from web import driver


class TestWebDriver(unittest.TestCase):
    def test_driver(self):
        driver_object = driver()
        self.assertIsInstance(driver_object, Remote)
        driver_object.quit()


if __name__ == '__main__':
    unittest.main()
