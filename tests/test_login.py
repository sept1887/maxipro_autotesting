from pages import MainPage
from pages.PopupForm import LoginForm
import pytest
import time


@pytest.mark.env("develop")
@pytest.mark.env("prod")
class TestLoginForm:
    @pytest.fixture(scope="function")
    def setup(self, browser, url):
        # Arrange
        main_page = MainPage(browser, url)
        main_page.open_page()
        main_page.open_login_form()

    def test_should_be_login_link(self, browser, url):
        # Arrange
        main_page = MainPage(browser, url)
        main_page.open_page()
        # Assert
        main_page.should_be_login_link()

    def test_open_login_form(self, browser, url, setup):
        login_form = LoginForm(browser, browser.current_url)
        # Assert
        login_form.check_enter_with_code_form()

    def test_get_code_is_not_available(self, browser, url, setup):
        login_form = LoginForm(browser, browser.current_url)
        # Assert
        login_form.get_code_is_not_available()

    def test_should_be_enter_with_pass_link(self, browser, url, setup):
        login_form = LoginForm(browser, browser.current_url)
        # Assert
        login_form.should_be_enter_with_pass_link()

    def test_should_be_close_btn(self, browser, url, setup):
        login_form = LoginForm(browser, browser.current_url)
        # Assert
        login_form.should_be_close_btn()

    def test_close_login_form(self, browser, url, setup):
        login_form = LoginForm(browser, browser.current_url)
        login_form.close_login_form()
        # Assert
        login_form.check_login_form_closed()


@pytest.mark.env("prod")
class TestLoginWithPasswordForm:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, url):
        # Arrange
        main_page = MainPage(browser, url)
        main_page.open_page()
        main_page.open_login_form()
        login_form = LoginForm(browser, browser.current_url)
        login_form.open_login_password_form()

    @pytest.mark.env("develop")
    def test_open_enter_with_pass_form(self, browser, url):
        login_form = LoginForm(browser, browser.current_url)
        time.sleep(3)
        # Assert
        login_form.check_enter_with_pass_form()

    @pytest.mark.env("develop")
    def test_should_enter_with_code_link(self, browser, url):
        login_form = LoginForm(browser, browser.current_url)
        # Assert
        login_form.should_be_enter_with_code_link()

    @pytest.mark.env("develop")
    def test_open_enter_with_code_form_from_enter_with_pass_form(self, browser, url):
        login_form = LoginForm(browser, browser.current_url)
        login_form.open_login_code_form()
        # Assert
        login_form.check_enter_with_code_form()

    @pytest.mark.env("develop")
    def test_should_be_restore_pass_link(self, browser, url):
        login_form = LoginForm(browser, browser.current_url)
        # Assert
        login_form.should_be_restore_pass_link()

    @pytest.mark.env("develop")
    def test_fill_login_form(self, browser, url):
        login_form = LoginForm(browser, browser.current_url)
        login_form.input_phone_number()
        login_form.input_password()
        # Assert
        login_form.should_be_submit_pass_btn()

    def test_login_form_submit(self, browser, url):
        login_form = LoginForm(browser, browser.current_url)
        login_form.input_phone_number()
        login_form.input_password()
        login_form.submit_pass_btn()
        # Assert
        login_form.check_login_success()


@pytest.mark.env("develop")
@pytest.mark.env("prod")
class TestRestorePasswordForm:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, url):
        # Arrange
        main_page = MainPage(browser, url)
        main_page.open_page()
        main_page.open_login_form()
        login_form = LoginForm(browser, browser.current_url)
        login_form.open_login_password_form()
        login_form.open_restore_pass_form()

    def test_restore_pass_form(self, browser, url):
        login_form = LoginForm(browser, browser.current_url)
        # Assert
        login_form.check_restore_pass_form()

    def test_should_be_login_link(self, browser, url):
        login_form = LoginForm(browser, browser.current_url)
        # Assert
        login_form.should_be_login_link()

    def test_back_to_login_form_from_restore_pass_form(self, browser, url):
        login_form = LoginForm(browser, browser.current_url)
        login_form.back_to_login_form_from_restore_pass_form()
        # Assert
        login_form.check_login_pass_form()

    def test_fill_restore_pass_form(self, browser, url):
        login_form = LoginForm(browser, browser.current_url)
        login_form.input_phone_number_in_restore_pass_form()
        login_form.input_pass_in_restore_pass_form()
        login_form.input_pass_in_restore_pass_form_repeat()
        # Assert
        login_form.should_be_receive_code_btn()

    def test_receive_code_form(self, browser, url):
        login_form = LoginForm(browser, browser.current_url)
        login_form.input_phone_number_in_restore_pass_form()
        login_form.input_pass_in_restore_pass_form()
        login_form.input_pass_in_restore_pass_form_repeat()
        login_form.open_receive_code_form()
        # Assert
        login_form.check_restore_pass_enter_code_form()


@pytest.mark.env("develop")
@pytest.mark.env("prod")
class TestReceiveCodeForm:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, url):
        # Arrange
        main_page = MainPage(browser, url)
        main_page.open_page()
        main_page.open_login_form()
        login_form = LoginForm(browser, browser.current_url)
        login_form.open_login_password_form()
        login_form.open_restore_pass_form()
        login_form.input_phone_number_in_restore_pass_form()
        login_form.input_pass_in_restore_pass_form()
        login_form.input_pass_in_restore_pass_form_repeat()
        login_form.open_receive_code_form()

    def test_should_be_new_code_link(self, browser, url):
        login_form = LoginForm(browser, browser.current_url)
        # Assert
        login_form.should_be_new_code_link()

    def test_should_be_login_link(self, browser, url):
        login_form = LoginForm(browser, browser.current_url)
        # Assert
        login_form.should_be_login_link()

    def test_submit_btn_is_not_available(self, browser, url):
        login_form = LoginForm(browser, browser.current_url)
        # Assert
        login_form.submit_btn_is_not_available()

