import re

from source.excpetion import TestCaseFailed
from source.src import driver

STEP_REGEX = r'step_\d+'


class TestCase:

    def _steps(self):
        steps = []
        for name in dir(self):
            if re.match(STEP_REGEX, name):
                steps.append([name, getattr(self, name)])
        return sorted(steps)

    def execute(self):
        for name, step in self._steps():
            try:
                print(f"Executing step {name}")
                step()
            except AssertionError as e:
                raise TestCaseFailed(f"Assertion failed. Test case failed at {name}, exception: {e}")
            except Exception as e:
                driver().quit()
                raise TestCaseFailed(f"Failed at step: {name}, Exception: {type(e)}, {e}")
        driver().quit()
