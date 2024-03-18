import pytest
from selenium import webdriver
from utils.urls import Urls


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.HOME_PAGE)
    
    yield driver
    driver.quit()
