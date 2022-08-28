from qatest.src.locators.sm_website.KnowledgeCenterLocator import KnowledgeCenterLocator
from qatest.src.SeleniumExtended import SeleniumExtended
from qatest.src.helpers.config_helpers import get_base_url


class KnowledgeCenterPage(KnowledgeCenterLocator):

    endpoint = KnowledgeCenterLocator.KNOWLEDGE_CENTER_LINK

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_knowledge_center_page(self):
        base_url = get_base_url()
        my_base_url = base_url + self.endpoint
        self.driver.get(my_base_url)

    def click_on_selected_ebook_link(self, ebook_path):
        self.sl.wait_and_click(self.build_ebook_param(ebook_path))

        # self.driver.find_element(By.XPATH, '//a[contains(@href,"' + ebook_path + '")]')
