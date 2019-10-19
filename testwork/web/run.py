import importlib
import re

from source.system_config import SystemConfig
from source.test_case_src import TestCaseFailed
from web.web_src import driver


def run_test_suite():
    pass


def run_web_test_case(test_case: str, runs: [list, str]) -> None:
    try:
        module = importlib.import_module('.{}'.format(test_case), 'test_cases.web')
        test_case_class = [cls for cls in dir(module) if re.match(SystemConfig.TEST_CLASS_REGEX, cls) is not None][0]
        if isinstance(runs, str):
            getattr(module, test_case_class)().execute(runs)
        elif isinstance(runs, list):
            for run in runs:
                getattr(module, test_case_class)().execute(run)
        driver().quit()
    except TestCaseFailed:
        driver().quit()
