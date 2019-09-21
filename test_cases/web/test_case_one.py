from object_map import cyclos
from source import TestCase, driver
from source.test_case_src import TestData


class TestCaseOne(TestCase):
    def step_1(self, url):
        driver().get(url)
        cyclos.HomePage().SIGN_IN_LINK.wait().element_to_be_clickable.click()

    #
    def step_2(self, username, password):
        cyclos.LoginPage().sign_in(username, password)
    #
    # def step_3(self):
    #     cyclos.HomePageLoggedIn(driver).ACCOUNT_INTO_BUTTON.wait().element_to_be_clickable.click()
    #     text = cyclos.HomePageLoggedIn(driver).BALANCE_TEXT.wait().visibility_of_element_located.text
    #     assert text == "Balance: 761,66 IU's"


if __name__ == '__main__':
    import os

    parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    test_data_file = os.path.basename(__file__).split('.')[0]
    test_data_path = os.path.join(parent_dir, 'test_data\\web\\{}.data'.format(test_data_file))
    test_data = TestData(test_data_path)
    TestCaseOne().execute(test_data, 'run_1')
