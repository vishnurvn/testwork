import importlib
import os
import re

from testwork import SystemConfig

exec_dir = os.getcwd()


def get_test_case_list(type_):
    web_test_cases = os.path.join(exec_dir, f"test_cases\\{type_}")
    test_case_list = []
    for file_name in os.listdir(web_test_cases):
        if re.match(SystemConfig.TEST_CASE_REGEX, file_name):
            test_case_list.append(file_name)
    return test_case_list


def get_test_class(test_case_py_file, type_):
    module_name = test_case_py_file.split('.')[0]
    module = importlib.import_module(f".{module_name}", f"test_cases.{type_}")
    test_case_class = [cls for cls in dir(module) if
                       re.match(SystemConfig.TEST_CLASS_REGEX, cls) is not None][0]
    return getattr(module, test_case_class)


for item_name in get_test_case_list('web'):
    print(get_test_class(item_name, 'web')().__description__)
