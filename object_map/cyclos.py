from object_map import Element, ObjectMap


class HomePage(ObjectMap):
    SIGN_IN_LINK = Element("//span[text()='Sign in']", "XPATH")
    BUSINESS_DIR_LINK = Element("//span[text()='Business directory']", "XPATH")
    DEMO_TEN_LINK = Element("//div[text()='Demo ten']", "XPATH")


class LoginPage(ObjectMap):
    USERNAME_FIELD = Element("principal", "NAME")
    PASSWORD_FIELD = Element("password", "NAME")
    LOGIN_BUTTON = Element("//div[contains(text(), 'Sign in') and @class='actionButtonText']", "XPATH")

    @staticmethod
    def sign_in(driver):
        LoginPage(driver).USERNAME_FIELD.wait().element_to_be_clickable.send_keys('demo.user')
        LoginPage(driver).PASSWORD_FIELD.get().send_keys('demo123')
        LoginPage(driver).LOGIN_BUTTON.get().click()


class HomePageLoggedIn(ObjectMap):
    ACCOUNT_INTO_BUTTON = Element("//div[text()='Account info']", "XPATH")
    BALANCE_TEXT = Element("//span[contains(text(), 'Balance:')]", "XPATH")
