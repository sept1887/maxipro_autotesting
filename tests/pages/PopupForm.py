from .BasePage import BasePage
from .LOCATORS import RequestFormLocators, LoginFormLocators
from .Data import RequestFormData


class RequestForm(BasePage):
    def check_agreement_error_text(self):
        self.check_popup(*RequestFormLocators.ERROR_MSG_TXT,
                         RequestFormLocators.AGREEMENT_ERROR_TXT, RequestFormLocators.SECURITY_ALERT)

    def check_error_message_title(self):
        self.check_popup(*RequestFormLocators.ERROR_MSG_TITLE_ACT,
                         RequestFormLocators.ERROR_MSG_TITLE_EXP, RequestFormLocators.SECURITY_ALERT)

    def check_list_error_text(self):
        self.check_popup(*RequestFormLocators.ERROR_MSG_TXT,
                         RequestFormLocators.LIST_FILE_ERROR_TXT, RequestFormLocators.SECURITY_ALERT)

    def check_list_type_error_text(self):
        self.check_popup(*RequestFormLocators.ERROR_MSG_TXT,
                         RequestFormLocators.LIST_TYPE_ERROR_TXT, RequestFormLocators.SECURITY_ALERT)

    def check_list_file_name_is_present(self):
        self.check_popup(*RequestFormLocators.LIST_FILE_NAME,
                         RequestFormLocators.LIST_FILE, RequestFormLocators.SECURITY_ALERT)

    def check_phone_error_text(self):
        self.check_popup(*RequestFormLocators.ERROR_MSG_TXT,
                         RequestFormLocators.PHONE_ERROR_TXT, RequestFormLocators.SECURITY_ALERT)

    def check_success_msg_text(self):
        self.check_popup(*RequestFormLocators.SUCCESS_MSG_TXT_ACT,
                         RequestFormLocators.SUCCESS_MSG_TXT_EXP, RequestFormLocators.SECURITY_ALERT)

    def check_success_msg_is_not_present(self):
        assert self.is_not_element_present(*RequestFormLocators.SUCCESS_MSG_TXT_ACT, timeout=10), \
            "Success message is presented, but should not be"

    def check_requisite_file_name_is_present(self):
        self.check_popup(*RequestFormLocators.REQUISITE_FILE_NAME, RequestFormLocators.REQUISITE_FILE)

    def check_requisite_error_text(self):
        self.check_popup(*RequestFormLocators.ERROR_MSG_TXT,
                         RequestFormLocators.REQUISITE_ERROR_TXT, RequestFormLocators.SECURITY_ALERT)

    def check_request_form(self):
        self.check_popup(*RequestFormLocators.REQUEST_FORM_TITLE_ACT, RequestFormLocators.REQUEST_FORM_TITLE_EXP)

    def check_request_form_is_not_present(self):
        assert self.is_not_element_present(*RequestFormLocators.POPUP_ACTIVE), \
            "Request form is presented, but should not be"

    def close_request_form(self):
        self.push_the_btn(*RequestFormLocators.CLOSE_FORM_BTN)

    def input_org_name(self):
        self.input_value(RequestFormData.organisation, *RequestFormLocators.ORG_AREA)

    def input_inn_number(self):
        self.input_value(RequestFormData.inn, *RequestFormLocators.INN_AREA)
        inn = RequestFormData.inn
        assert self.check_input_value(*RequestFormLocators.INN_AREA) \
               == inn[0:10], f'Expected value is "{inn}", ' \
                             f'but actual value is "{self.check_input_value(*RequestFormLocators.INN_AREA)}"'

    def input_person_name(self):
        self.input_value(RequestFormData.name, *RequestFormLocators.NAME_AREA)

    def input_phone_number(self):
        self.input_value(RequestFormData.phone, *RequestFormLocators.PHONE_AREA)
        phone = RequestFormData.phone
        phone_in_form = ('+7' + ' ' + '(' + phone[0:3] + ')' + ' ' + phone[3:6] + '-' + phone[6:8] + '-' + phone[8:10])
        assert self.check_input_value(*RequestFormLocators.PHONE_AREA) \
               == phone_in_form, f'Expected value is "{phone_in_form}", ' \
                                f'but actual value is "{self.check_input_value(*RequestFormLocators.PHONE_AREA)}"'

    def input_email(self):
        self.input_value(RequestFormData.email, *RequestFormLocators.EMAIL_AREA)

    def input_comment(self):
        self.input_value(RequestFormData.comment, *RequestFormLocators.COMMENT_AREA)
        assert self.check_input_value(*RequestFormLocators.COMMENT_AREA) \
               == RequestFormData.comment, f'Expected value is "{RequestFormData.comment}", ' \
                           f'but actual value is "{self.check_input_value(*RequestFormLocators.COMMENT_AREA)}"'

    def fill_spec_checkbox(self):
        self.fill_checkbox(*RequestFormLocators.CHECKBOX)

    def fill_agreement_checkbox(self):
        self.fill_checkbox_with_link(*RequestFormLocators.AGREEMENT_CHECKBOX)

    def load_requisite(self):
        self.load_file(*RequestFormLocators.LOAD_REQUISITE, RequestFormLocators.REQUISITE_FILE)

    def load_list(self):
        self.load_file(*RequestFormLocators.LOAD_LIST, RequestFormLocators.LIST_FILE)

    def load_list_wrong_type_file(self):
        self.load_file(*RequestFormLocators.LOAD_LIST, RequestFormLocators.LIST_FILE_WRONG_TYPE)

    def push_error_msg_btn(self):
        self.push_the_btn(*RequestFormLocators.ERROR_MSG_BTN)

    def push_success_btn(self):
        self.push_the_btn(*RequestFormLocators.SUCCESS_MSG_BTN)

    def should_be_submit_btn(self):
        assert self.is_element_present(*RequestFormLocators.SUBMIT_BTN), "Submit button is not presented"

    def submit_request(self):
        self.push_the_btn(*RequestFormLocators.SUBMIT_BTN)


