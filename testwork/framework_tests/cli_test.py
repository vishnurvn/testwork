import os
import subprocess
import unittest

import testwork


class TestCLI(unittest.TestCase):

    def setUp(self) -> None:
        path = r'C:\Users\Vishnu\Documents\test_work_project'
        test_location = os.fspath(path)
        os.chdir(test_location)
        self.app = os.path.join(os.path.dirname(testwork.__file__), 'app.py')

    def test_start(self) -> None:
        subprocess.run([self.app, 'start'])

    def test_create_test_case_web(self) -> None:
        pass
