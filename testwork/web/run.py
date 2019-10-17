import importlib
import os
import re

from source import driver
from source.system_config import SystemConfig
from source.test_case_src import TestCaseFailed


def run_test_suite():
    pass


def run_test_case(test_case: str, runs: [list, str]) -> None:
    try:
        module_name = os.path.basename(test_case).split('.')[0]
        module = importlib.import_module('.{}'.format(module_name), 'test_cases.web')
        test_case_class = [cls for cls in dir(module) if re.match(SystemConfig.TEST_CLASS_REGEX, cls) is not None][0]
        if isinstance(runs, str):
            getattr(module, test_case_class)().execute(runs)
        elif isinstance(runs, list):
            for run in runs:
                getattr(module, test_case_class)().execute(run)
        driver().quit()
    except TestCaseFailed:
        driver().quit()


if __name__ == '__main__':
    run_test_case('test_case_1.py', 'run_1')
