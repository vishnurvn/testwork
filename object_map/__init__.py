from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Element:
    def __init__(self, selector: str, _type: str):
        self._selector = selector
        self._type = _type

    @property
    def props(self):
        return self._type, self._selector

    @property
    def selector(self):
        return self._selector

    @property
    def selector_type(self):
        return self._type


class ObjectMap(object):
    def __init__(self, driver):
        if not isinstance(driver, WebDriver):
            raise TypeError(f'driver of type: {type(driver)} is not an instance of class WebDriver')
        self.driver = driver

    def __getattribute__(self, item: str):
        if not item.isupper():
            return object.__getattribute__(self, item)

        attribute = object.__getattribute__(self, item)
        driver = object.__getattribute__(self, 'driver')
        selector_type = getattr(By, attribute.selector_type)
        return GetElement(driver, selector_type, attribute.selector)


class GetElement:
    def __init__(self, driver, selector_type, selector):
        self.driver = driver
        self.selector_type = selector_type
        self.selector = selector

    def get(self):
        return self.driver.find_element(self.selector_type, self.selector)

    def wait(self):
        return Wait(self.driver, self.selector_type, self.selector)


class Wait:
    def __init__(self, driver, selector_type, selector):
        self.driver = driver
        self.selector_type = selector_type
        self.selector = selector

    def __getattr__(self, item):
        wait_condition = getattr(ec, item)
        return WebDriverWait(self.driver, 60).until(wait_condition((self.selector_type, self.selector)))
