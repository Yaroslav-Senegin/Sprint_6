from conftest import driver
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
from utils.test_data import YaScooterOrderHeaderBtn, YaScooterOrderMainBtn
import allure


class TestOrderPage:
    @allure.title('Проверка оформления заказа через кнопку "Заказать" в шапке главной страницы')
    def test_create_order_header_btn(self, driver):
        HomePage(driver).get_cookies(HomePageLocators.COOKIES_BTN)
        OrderPage(driver).click_header_order_btn()
        OrderPage(driver).create_order(YaScooterOrderHeaderBtn.first_name,
                                       YaScooterOrderHeaderBtn.last_name,
                                       YaScooterOrderHeaderBtn.address,
                                       OrderPageLocators.STATION_1,
                                       YaScooterOrderHeaderBtn.phone,
                                       OrderPageLocators.DATE_1,
                                       OrderPageLocators.TERM_1,
                                       OrderPageLocators.BLACK_COLOR,
                                       YaScooterOrderHeaderBtn.comment)
        text = OrderPage(driver).check_success_order()
        assert 'Заказ оформлен' in text

    @allure.title('Проверка оформления заказа через кнопку "Заказать" в середине главной страницы')
    def test_create_order_main_page_btn(self, driver):
        HomePage(driver).get_cookies(HomePageLocators.COOKIES_BTN)
        OrderPage(driver).click_main_order_btn()
        OrderPage(driver).create_order(YaScooterOrderMainBtn.first_name,
                                       YaScooterOrderMainBtn.last_name,
                                       YaScooterOrderMainBtn.address,
                                       OrderPageLocators.STATION_2,
                                       YaScooterOrderMainBtn.phone,
                                       OrderPageLocators.DATE_2,
                                       OrderPageLocators.TERM_2,
                                       OrderPageLocators.GREY_COLOR,
                                       YaScooterOrderMainBtn.comment)
        text = OrderPage(driver).check_success_order()
        assert 'Заказ оформлен' in text