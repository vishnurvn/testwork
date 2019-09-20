import re

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
            except Exception as e:
                print(f"Failed at step: {name}, Exception: {type(e)}, {e}")
