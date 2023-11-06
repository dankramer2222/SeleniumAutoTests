import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.form_page_locators import  FormPageLocators as Locators


class FormPage(BasePage):

    def fill_fields_and_submit(self):
        first_name = "Danila"
        last_name = "Kramer"
        email = "KramerIndustry@gmail.com"

        self.remove_footer()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.GENDER).click()
        self.element_is_visible(Locators.MOBILE).send_keys("8800553535")

        subject = self.element_is_visible(Locators.SUBJECT)
        subject.send_keys('English')
        subject.send_keys(Keys.RETURN)

        self.element_is_visible(Locators.FILE_INPUT).send_keys(
            r'C:\Users\danil\OneDrive\Документы\PycharmPythonLabs\pythonProject5\test.txt')
        self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys("City,123,Usa")
        self.element_is_visible(Locators.SUBMIT).click()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="alert alert-success"]'))
            )
        except TimeoutException as e:
            print(f"Timeout Exception: {e}")

        return first_name, last_name, email

    def form_result(self):
        result_list = self.elements_are_visible(Locators.RESULT_TABLE)  # Используйте метод elements_are_visible
        result_text = []
        for element in result_list:
            result_text.append(element.text)
        return result_text

