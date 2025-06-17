import pytest

from selenium import webdriver
from data import AuthDate
from pages.login_page import LoginPage
from pages.main_page import MainPage
from urls import BASE_URL


# Фикстура веб-драйвера Chrome
@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(BASE_URL)
    elif request.param == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--window-size=1200,600')
        driver = webdriver.Firefox(options=firefox_options)
        driver.get(BASE_URL)
    yield driver
    driver.quit()

# Фикстура для авторизации пользователя
@pytest.fixture
def login(driver):
    main_page = MainPage(driver)
    main_page.go_to_login_page_buttom_lk()
    login_page = LoginPage(driver)
    email = AuthDate.EMAIL
    password = AuthDate.PASSWORD
    login_page.user_authorization(email, password)

    yield
