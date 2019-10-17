import os

from source.utils import yaml_config

current_file_path = os.path.dirname(os.path.dirname(__file__))
user_config = yaml_config(os.path.join(os.getcwd(), 'config.yaml'))


class SystemConfig:
    STEP_REGEX = r'step_\d+'
    TEST_CLASS_REGEX = r'^TestCase\d+$'
    TEST_CASE_REGEX = r'test_case_(?P<id>\d+)\.py'
    TEST_DATA_REGEX = r'test_data_(?P<id>\d+)\.py'
    DESCRIPTOR_REGEX = {
        value: r':{}:\s?(?P<content>.*)'.format(descriptor) for
        descriptor, value in user_config['test_case']['step_descriptors'].items()
    }

    TEST_CASE_FOLDER = os.path.join(current_file_path, 'test_cases')
    REPORT_FOLDER = os.path.join(current_file_path, 'reports')
