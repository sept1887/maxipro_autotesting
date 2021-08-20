from selenium.webdriver.common.by import By


class MainPageLocators:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.js-add-to-basket")  # return list of buttons !!!
    CART_LINK = (By.ID, "header__right--basket_btn")
    LOGIN_LINK = (By.XPATH, "//div[@class='js-auth-block']")
    IMPROVEMENT_LINK = (By.CSS_SELECTOR, "button.service_improvement-callform")
    IMPROVEMENT_POPUP = (By.ID, "popup_improvement_callform")
    IMPROVEMENT_POPUP_TITLE_ACT = (By.CLASS_NAME, "popup-title")
    IMPROVEMENT_POPUP_TITLE_EXP = "Помогите нам улучшить сайт"
    PLACE_AN_ORDER_BTN = (By.XPATH, "//*[@id='product_add_basket_success']/div[4]/div[3]/a")
    REQUEST_LINK = (By.XPATH, "//button[@data-ajax-popup-new='PopupCompany']")


class CartPageLocators:
    CART_PAGE_TITLE = (By.XPATH, "//h1/strong[contains(text(), 'Корзина')]")
    DELIVERY_PICKUP = (By.XPATH, "//*[@id ='popup_fast_order-new']/form/div[4]/div[3]/div[2]/label")
    EXP_SUCCESS_MSG_TITLE = "Ваш заказ отправлен"
    NAME = (By.NAME, "name")
    ONE_CLICK_ORDER_BTN = (By.CSS_SELECTOR, "button.js-fast-order-btn")
    PHONE = (By.NAME, "phone")
    SEND_AN_ORDER_BTN = (By.CSS_SELECTOR, "button.js-fo-submit")
    SUCCESS_MSG_TITLE = (By.CSS_SELECTOR, "div.-green")


class LoginFormLocators:
    LOGIN_POPUP_ACTIVE = (By.XPATH, "//div[@class='fancybox-slide fancybox_wrapper fancybox-slide--html fancybox-slide--current fancybox-slide--complete']")
    LOGIN_CODE_LINK = (By.XPATH, "//*[@id='popup_login_password']/form/div[4]/div[1]/button")

    LOGIN_LINK = (By.XPATH, "//button[@class='c_btn_reset -back -grey']")
    LOGIN_PASSWORD_LINK = (By.XPATH, "//button[@class='cf_input-btn -red -mt-8 -mb0']")
    LOGIN_PASSWORD_POPUP = (By.ID, "popup_login_password")
    LOGIN_PASSWORD_POPUP_TITLE_ACT = (By.XPATH, "//*[@id='popup_login_password']/form/div[1]")
    LOGIN_PASSWORD_POPUP_TITLE_EXP = "Вход"
    LOGIN_POPUP = (By.ID, "popup_login_code")

    ENTER_WITH_CODE_FORM_TITLE_ACT = (By.XPATH, "//*[@id='popup_login_code']/form/div[1]")
    ENTER_WITH_CODE_FORM_TITLE_EXP = "Вход и Регистрация"
    ENTER_WITH_PASS_FORM_TITLE_ACT = (By.XPATH, "//*[@id='popup_login_password']/form/div[1]")
    ENTER_WITH_PASS_FORM_TITLE_EXP = "Вход"

    CLOSE_FORM_BTN = (By.XPATH, "//*[@id='popup_login_code']/button")
    GET_CODE_BTN = (By.XPATH, "//button[@class='c_btn -red w-100 -mb20 js-auth-sms-button']")

    PASSWORD_AREA = (By.NAME, "password")
    PHONE_AREA = (By.XPATH, "//*[@id='popup_login_password']/form/div[2]/label[1]/input")

    RESTORE_PASS_LINK = (By.XPATH, "//button[@data-target='#popup_password_restore']")
    RESTORE_PASS_ENTER_CODE_FORM = (By.XPATH, "//*[@id='popup_approv_rp']/form/div[1]")
    RESTORE_PASS_ENTER_CODE_FORM_NEW_CODE_LINK = (By.XPATH, "//*[@id='popup_approv_rp']/form/div[2]/div/div[1]/button")
    RESTORE_PASS_ENTER_CODE_FORM_SUBMIT_BTN = (By.XPATH, "//*[@id='popup_approv_rp']/form/button[2]")
    RESTORE_PASS_FORM_TITLE_ACT = (By.XPATH, "//*[@id='popup_password_restore']/form/div[1]")
    RESTORE_PASS_FORM_TITLE_EXP = "Восстановление пароля"
    RESTORE_FORM_PHONE = (By.XPATH, "//*[@id='popup_password_restore']/form/div[3]/label[1]/input")
    RESTORE_FORM_PASS = (By.XPATH, "//*[@id='popup_password_restore']/form/div[3]/label[2]/input")
    RESTORE_FORM_PASS_REPEAT = (By.XPATH, "//*[@id='popup_password_restore']/form/div[3]/label[3]/input")
    RESTORE_FORM_RECEIVE_CODE_BTN = (By.XPATH, "//button[@class='c_btn -red w-100 js-subm-btn']")

    SUBMIT_PASS_BTN = (By.XPATH, "//*[@id='popup_login_password']/form/button")
    SUCCESS_LOGIN_ICON = (By.CLASS_NAME, "header__right--iconuser")


