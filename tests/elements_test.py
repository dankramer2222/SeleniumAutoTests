
from selenium import webdriver

from pages.elements_page import TextBoxPage, CheckBoxPage


class TestElements:
    def setup_method(self):
        self.driver = webdriver.Chrome()

    def test_text_box(self):
        text_box_page = TextBoxPage(self.driver, 'https://demoqa.com/text-box')
        text_box_page.open()
        text_box_page.fill_all_fields(self.driver)  # Добавлен аргумент self.driver

        # we can actually make it lot easier input_data = text_box_page.check_filled_form()
        full_name, email, current_address, permanent_address = text_box_page.check_filled_form()
        # same as here output_data = text_box_page.check_filled_form()
        output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()

        # but I think if it will be more elements and even one bug going to happen assert will work better (easier to
        # understand what happened)
        assert full_name == output_name, "The full name doesn't match"
        assert email == output_email, "The email doesn't match"
        assert current_address == output_cur_addr, "The current address doesn't match"
        assert permanent_address == output_per_addr, "The permanent address doesn't match"

    class TestCheckBox:
        def test_check_box(self,driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()

