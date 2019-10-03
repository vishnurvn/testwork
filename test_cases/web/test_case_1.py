from object_map import cyclos
from source import TestCase, driver


class TestCaseOne(TestCase):
    __name__ = 'test_case_one'
    __description__ = "This is a description for this test case"

    def step_1(self, url):
        """
        :description: Launch URL: {url} and click on sign in link
        :expected: Cyclos home page is displayed. Sign in link is clicked. Sign in page is displayed.
        """
        driver().get(url)
        cyclos.HomePage().SIGN_IN_LINK.get_element().click()

    def step_2(self, username, password):
        """
        :description: Enter username: {username} and password. Click on Sign in button.
        :expected: Cyclos home page is displayed.
        """
        cyclos.LoginPage().USERNAME_FIELD.wait().element_to_be_clickable.send_keys(username)
        cyclos.LoginPage().PASSWORD_FIELD.get_element().send_keys(password)
        cyclos.LoginPage().LOGIN_BUTTON.get_element().click()

    def step_3(self):
        """
        :description: Click on Account info button. Verify balance is {balance}
        :expected: The balance of the account in {balance}
        """
        cyclos.HomePageLoggedIn().ACCOUNT_INTO_BUTTON.wait().element_to_be_clickable.click()
        text = cyclos.HomePageLoggedIn().BALANCE_TEXT.wait().visibility_of_element_located.text
        assert text == "Balance: 8.990,90 IU's"


if __name__ == '__main__':
    TestCaseOne().execute('run_1')
