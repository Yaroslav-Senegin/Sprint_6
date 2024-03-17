from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from conftest import driver
from utils.urls import Urls
import allure


class TestHeaderLogo:
    @allure.title('Клик на лого Самоката в шапке возвращает на главную страницу')
    def test_redirect_samokat_logo(self, driver):
        HomePage(driver).click_to_element(HomePageLocators.ORDER_BTN_HEADER)
        HomePage(driver).click_samokat_logo()
        HomePage(driver).wait_navigating_url(Urls.HOME_PAGE)
        assert driver.current_url == Urls.HOME_PAGE

    @allure.title('Проверка редиректа на Dzen.ru при клике на Яндекс в лого шапки')
    def test_redirect_yandex_logo(self, driver):
        HomePage(driver).click_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])
        HomePage(driver).wait_navigating_url(Urls.ZEN_HOME_PAGE)
        assert driver.current_url == Urls.ZEN_HOME_PAGE