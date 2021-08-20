from pages import MainPage
from pages.PopupForm import RequestForm
import pytest


@pytest.mark.env("prod")
@pytest.mark.env("develop")
class TestRequestFormNoData:

    def test_should_be_request_link(self, browser, url):
        # Arrange
        page = MainPage(browser, url)
        # Act
        page.open_page()
        # Assert element
        page.should_be_request_link()

    def test_open_request_form(self, browser, url):
        # Arrange
        page = MainPage(browser, url)
        page.open_page()
        # Act
        page.open_request_form()
        form = RequestForm(browser, browser.current_url)
        # Assert title
        form.check_request_form()

    def test_send_empty_form(self, browser, url):
        # Arrange
        page = MainPage(browser, url)
        page.open_page()
        # Act
        page.open_request_form()
        form = RequestForm(browser, browser.current_url)
        form.submit_request()
        # Assert element not present
        form.check_success_msg_is_not_present()


@pytest.mark.env("prod")
class TestRequestFormWithData:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, url):
        # Arrange
        page = MainPage(browser, url)
        page.open_page()
        page.should_be_request_link()
        page.open_request_form()
        form = RequestForm(browser, browser.current_url)
        form.input_org_name()
        form.input_inn_number()
        form.input_person_name()
        form.input_phone_number()
        form.input_email()
        form.input_comment()

    @pytest.mark.env("develop")
    def test_close_request_form(self, browser, url):
        # Act
        form = RequestForm(browser, browser.current_url)
        form.close_request_form()
        # Assert request form is not present
        form.check_request_form_is_not_present()

    @pytest.mark.env("develop")
    def test_fill_text(self, browser, url):
        # Act
        form = RequestForm(browser, browser.current_url)
        form.submit_request()
        # Assert
        form.check_error_message_title()

    @pytest.mark.env("develop")
    def test_fill_checkbox(self, browser, url):
        # Act
        form = RequestForm(browser, browser.current_url)
        form.fill_spec_checkbox()
        form.fill_agreement_checkbox()
        form.submit_request()
        # Assert error message text "Для поля 'Реквизиты' необходимо прикрепить хотя бы один файл"
        form.check_requisite_error_text()

    @pytest.mark.env("develop")
    def test_upload_requisite_file(self, browser, url):
        # Act
        form = RequestForm(browser, browser.current_url)
        form.fill_spec_checkbox()
        form.fill_agreement_checkbox()
        form.load_requisite()
        # Assert file name
        form.check_requisite_file_name_is_present()

    @pytest.mark.env("develop")
    def test_check_list_file_error_text(self, browser, url):
        # Act
        form = RequestForm(browser, browser.current_url)
        form.fill_spec_checkbox()
        form.fill_agreement_checkbox()
        form.load_requisite()
        form.submit_request()
        # Assert error message text "Для поля 'Смета или список' необходимо прикрепить хотя бы один файл"
        form.check_list_error_text()

    @pytest.mark.env("develop")
    def test_upload_wrong_list_file(self, browser, url):
        # Act
        form = RequestForm(browser, browser.current_url)
        form.fill_spec_checkbox()
        form.fill_agreement_checkbox()
        form.load_requisite()
        form.load_list_wrong_type_file()
        form.submit_request()
        # Assert list file name
        form.check_list_type_error_text()

    @pytest.mark.env("develop")
    def test_upload_list_file(self, browser, url):
        # Act
        page = MainPage(browser, url)
        page.open_page()
        page.open_request_form()
        form = RequestForm(browser, browser.current_url)
        form.fill_spec_checkbox()
        form.fill_agreement_checkbox()
        form.load_requisite()
        form.load_list()
        # Assert list file name
        form.check_list_file_name_is_present()

    @pytest.mark.env("develop")
    def test_check_success_message(self, browser, url):
        # Act
        form = RequestForm(browser, browser.current_url)
        form.fill_spec_checkbox()
        form.fill_agreement_checkbox()
        form.load_requisite()
        # Assert success message text "Ваша заявка успешно отправлена"
        form.load_list()
        form.submit_request()
        form.check_success_msg_text()

    def test_send_request_form(self, browser, url):
        # Act
        form = RequestForm(browser, browser.current_url)
        form.fill_spec_checkbox()
        form.fill_agreement_checkbox()
        form.load_requisite()
        form.load_list()
        form.should_be_submit_btn()
        form.submit_request()
        form.push_success_btn()
        # Assert
        form.check_request_form_is_not_present()

