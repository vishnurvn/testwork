import importlib
import os
import re

from source import driver
from source.test_case_src import TestData

FILE_REGEX = r'^[a-zA-Z].*\.py$'
TEST_CLASS_REGEX = r'^TestCase\w+$'

test_data_path = os.path.join(os.path.dirname(__file__), 'test_data/web')
test_data_files = os.listdir(test_data_path)

for file in os.listdir(os.path.join(os.path.dirname(__file__), 'test_cases/web')):
    try:
        if re.match(FILE_REGEX, file):
            module_name = file.split('.')[0]
            test_data = TestData(os.path.join(test_data_path, '{}.data'.format(module_name)))
            module = importlib.import_module('.{}'.format(module_name), 'test_cases.web')
            test_case_class = [cls for cls in dir(module) if re.match(TEST_CLASS_REGEX, cls) is not None][0]
            for run in test_data.runs():
                getattr(module, test_case_class)().execute(test_data, run)
                print('Test case successfully ran')
    except FileNotFoundError:
        print('Test data for the test case does not exist')
    finally:
        driver().quit()
