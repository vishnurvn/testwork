from object_map import cyclos
from source import TestCase, driver


class TestCaseTwo(TestCase):
    __name__ = 'test_case_two'
    __description__ = "This is another description for this test case"

    def step_1(self, url):
        """
        :description: Hello world
        :expected: This is an expected result
        """
        driver().get(url)
        cyclos.HomePage().SIGN_IN_LINK.wait().element_to_be_clickable.click()

    def step_2(self, username, password):
        """
        :description: Hello world
        :expected: This is an expected result
        """
        cyclos.LoginPage().sign_in(username, password)

    # def step_3(self):
    #     cyclos.HomePageLoggedIn(driver).ACCOUNT_INTO_BUTTON.wait().element_to_be_clickable.click()
    #     text = cyclos.HomePageLoggedIn(driver).BALANCE_TEXT.wait().visibility_of_element_located.text
    #     assert text == "Balance: 761,66 IU's"


if __name__ == '__main__':
    TestCaseTwo().execute('run_1')
