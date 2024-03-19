from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
import allure

class HomePage(BasePage):
    @allure.step('Клик на вопрос')
    def click_question(self, number):
        method, locator = HomePageLocators.QUESTION
        locator = locator.format(number)
        self.find_element((method, locator))
        return self.click_to_element((method, locator))

    @allure.step('Получение ответа')
    def get_answer(self, number):
        method, locator = HomePageLocators.ANSWER
        locator = locator.format(number)
        self.find_element((method, locator))
        return self.get_text((method, locator))

    @allure.step('Клик на Яндекс в шапке')
    def click_yandex_logo(self):
        self.click_to_element(HomePageLocators.YANDEX_LOGO)

    @allure.step('Клик на Самокат в шапке')
    def click_samokat_logo(self):
        self.click_to_element(HomePageLocators.SAMOKAT_LOGO)
