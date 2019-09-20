import os
import unittest

from config import Config


class ConfigTests(unittest.TestCase):
    def test_browser_location(self):
        chrome_file_name = os.path.basename(Config.CHROME_DRIVER_LOCATION)
        ie_file_name = os.path.basename(Config.IE_DRIVER_LOCATION)
        self.assertEqual(chrome_file_name, 'chromedriver.exe')
        self.assertEqual(ie_file_name, 'IEDriverServer.exe')
