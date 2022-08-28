import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def init_driver(request):
    # add more browsers in future
    # supported_browsers = ['chrome']

    service = Service()
    service.start()

    driver = webdriver.Remote(service.service_url)
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.quit()
