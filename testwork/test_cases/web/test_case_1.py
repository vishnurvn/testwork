from object_map import cyclos
from source import TestCase, driver
from source.web.run import run_test_case


class TestCase1(TestCase):
    __name__ = 'test_case_1'
    __description__ = "This is a description for this test case"

    def step_1(self, url):
        """
        :description: Launch URL: {url} and click on sign in link
        :expected_result: Cyclos home page is displayed. Sign in link is clicked. Sign in page is displayed.
        """
        driver().get(url)
        cyclos.HomePage().SIGN_IN_LINK.get_element().click()

    # def step_2(self, username, password):
    #     """
    #     :description: Enter username: {username} and password. Click on Sign in button.
    #     :expected_result: Cyclos home page is displayed.
    #     """
    #     cyclos.LoginPage().USERNAME_FIELD.wait().element_to_be_clickable.send_keys(username)
    #     cyclos.LoginPage().PASSWORD_FIELD.get_element().send_keys(password)
    #     cyclos.LoginPage().LOGIN_BUTTON.get_element().click()
    #
    # def step_3(self, balance):
    #     """
    #     :description: Click on Account info button. Verify balance is {balance}
    #     :expected_result: The balance of the account in {balance}
    #     """
    #     cyclos.HomePageLoggedIn().ACCOUNT_INTO_BUTTON.wait().element_to_be_clickable.click()
    #     text = cyclos.HomePageLoggedIn().BALANCE_TEXT.wait().visibility_of_element_located.text
    #     assert text == balance
    #
    # def step_4(self, email):
    #     """
    #     :description: Click on personal tab. Verify email is {email}
    #     :expected_result: The email is {email}
    #     """
    #     cyclos.HomePageLoggedIn().PERSONAL_TAB.get_element().click()
    #     text = cyclos.PersonalTab().EMAIL.wait().visibility_of_element_located.text
    #     assert text == email
    #
    # def step_5(self):
    #     """
    #     :description: Click on logout button.
    #     :expected_result: Home page is displayed
    #     """
    #     cyclos.HomePageLoggedIn().LOGOUT_LINK.get_element().click()
    #     cyclos.HomePage().SIGN_IN_LINK.get_element()


if __name__ == '__main__':
    run_test_case(__file__, 'run_1')
