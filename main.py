import logging
import unittest

from selenium import webdriver
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import Config
from object_map.alsc import (HomePage, DisclaimerPage, LoginPage)

LOGGER.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('./selenium.log', mode='w', encoding='utf-8')
LOGGER.addHandler(file_handler)


class SampleTestCase(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        SampleTestCase.driver = webdriver.Chrome(Config.CHROME_DRIVER_LOCATION)
        SampleTestCase.driver.maximize_window()
        SampleTestCase.driver.find_element()

    def step_1(self):
        SampleTestCase.driver.get("http://phxalc5lapp416.comp.nadc.accenture.com:8001/ALSCWebApp/login.html")
        WebDriverWait(SampleTestCase.driver, 30). \
            until(EC.element_to_be_clickable(LoginPage.LOGIN_BUTTON.props))

    def step_2(self):
        SampleTestCase.driver.find_element(LoginPage.USERNAME_FIELD.props).send_keys('username')
        SampleTestCase.driver.find_element(LoginPage.PASSWORD_FIELD.props).send_keys('password')
        SampleTestCase.driver.find_element(LoginPage.LOGIN_BUTTON.props).click()

    def step_3(self):
        element = WebDriverWait(SampleTestCase.driver, 30). \
            until(EC.element_to_be_clickable(DisclaimerPage.ACCEPT_BUTTON.props))
        element.click()

    def step_4(self):
        element = WebDriverWait(SampleTestCase.driver, 30). \
            until(EC.element_to_be_clickable(HomePage.RAVE_ICON.props))
        element.click()

    def _steps(self):
        steps = []
        for name in dir(self):
            if name.startswith('step'):
                steps.append((name, getattr(self, name)))
        return steps

    def test_steps(self):
        for name, step in self._steps():
            try:
                print(f'Executing step {name}')
                step()
            except Exception as e:
                self.fail(f'{step} failed ({type(e)}:{e})')

    @classmethod
    def tearDownClass(cls) -> None:
        SampleTestCase.driver.quit()
