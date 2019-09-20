from object_map import Element, ObjectMap


class HomePage:
    SIGN_IN_LINK = Element("//span[text()='Sign in']", "XPATH")
    BUSINESS_DIR_LINK = Element("//span[text()='Business directory']", "XPATH")
    DEMO_TEN_LINK = Element("//div[text()='Demo ten']", "XPATH")


class HomePageTwo(ObjectMap):
    SIGN_IN_LINK = Element("//span[text()='Sign in']", "XPATH")
    BUSINESS_DIR_LINK = Element("//span[text()='Business directory']", "XPATH")
    DEMO_TEN_LINK = Element("//div[text()='Demo ten']", "XPATH")

    def sign_in(self):
        print(self.driver)
