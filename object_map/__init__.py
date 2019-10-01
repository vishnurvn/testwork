from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from source.web_src import driver


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


class Wait:
    def __init__(self, driver_instance, selector_type, selector):
        self.driver = driver_instance
        self.selector_type = selector_type
        self.selector = selector

    def __getattr__(self, item) -> WebElement:
        wait_condition = getattr(ec, item)
        return WebDriverWait(self.driver, 60).until(wait_condition((self.selector_type, self.selector)))


class GetElement:
    def __init__(self, driver_instance, selector_type, selector):
        self.driver = driver_instance
        self.selector_type = selector_type
        self.selector = selector

    def get_element(self) -> WebElement:
        return self.driver.find_element(self.selector_type, self.selector)

    def get_element_list(self) -> WebElement:
        return self.driver.find_elements(self.selector_type, self.selector)

    def wait(self) -> Wait:
        return Wait(self.driver, self.selector_type, self.selector)


class ObjectMap(object):
    def __init__(self):
        self.driver = driver()

    def __getattribute__(self, item: str) -> GetElement:
        if not item.isupper():
            return object.__getattribute__(self, item)

        attribute = object.__getattribute__(self, item)
        driver_instance = object.__getattribute__(self, 'driver')
        selector_type = getattr(By, attribute.selector_type)
        return GetElement(driver_instance, selector_type, attribute.selector)
