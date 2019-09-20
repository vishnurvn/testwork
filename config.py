import os

current_file_path = os.path.dirname(__file__)


class Config:
    CHROME_DRIVER_LOCATION = os.path.join(current_file_path, 'drivers\\chromedriver.exe')
    IE_DRIVER_LOCATION = os.path.join(current_file_path, 'drivers\\IEDriverServer.exe')
    FIREFOX_DRIVER_LOCATION = r'some location'
    EDGE_DRIVER_LOCATION = r'some location'
    WEB_DRIVER_WAIT_TIME = 60
    POLL_TIME = 1
    IMPLICIT_WAIT_TIME = 60

    BROWSER = 'chrome'
