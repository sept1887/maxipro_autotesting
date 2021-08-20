from pages import MainPage, CartPage
import time
import pytest


@pytest.mark.env("prod")
class TestMainPage:

    def test_add_to_cart_from_main_page(self, browser, url):
        # Arrange
        main_page = MainPage(browser, url)
        main_page.open_page()
        main_page.scroll_down(1000)
        # Act
        main_page.push_add_to_cart_btn()
        main_page.push_place_an_order_btn()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.place_one_click_order()
        cart_page.fill_name()
        cart_page.fill_phone()
        cart_page.choose_delivery_method()
        cart_page.send_an_order()
        # Assert
        cart_page.check_success_msg_title()

    @pytest.mark.env("develop")
    def test_open_improvement_form_from_main_page(self, browser, url):
        # Arrange
        main_page = MainPage(browser, url)
        main_page.open_page()
        main_page.scroll_down()
        # Act
        main_page.open_improvement_form()
        time.sleep(5)
        # Assert
        main_page.check_improvement_form()

    @pytest.mark.env("develop")
    def test_open_cart_from_main_page(self, browser, url):
        # Arrange
        main_page = MainPage(browser, url)
        main_page.open_page()
        # Act
        main_page.open_cart_from_main_page()
        cart_page = CartPage(browser, browser.current_url)
        # Assert
        cart_page.should_be_cart_page()
