from pages.login_page import LoginPage
from utils.config import BASE_URL, VALID_USER, VALID_PASS

def test_login_valid_credentials(driver):
    driver.get(BASE_URL)
    login = LoginPage(driver)

    login.enter_username(VALID_USER)
    login.enter_password(VALID_PASS)
    login.click_login()

    assert "dashboard" in driver.current_url
