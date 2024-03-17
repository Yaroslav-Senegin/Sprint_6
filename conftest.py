import pytest
from selenium import webdriver
from utils.urls import Urls


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(Urls.MAIN_PAGE)
    
    yield driver
    driver.quit()
