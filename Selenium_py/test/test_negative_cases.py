from pages.login_page import LoginPage
from utils.config import BASE_URL, INVALID_USER, INVALID_PASS

def test_login_invalid_credentials(driver):
    driver.get(BASE_URL)
    login = LoginPage(driver)

    login.enter_username(INVALID_USER)
    login.enter_password(INVALID_PASS)
    login.click_login()

    assert "Invalid credentials" in login.get_error()


def test_login_empty_fields(driver):
    driver.get(BASE_URL)
    login = LoginPage(driver)

    login.click_login()
    assert "required" in login.get_error()
