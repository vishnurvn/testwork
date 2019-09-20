from object_map import cyclos
from source.src import driver
from test_cases import TestCase

driver = driver()


class TestCaseOne(TestCase):
    def step_1(self):
        driver.get('https://demo.cyclos.org/')
        cyclos.HomePage(driver).SIGN_IN_LINK.wait().element_to_be_clickable.click()

    def step_2(self):
        cyclos.LoginPage.sign_in(driver)

    def step_3(self):
        cyclos.HomePageLoggedIn(driver).ACCOUNT_INTO_BUTTON.wait().element_to_be_clickable.click()
        text = cyclos.HomePageLoggedIn(driver).BALANCE_TEXT.wait()
        assert text == 'Balance: 761,66 IU'


TestCaseOne().execute()
