import os

current_file_path = os.path.dirname(os.path.dirname(__file__))


class Config:
    TEST_CLASS_REGEX = r'^TestCase\w+$'
    TEST_CASE_REGEX = r'test_case_(?P<id>\d+)\.py'
    TEST_DATA_REGEX = r'test_data_(?P<id>\d+)\.py'
    STEP_REGEX = r'step_\d+'
    DESCRIPTION_REGEX = r':description:\s?(?P<content>.*)'
    EXPECTED_REGEX = r':expected:\s?(?P<content>.*)'

    CHROME_DRIVER_LOCATION = os.path.join(current_file_path, 'drivers\\chromedriver.exe')
    IE_DRIVER_LOCATION = os.path.join(current_file_path, 'drivers\\IEDriverServer.exe')
    FIREFOX_DRIVER_LOCATION = os.path.join(current_file_path, 'drivers\\geckodriver.exe')
    EDGE_DRIVER_LOCATION = r'some location'
    TEST_CASE_FOLDER = os.path.join(current_file_path, 'test_cases')

    WEB_DRIVER_WAIT_TIME = 60
    POLL_TIME = 1
    IMPLICIT_WAIT_TIME = 60
    PAGE_LOAD_TIMEOUT = 30
