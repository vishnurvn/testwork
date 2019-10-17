"""
Module for web driver related functions.

"""
import os

from selenium import webdriver

from source.system_config import user_config, current_file_path
from source.utils import cache
from web.exception import InvalidBrowser


@cache
def driver() -> webdriver.Remote:
    """
    Function for launching the browser according to the config specified in the config.yaml file.
    Supports drivers of chrome, internet explorer, firefox and edge. Throws InvalidBrowser exception if an invalid
    browser is specified in the config file.

    Returns
    -------
    driver: webdriver
        Returns a webdriver object according to the configurations in the config file.

    """

    def get_path(path):
        return os.path.join(current_file_path, path)

    if user_config["web"]["browser"] == 'chrome':
        driver_object = webdriver.Chrome(get_path(user_config['web']['chrome_path']))
    elif user_config["web"]["browser"] == 'ie':
        driver_object = webdriver.Ie(get_path(user_config['web']['ie_path']))
    elif user_config["web"]["browser"] == 'firefox':
        driver_object = webdriver.Firefox(executable_path=get_path(user_config['web']['firefox_path']))
    elif user_config["web"]["browser"] == 'edge':
        driver_object = webdriver.Edge(get_path(user_config['web']['edge_path']))
    else:
        raise InvalidBrowser(f'{user_config["web"]["browser"]} is not a valid browser. Please provide a valid '
                             f'browser name')
    driver_object.maximize_window()
    driver_object.set_page_load_timeout(user_config["web"]["page_load_timeout"])
    driver_object.implicitly_wait(user_config["web"]["implicit_wait_time"])
    return driver_object
