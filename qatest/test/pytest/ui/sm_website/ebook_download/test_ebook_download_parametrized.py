import pytest

from qatest.src.pages.sm_website.EbookRegistrationPage import EbookRegistrationPage
from qatest.src.pages.sm_website.KnowledgeCenterPage import KnowledgeCenterPage
from qatest.test.pytest.ui.sm_website.common import RegistrationFormDataBasicGenerator


@pytest.mark.usefixtures("init_driver")
class TestClass:

    # def setUp(self):
    #     self.generated_data = RegistrationFormDataBasicGenerator.get_random()

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

        kc_page = KnowledgeCenterPage(self.driver)
        kc_page.go_to_knowledge_center_page()
        kc_page.click_on_selected_ebook_link(ebook_path)

        registration_page = EbookRegistrationPage(self.driver)
        registration_page.change_page(1)
        self.generated_data = RegistrationFormDataBasicGenerator.get_random()
        registration_page.fill_form(**self.generated_data.to_dict())
        registration_page.click_on_submit_btn()
        registration_page.scroll_to_top()
        registration_page.click_on_download_btn()
        registration_page.change_page(2)

        # TO REFACTOR
        validation_link = registration_page.build_parametrized_link_for_validation(file_lang,valid_link)
        file_url = registration_page.get_url_for_validation()
        valid_file_bool = registration_page.check_is_link_to_pdf_file(validation_link, file_url)
        registration_page.quit_driver()
        assert valid_file_bool is True, f'Url "{file_url}" after form submitting does not link to pdf file.'