class RequestFormLocators:

    CLOSE_FORM_BTN = (By.XPATH, "//*[@id='popup_company']/button[2]")
    POPUP_ACTIVE = (By.XPATH, "//div[@class='fancybox-container fancybox_base fancybox-is-open']")
    REQUEST_FORM_TITLE_ACT = (By.CSS_SELECTOR, "div.popup-title")
    REQUEST_FORM_TITLE_EXP = "Заявка на оформление договора"

    ORG_AREA = (By.NAME, "org")
    INN_AREA = (By.NAME, "inn")
    NAME_AREA = (By.NAME, "name")
    PHONE_AREA = (By.NAME, "phone")
    EMAIL_AREA = (By.XPATH, "//*[@id='popup_company']/div[3]/form/div[1]/div[9]/label/input")
    COMMENT_AREA = (By.NAME, "comment")

    CHECKBOX = (By.XPATH, "//*[@id='popup_company']/div[3]/form/div[1]/div[4]/label/span")
    AGREEMENT_CHECKBOX = (By.XPATH, "//*[@id='popup_company']/div[3]/form/div[2]/div[2]/label/span")
    LOAD_REQUISITE = (By.XPATH, "//input[@data-id='DETAILS']")
    REQUISITE_FILE = "requisite_2021.pdf"
    REQUISITE_FILE_NAME = (By.XPATH, "//*[@id='popup_company']/div[3]/form/div[1]/div[5]/div/div/div[2]/button/span[1]")

    LOAD_LIST = (By.NAME, "LIST[0]")
    LIST_FILE = "list_2021.docx"
    LIST_FILE_WRONG_TYPE = "list_2021.xlsx"
    LIST_FILE_NAME = (By.XPATH, "//*[@id='popup_company']/div[3]/form/div[1]/div[11]/div/div/div[2]/button/span[1]")

    SUBMIT_BTN = (By.XPATH, "//*[@id='popup_company']/div[3]/form/div[2]/div[1]/button")

    SECURITY_ALERT = "К сожалению, запрос, поступивший из вашей сети, похож на автоматический. Пожалуйста, попробуйте снова позже."
    ERROR_MSG_TITLE_ACT = (By.CSS_SELECTOR, "div.js-fb-msg-title")
    ERROR_MSG_TITLE_EXP = "Ошибка!"
    ERROR_MSG_TXT = (By.CSS_SELECTOR, "div.js-fb-msg-text")
    AGREEMENT_ERROR_TXT = "Необходимо согласие на обработку данных"
    REQUISITE_ERROR_TXT = 'Для поля "Реквизиты" необходимо прикрепить хотя бы один файл'
    LIST_FILE_ERROR_TXT = 'Для поля "Смета или список" необходимо прикрепить хотя бы один файл'
    LIST_TYPE_ERROR_TXT = f'Для поля "Смета или список" недопустимый тип файла - {LIST_FILE_WRONG_TYPE}'
    PHONE_ERROR_TXT = "Некорректный телефон"
    ERROR_MSG_BTN = (By.CSS_SELECTOR, "button.js-fb-msg-btnreject")

    SUCCESS_MSG_TXT_ACT = (By.CSS_SELECTOR, "div.js-fb-msg-text")
    SUCCESS_MSG_TXT_EXP = "Ваша заявка успешно отправлена!"
    SUCCESS_MSG_BTN = (By.CSS_SELECTOR, "button.js-fb-msg-btnsuccess")









