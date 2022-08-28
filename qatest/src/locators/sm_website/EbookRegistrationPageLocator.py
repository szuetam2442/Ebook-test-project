from selenium.webdriver.common.by import By


class EbookRegistrationPageLocator:
    NAME = (By.NAME, 'name')
    EMAIL = (By.NAME, 'email')
    COMPANY = (By.NAME, 'company')
    URL = (By.NAME, 'url')
    PHONE_DIALLING_CODE = (By.NAME, 'phoneDiallingCode')
    PHONE_NUMBER = (By.NAME, 'phoneNumber')
    SUBMIT_BTN = (By.XPATH, '//*[@type="submit" and not(contains(@class, "newsletter"))]')
    HTML_ELEMENT = (By.TAG_NAME, 'html')
    DOWNLOAD_BTN = (By.LINK_TEXT, 'HERE')
