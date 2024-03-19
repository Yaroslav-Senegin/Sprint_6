from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from conftest import driver
from utils.test_data import YaScooterHomePageFAQ
import pytest
import allure


class TestQuestionsHomePage:
    @allure.title('Проверка ответов на вопросы из выпадающего списка «Вопросы о важном»')
    @pytest.mark.parametrize('number, expected_answer', YaScooterHomePageFAQ.answers)
    def test_question(self, driver, number, expected_answer):
        hp = HomePage(driver)
        hp.get_cookies(HomePageLocators.COOKIES_BTN)
        hp.scroll(HomePageLocators.LAST_QUESTION)
        hp.click_question(number)
        answer = hp.get_answer(number)
        assert answer == expected_answer