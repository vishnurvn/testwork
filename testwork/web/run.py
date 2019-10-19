from source.test_case_src import TestCase
from source.test_case_src import TestCaseFailed
from web.web_src import driver


def run_test_suite():
    pass


def run_web_test_case(test_case: str, runs: [list, str]) -> None:
    try:
        if isinstance(runs, str):
            TestCase(test_case, 'web').execute(runs)
        elif isinstance(runs, list):
            for run in runs:
                TestCase(test_case, 'web').execute(run)
        driver().quit()
    except TestCaseFailed:
        driver().quit()
