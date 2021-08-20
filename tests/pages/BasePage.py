from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def check_input_value(self, how, what):
        return self.browser.find_element(how, what).get_attribute("value")

    def check_popup(self, how, what, exp_value, sec_alert=0):
        assert self.is_element_present(how, what, timeout=15), "Element is not presented"
        act_value = self.browser.find_element(how, what).text
        assert (act_value == exp_value) or (act_value == sec_alert), \
            f"Expected value is '{exp_value}', but actual value is '{act_value}'"

    def fill_checkbox(self, how, what):
        checkbox = self.browser.find_element(how, what)
        checkbox.click()

    def fill_checkbox_with_link(self, how, what):
        assert self.is_element_present(how, what), "Agreement checkbox is not presented"
        agreement_checkbox = self.browser.find_element(how, what)
        ActionChains(self.browser).move_to_element_with_offset(agreement_checkbox, 10, 10).click().perform()

    def input_value(self, value, how, what):
        value_area = self.browser.find_element(how, what)
        value_area.send_keys(value)

    def is_element_present(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_not_element_present(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_element_available(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_located_to_be_selected((how, what)))
        except TimeoutException:
            return True

        return False

    def load_file(self, how, what, file_name):
        file = self.browser.find_element(how, what)
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, file_name)
        file.send_keys(file_path)

    def open_page(self):
        self.browser.get(self.url)

    def push_the_btn(self, how, what):
        self.browser.find_element(how, what).click()
        time.sleep(10)

    def scroll_down(self, offset=0):
        if offset:
            self.browser.execute_script("window.scrollTo(0, {0});".format(offset))  # scroll down with offset
        else:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scroll to the page bottom

    def scroll_up(self, offset=0):
        if offset:
            self.browser.execute_script("window.scrollTo(0, -{0});".format(offset))  # scroll up with offset
        else:
            self.browser.execute_script("window.scrollTo(0, -document.body.scrollHeight);")  # scroll to the page top

