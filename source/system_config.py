import os

from source.utils import yaml_config

current_file_path = os.path.dirname(os.path.dirname(__file__))
user_config = yaml_config(os.path.join(current_file_path, 'config.yaml'))


class Config:
    STEP_REGEX = r'step_\d+'
    TEST_CLASS_REGEX = r'^TestCase\d+$'
    TEST_CASE_REGEX = r'test_case_(?P<id>\d+)\.py'
    TEST_DATA_REGEX = r'test_data_(?P<id>\d+)\.py'
    DESCRIPTOR_REGEX = {
        value: r':{}:\s?(?P<content>.*)'.format(descriptor) for
        descriptor, value in user_config['test_case']['step_descriptors'].items()
    }

    CHROME_DRIVER_LOCATION = os.path.join(current_file_path, 'drivers\\chromedriver.exe')
    IE_DRIVER_LOCATION = os.path.join(current_file_path, 'drivers\\IEDriverServer.exe')
    FIREFOX_DRIVER_LOCATION = os.path.join(current_file_path, 'drivers\\geckodriver.exe')
    EDGE_DRIVER_LOCATION = r'some location'
    TEST_CASE_FOLDER = os.path.join(current_file_path, 'test_cases')
    REPORT_FOLDER = os.path.join(current_file_path, 'reports')

    WEB_DRIVER_WAIT_TIME = 60
    POLL_TIME = 1
    IMPLICIT_WAIT_TIME = 60
    PAGE_LOAD_TIMEOUT = 30


if __name__ == '__main__':
    print(Config.DESCRIPTOR_REGEX.items())
