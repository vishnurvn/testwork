import os
import unittest

from source.system_config import Config


class ConfigTests(unittest.TestCase):
    def test_browser_location(self):
        drivers_location = os.listdir(os.path.dirname(Config.CHROME_DRIVER_LOCATION))
        driver_list = ['chromedriver.exe', 'geckodriver.exe', 'IEDriverServer.exe']
        self.assertListEqual(drivers_location, driver_list)
