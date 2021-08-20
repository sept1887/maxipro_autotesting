from .BasePage import BasePage
from .LOCATORS import MainPageLocators
import random


class MainPage(BasePage):

    def check_improvement_form(self):
        self.check_popup(*MainPageLocators.IMPROVEMENT_POPUP_TITLE_ACT,
                         MainPageLocators.IMPROVEMENT_POPUP_TITLE_EXP)



    def open_cart_from_main_page(self):
        self.push_the_btn(*MainPageLocators.CART_LINK)

    def open_improvement_form(self):
        self.push_the_btn(*MainPageLocators.IMPROVEMENT_LINK)

    def open_login_form(self):
        self.push_the_btn(*MainPageLocators.LOGIN_LINK)

    def open_request_form(self):
        self.push_the_btn(*MainPageLocators.REQUEST_LINK)

    def push_add_to_cart_btn(self):
        self.is_element_present(*MainPageLocators.ADD_TO_CART_BTN)
        btn_list = self.browser.find_elements(*MainPageLocators.ADD_TO_CART_BTN)
        random.choice(btn_list[0:4]).click()

    def push_place_an_order_btn(self):
        assert self.is_element_present(*MainPageLocators.PLACE_AN_ORDER_BTN)
        self.push_the_btn(*MainPageLocators.PLACE_AN_ORDER_BTN)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), \
            "Login link is not presented"

    def should_be_request_link(self):
        assert self.is_element_present(*MainPageLocators.REQUEST_LINK), \
            "Request link is not presented"

