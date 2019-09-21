from object_map import Element, ObjectMap


class HomePage(ObjectMap):
    SIGN_IN_LINK = Element("//span[text()='Sign in']", "XPATH")
    BUSINESS_DIR_LINK = Element("//span[text()='Business directory']", "XPATH")
    DEMO_TEN_LINK = Element("//div[text()='Demo ten']", "XPATH")


class LoginPage(ObjectMap):
    USERNAME_FIELD = Element("principal", "NAME")
    PASSWORD_FIELD = Element("password", "NAME")
    LOGIN_BUTTON = Element("//div[contains(text(), 'Sign in') and @class='actionButtonText']", "XPATH")

    def sign_in(self, username, password):
        self.USERNAME_FIELD.wait().element_to_be_clickable.send_keys(username)
        self.PASSWORD_FIELD.get_element().send_keys(password)
        self.LOGIN_BUTTON.get_element().click()


class HomePageLoggedIn(ObjectMap):
    ACCOUNT_INTO_BUTTON = Element("//div[text()='Account info']", "XPATH")
    BALANCE_TEXT = Element("//span[contains(text(), 'Balance:')]", "XPATH")
