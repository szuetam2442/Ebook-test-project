import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib import parse


class TestClass(object):

    @pytest.mark.parametrize(
        "ebook_path, file_lang, valid_link",
        [
            (
                    "cookbok-of-marketing-automation-in-ecommerce.htm", "files.salesmanago.pl",
                    "/Marek/ebook_en/cookbook-reguly-vital-en.pdf"),
            (
                    "philosophers.htm", "files.salesmanago.com",
                    "/media/great-philosophers.pdf")
        ]
    )
    def test_filling_demo_form(self, ebook_path, file_lang, valid_link):
        service = Service()
        service.start()
        driver = webdriver.Remote(service.service_url)
        driver.maximize_window()
        driver.get('https://www.salesmanago.com/info/knowledgecenter.htm')
        driver.implicitly_wait(3)
        ebook = driver.find_element(By.XPATH, '//a[contains(@href,"' + ebook_path + '")]')
        ebook.click()
        # original_window_handle = driver.current_window_handle
        all_window_handles = driver.window_handles
        new_window = all_window_handles[1]
        driver.switch_to.window(new_window)

        driver.implicitly_wait(3)

        name = driver.find_element(By.NAME, 'name')
        name.send_keys('Jan Kowalski')

        email = driver.find_element(By.NAME, 'email')
        # name = driver.find_element(By.XPATH,'//*[@id="email"]')
        email.send_keys('lwoypaeimnjjvtecdu@nthrl.com')

        company = driver.find_element(By.NAME, 'company')
        company.send_keys('Company')

        url = driver.find_element(By.NAME, 'url')
        url.send_keys('www.salesmanago.com')

        phoneDiallingCode = driver.find_element(By.NAME, 'phoneDiallingCode')
        phoneDiallingCode.clear()
        phoneDiallingCode.send_keys('+48')

        # sms gateway from website: https://online-sms.org/pl/free-phone-number-48796599710
        phoneNumber = driver.find_element(By.NAME, 'phoneNumber')
        phoneNumber.send_keys('796599710')

        submit = driver.find_element(By.XPATH, '//*[@type="submit" and not(contains(@class, "newsletter"))]')
        submit.click()

        html_element = driver.find_element(By.TAG_NAME, 'html')
        html_element.send_keys(Keys.HOME)

        download_btn = driver.find_element(By.LINK_TEXT, 'HERE')

        driver.implicitly_wait(5)

        # download_btn_link = download_btn.get_attribute('href')
        # print(download_btn_link)

        download_btn.click()

        all_window_handles = driver.window_handles
        new_window = all_window_handles[2]
        driver.switch_to.window(new_window)

        # pdb.set_trace()

        file_url = driver.current_url
        print(file_url)

        file_url2 = parse.urlparse(file_url)
        file_url3 = file_url2.netloc + file_url2.path
        print(file_url3)

        file_salesmanago_pl = file_lang
        philosophers_path = valid_link
        model = f'{file_salesmanago_pl}{philosophers_path}'

        def check_is_link_to_pdf_file(url: str):
            if model == url:
                return True
            else:
                return False

        test_1 = check_is_link_to_pdf_file(file_url3)
        assert test_1 is True, f'Url "{file_url}" after form submitting does not link to pdf file.'

        driver.quit()
