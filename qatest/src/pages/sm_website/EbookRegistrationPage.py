# uzupełnainie danyc fill form,
from typing import Tuple
from urllib import parse

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from qatest.src.SeleniumExtended import SeleniumExtended
from qatest.src.locators.sm_website.EbookRegistrationPageLocator import EbookRegistrationPageLocator


class EbookRegistrationPage(EbookRegistrationPageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def change_page(self, page_number: int):
        all_window_handles = self.driver.window_handles
        new_window = all_window_handles[page_number]
        self.driver.switch_to.window(new_window)

    def fill_form(
            self,
            name: str = None,
            email: str = None,
            company: str = None,
            web_url: str = None,
            phone: Tuple[str, str] = (None, None),
            **kwargs,
    ):
        if name:
            self.enter_name_and_surname(name)
        if email:
            self.enter_email(email)
        if company:
            self.enter_company(company)
        if web_url:
            self.enter_website_url(web_url)
        if phone is not (None, None):
            country_code, phone_num = phone
            self.enter_country_phone_prefix(country_code)
            self.enter_phone_number(phone_num)

    # methods for fill form
    def enter_name_and_surname(self, name_and_surname: str):
        self.sl.wait_and_enter_text(name_and_surname, self.NAME)

    def enter_email(self, email: str):
        self.sl.wait_and_enter_text(email, self.EMAIL)

    def enter_company(self, company_name: str):
        self.sl.wait_and_enter_text(company_name, self.COMPANY)

    def enter_country_phone_prefix(self, country_code: str):
        self.sl.wait_and_enter_text(country_code, self.PHONE_DIALLING_CODE)

    def enter_phone_number(self, phone_number: str):
        self.sl.wait_and_enter_text(phone_number, self.PHONE_NUMBER)

    def enter_website_url(self, web_url: str):
        self.sl.wait_and_enter_text(web_url, self.URL)

    # other page methods
    def click_on_submit_btn(self):
        self.sl.wait_and_click(self.SUBMIT_BTN)

    def scroll_to_top(self):
        keys = Keys.HOME
        self.sl.wait_and_send_keys(keys, self.HTML_ELEMENT)

    def click_on_download_btn(self):
        self.sl.wait_and_click(self.DOWNLOAD_BTN)

    # methods for validation

    def get_url_for_validation(self):
        file_url = parse.urlparse(self.driver.current_url)
        return file_url.netloc + file_url.path

    def build_parametrized_link_for_validation(self, file_lang, valid_link):
        return f'{file_lang}{valid_link}'

    def check_is_link_to_pdf_file(self, validation_link: str, file_url: str):
        if validation_link == file_url:
            return True
        else:
            return False

    def quit_driver(self):
        self.driver.quit()
