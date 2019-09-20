from selenium import webdriver

from config import Config
from source.excpetion import InvalidBrowser
from source.utils import cache


@cache
def driver():
    if Config.BROWSER == 'chrome':
        driver_object = webdriver.Chrome(Config.CHROME_DRIVER_LOCATION)
    elif Config.BROWSER == 'ie':
        driver_object = webdriver.Ie(Config.IE_DRIVER_LOCATION)
    elif Config.BROWSER == 'firefox':
        driver_object = webdriver.Firefox(Config.FIREFOX_DRIVER_LOCATION)
    elif Config.BROWSER == 'edge':
        driver_object = webdriver.Edge(Config.EDGE_DRIVER_LOCATION)
    else:
        raise InvalidBrowser(f'{Config.BROWSER} is not a valid browser. Please provide a valid '
                                      f'browser name')
    return driver_object
