from selenium.webdriver.common.by import By


class KnowledgeCenterLocator:
    KNOWLEDGE_CENTER_LINK = '/info/knowledgecenter.htm'
    # EBOOK_PARAMETRIZED = (By.XPATH, '//a[contains(@href,"{}")]')

    @staticmethod
    def build_ebook_param(ebook_path):
        ebook_parametrized = (By.XPATH, '//a[contains(@href,"{}")]'.format(ebook_path))
        return ebook_parametrized
