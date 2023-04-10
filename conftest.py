import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

url = 'https://qa-scooter.praktikum-services.ru/'


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--window-size=1200,600')

    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser.get(url)

    yield browser
    browser.quit()
