import inspect
import re
from configparser import ConfigParser

from source.excpetion import TestCaseFailed
from source.web_src import driver

STEP_REGEX = r'step_\d+'


class TestCase:

    def _steps(self):
        steps = []
        for name in dir(self):
            if re.match(STEP_REGEX, name):
                steps.append([name, getattr(self, name)])
        return sorted(steps)

    def execute_batch(self, test_data, run):
        for name, step in self._steps():
            arguments = inspect.signature(step).parameters
            try:
                kwargs = dict([(arg, test_data.get_data(run, arg)) for arg in arguments])
                step(**kwargs)
            except KeyError:
                print("Test case failed")
                print(f"Skipping run: {run}, arguments not found in the test data: {[arg for arg in arguments]}")
                break
            except AssertionError as e:
                raise TestCaseFailed(f"Assertion failed. Test case failed at {name}, exception: {e}")
            except Exception as e:
                raise TestCaseFailed(f"Failed at step: {name}, Exception: {type(e)}, {e}")

    def execute(self, test_data, run):
        self.execute_batch(test_data, run)
        driver().quit()


class TestData:
    def __init__(self, filename):
        self.config = ConfigParser()
        self.config.read(filename)

    def runs(self):
        return self.config.sections()

    def get_data(self, run, argument):
        return self.config[run][argument]
