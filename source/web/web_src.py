"""
Module for web driver related functions.

"""

from selenium import webdriver

from config import Config
from source.excpetion import InvalidBrowser
from source.system_config import Config as SysConfig
from source.utils import cache


@cache
def driver() -> webdriver.Remote:
    """
    Function for launching the browser according to the config specified in the config.py file.
    Supports drivers of chrome, internet explorer, firefox and edge. Throws InvalidBrowser exception if an invalid
    browser is specified in the config file.

    Returns
    -------
    driver: webdriver
        Returns a webdriver object according to the configurations in the config file.

    """
    if Config.BROWSER == 'chrome':
        driver_object = webdriver.Chrome(SysConfig.CHROME_DRIVER_LOCATION)
    elif Config.BROWSER == 'ie':
        driver_object = webdriver.Ie(SysConfig.IE_DRIVER_LOCATION)
    elif Config.BROWSER == 'firefox':
        driver_object = webdriver.Firefox(executable_path=SysConfig.FIREFOX_DRIVER_LOCATION)
    elif Config.BROWSER == 'edge':
        driver_object = webdriver.Edge(SysConfig.EDGE_DRIVER_LOCATION)
    else:
        raise InvalidBrowser(f'{Config.BROWSER} is not a valid browser. Please provide a valid '
                             f'browser name')
    driver_object.maximize_window()
    driver_object.set_page_load_timeout(SysConfig.PAGE_LOAD_TIMEOUT)
    driver_object.implicitly_wait(SysConfig.IMPLICIT_WAIT_TIME)
    return driver_object
