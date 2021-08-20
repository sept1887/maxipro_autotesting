from .BasePage import BasePage
from .LOCATORS import CartPageLocators
from .Data import CartPageData


class CartPage(BasePage):

    def check_success_msg_title(self):
        assert self.is_element_present(*CartPageLocators.SUCCESS_MSG_TITLE), "Success message is not presented"
        act_success_msg_title = self.browser.find_element(*CartPageLocators.SUCCESS_MSG_TITLE).text
        assert act_success_msg_title == CartPageLocators.EXP_SUCCESS_MSG_TITLE, \
            f"Expected success message title is '{CartPageLocators.EXP_SUCCESS_MSG_TITLE}', " \
            f"but actual success message title is '{act_success_msg_title}'"

    def choose_delivery_method(self):
        self.fill_checkbox(*CartPageLocators.DELIVERY_PICKUP)

    def fill_name(self):
        self.input_value(CartPageData.name, *CartPageLocators.NAME)

    def fill_phone(self):
        self.input_value(CartPageData.phone, *CartPageLocators.PHONE)

    def place_one_click_order(self):
        self.push_the_btn(*CartPageLocators.ONE_CLICK_ORDER_BTN)

    def send_an_order(self):
        self.push_the_btn(*CartPageLocators.SEND_AN_ORDER_BTN)

    def should_be_cart_page(self):
        assert "cart" in self.browser.current_url