class LoginForm(BasePage):

    def back_to_login_form_from_restore_pass_form(self):
        self.push_the_btn(*LoginFormLocators.LOGIN_LINK)

    def check_restore_pass_enter_code_form(self):
        self.check_popup(*LoginFormLocators.RESTORE_PASS_ENTER_CODE_FORM,
                         LoginFormLocators.RESTORE_PASS_FORM_TITLE_EXP)

    def check_enter_with_pass_form(self):
        self.check_popup(*LoginFormLocators.ENTER_WITH_PASS_FORM_TITLE_ACT,
                         LoginFormLocators.ENTER_WITH_PASS_FORM_TITLE_EXP)

    def check_login_form_closed(self):
        assert self.is_not_element_present(*LoginFormLocators.LOGIN_POPUP_ACTIVE)

    def check_enter_with_code_form(self):
        self.check_popup(*LoginFormLocators.ENTER_WITH_CODE_FORM_TITLE_ACT,
                         LoginFormLocators.ENTER_WITH_CODE_FORM_TITLE_EXP)

    def check_login_pass_form(self):
        self.check_popup(*LoginFormLocators.LOGIN_PASSWORD_POPUP_TITLE_ACT,
                         LoginFormLocators.LOGIN_PASSWORD_POPUP_TITLE_EXP)

    def check_login_success(self):
        assert self.is_element_present(*LoginFormLocators.SUCCESS_LOGIN_ICON), "User icon is not presented"

    def check_restore_pass_form(self):
        self.check_popup(*LoginFormLocators.RESTORE_PASS_FORM_TITLE_ACT, LoginFormLocators.RESTORE_PASS_FORM_TITLE_EXP)

    def close_login_form(self):
        self.push_the_btn(*LoginFormLocators.CLOSE_FORM_BTN)

    def get_code_is_not_available(self):
        assert self.browser.find_element(*LoginFormLocators.GET_CODE_BTN).get_attribute("disabled")

    def input_password(self):
        self. input_value(RequestFormData.password, *LoginFormLocators.PASSWORD_AREA)

    def input_pass_in_restore_pass_form(self):
        self.input_value(RequestFormData.password, *LoginFormLocators.RESTORE_FORM_PASS)

    def input_pass_in_restore_pass_form_repeat(self):
        self.input_value(RequestFormData.password, *LoginFormLocators.RESTORE_FORM_PASS_REPEAT)

    def input_phone_number(self):
        self.input_value(RequestFormData.phone, *LoginFormLocators.PHONE_AREA)
        phone = RequestFormData.phone
        phone_in_form = ('+7' + ' ' + '(' + phone[0:3] + ')' + ' ' + phone[3:6] + '-' + phone[6:8] + '-' + phone[8:10])
        assert self.check_input_value(*LoginFormLocators.PHONE_AREA) \
               == phone_in_form, f'Expected value is "{phone_in_form}", ' \
                                f'but actual value is "{self.check_input_value(*LoginFormLocators.PHONE_AREA)}"'

    def input_phone_number_in_restore_pass_form(self):
        self.input_value(RequestFormData.phone, *LoginFormLocators.RESTORE_FORM_PHONE)
        phone = RequestFormData.phone
        phone_in_form = ('+7' + ' ' + '(' + phone[0:3] + ')' + ' ' + phone[3:6] + '-' + phone[6:8] + '-' + phone[8:10])
        assert self.check_input_value(*LoginFormLocators.RESTORE_FORM_PHONE) \
               == phone_in_form, f'Expected value is "{phone_in_form}", ' \
                                 f'but actual value is "{self.check_input_value(*LoginFormLocators.RESTORE_FORM_PHONE)}"'

    def open_login_code_form(self):
        self.push_the_btn(*LoginFormLocators.LOGIN_CODE_LINK)

    def open_login_password_form(self):
        self.push_the_btn(*LoginFormLocators.LOGIN_PASSWORD_LINK)

    def open_restore_pass_form(self):
        self.push_the_btn(*LoginFormLocators.RESTORE_PASS_LINK)

    def open_receive_code_form(self):
        self.push_the_btn(*LoginFormLocators.RESTORE_FORM_RECEIVE_CODE_BTN)

    def should_be_close_btn(self):
        assert self.is_element_present(*LoginFormLocators.CLOSE_FORM_BTN)

    def should_be_enter_with_code_link(self):
        assert self.browser.find_element(*LoginFormLocators.LOGIN_CODE_LINK), \
            "Login with code link is not presented"

    def should_be_login_link(self):
        assert self.is_element_present(*LoginFormLocators.LOGIN_LINK)

    def should_be_new_code_link(self):
        assert self.is_element_present(*LoginFormLocators.RESTORE_PASS_ENTER_CODE_FORM_NEW_CODE_LINK)

    def should_be_enter_with_pass_link(self):
        assert self.is_element_present(*LoginFormLocators.LOGIN_PASSWORD_LINK), \
            "Password link is not presented"

    def should_be_receive_code_btn(self):
        assert self.is_element_available(*LoginFormLocators.RESTORE_FORM_RECEIVE_CODE_BTN)

    def should_be_restore_pass_link(self):
        assert self.is_element_present(*LoginFormLocators.RESTORE_PASS_LINK)

    def should_be_submit_pass_btn(self):
        assert self.is_element_available(*LoginFormLocators.SUBMIT_PASS_BTN), "Submit password button is not available"

    def submit_btn_is_not_available(self):
        assert self.browser.find_element(*LoginFormLocators.RESTORE_PASS_ENTER_CODE_FORM_SUBMIT_BTN).get_attribute("disabled")

    def submit_pass_btn(self):
        self.push_the_btn(*LoginFormLocators.SUBMIT_PASS_BTN)





