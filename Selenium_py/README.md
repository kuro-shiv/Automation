# 🧪 Selenium Python Automation Framework - Learning & Practice

**Personal Learning Project:** I'm learning and practicing test automation using Selenium WebDriver with Python. This framework demonstrates modern testing practices, design patterns, and automation best practices.

---

A comprehensive, educational Selenium WebDriver-based test automation framework with Page Object Model pattern, built with Python and pytest.

## 📋 Overview

This framework provides a robust structure for automating web application testing using:
- **Selenium WebDriver** - Web automation library
- **pytest** - Testing framework
- **Page Object Model** - Design pattern for maintainable tests
- **webdriver-manager** - Automatic browser driver management

## 🎯 Key Features

✅ **Page Object Model** - Maintainable and scalable test architecture  
✅ **Reusable Components** - Base test class, utilities, and configurations  
✅ **Multiple Test Suites** - Login, dashboard, and negative test cases  
✅ **Browser Compatibility** - Support for Chrome, Firefox, Edge, Safari  
✅ **Screenshots & Logging** - Automatic failure screenshots and detailed logs  
✅ **Easy Configuration** - Centralized config file for URLs and credentials  
✅ **WebDriver Management** - Automatic driver download and management  

## ✅ Requirements

- Python 3.8+
- pip
- Selenium
- Browser WebDrivers (ChromeDriver, EdgeDriver, etc.)
- VS Code (optional but recommended)

### Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- **Selenium** - Web automation library
- **pytest** - Testing framework
- **webdriver-manager** - Automatic WebDriver management

---

## 🏗️ Project Structure

```
Selenium_py/
├── pages/
│   └── login_page.py          # Page Object Model for login page
├── test/
│   ├── test_login.py          # Login functionality tests
│   ├── test_dashboard.py       # Dashboard tests
│   └── test_negative_cases.py  # Negative scenario tests
├── utils/
│   ├── base_test.py           # Base test class with setup/teardown
│   └── config.py              # Configuration and constants
├── requirements.txt           # Python dependencies
├── run_tests.py               # Main test runner script
└── README.md                  # This file
```

---

## ▶️ Running Tests

### Run All Tests
```bash
python run_tests.py
```

### Run Tests with Pytest
```bash
pytest test/ -v
```

### Run Specific Test File
```bash
pytest test/test_login.py -v
```

### Run Specific Test Case
```bash
pytest test/test_login.py::TestLogin::test_valid_login -v
```

### Run Tests with Output
```bash
pytest test/ -v -s
```

---

## 📁 Directory Details

### `pages/`
**Page Object Model (POM) Classes** - Contains page classes that represent UI elements and actions.

**Example:**
```python
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)
    
    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()
```

**Files:**
- `login_page.py` - Login page elements and methods

### `test/`
**Test Cases** - Contains all test scenarios.

**Files:**
- `test_login.py` - Login functionality tests (valid credentials, UI elements)
- `test_dashboard.py` - Dashboard tests after successful login
- `test_negative_cases.py` - Negative scenarios (invalid login, error handling)

### `utils/`
**Utility Functions & Configuration** - Helper classes and settings.

**Files:**
- `base_test.py` - Base test class with WebDriver initialization and teardown
- `config.py` - Test configuration, URLs, credentials, and constants

---

## 🧪 Test Scenarios Covered

### Login Tests (`test_login.py`)
- ✅ Valid login with correct credentials
- ✅ Verify login page elements
- ✅ Navigate to login page
- ✅ Check page title and URL

### Dashboard Tests (`test_dashboard.py`)
- ✅ Dashboard loads after login
- ✅ Verify dashboard elements
- ✅ Navigation functionality
- ✅ User session management

### Negative Cases (`test_negative_cases.py`)
- ✅ Login with invalid credentials
- ✅ Error message validation
- ✅ Empty field handling
- ✅ Edge case scenarios

---

## 🔧 Configuration

Edit `utils/config.py` to customize:
- Base URL
- Browser type
- Test credentials
- Timeouts
- Wait times

**Example:**
```python
BASE_URL = "https://opensource-demo.orangehrmlive.com/"
BROWSER = "chrome"
USERNAME = "Admin"
PASSWORD = "admin123"
IMPLICIT_WAIT = 10
```

---

## 🌐 Testing Websites

We use the following websites for practice and testing:

- 🔹 [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)
- 🔹 [SauceDemo](https://www.saucedemo.com/)
- 🔹 [The Internet (Heroku)](https://the-internet.herokuapp.com/)
- 🔹 [Selenium Practice Form](https://www.selenium.dev/selenium/web/web-form.html)
- 🔹 [FormSite Practice](https://fs2.formsite.com/meherpavan/form2/)

These sites cover:
- Login and authentication testing
- Form handling and validation
- Element interaction (click, type, submit)
- Alerts, popups, and iFrames
- File uploads and downloads

---

## 📸 Screenshots & Logging

### Screenshots
Automatic screenshots on test failure:
```python
driver.save_screenshot('screenshot.png')
```

Screenshots are saved to the project directory.

### Logging
Python logging is configured in `base_test.py`:
```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

Use logging in tests:
```python
logger.info("Starting login test")
logger.error("Login failed")
```

---

## 🔄 Test Execution Flow

1. **Setup** - Initialize WebDriver and navigate to base URL
2. **Test Execution** - Execute test steps using Page Object methods
3. **Assertion** - Verify expected results
4. **Teardown** - Close browser and cleanup

Example:
```python
def test_valid_login(self):
    login_page = LoginPage(self.driver)
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    
    dashboard = DashboardPage(self.driver)
    assert dashboard.is_dashboard_loaded()
```

---

## 🐛 Debugging Tips

1. **Use `time.sleep()`** for manual waits (not recommended for production):
   ```python
   import time
   time.sleep(2)
   ```

2. **Use Explicit Waits** (recommended):
   ```python
   from selenium.webdriver.support.ui import WebDriverWait
   WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
   ```

3. **Take Screenshots**:
   ```python
   driver.save_screenshot('debug.png')
   ```

4. **Print Page Source**:
   ```python
   print(driver.page_source)
   ```

5. **Check WebDriver Logs**:
   ```python
   logs = driver.get_log('browser')
   ```

---

## ✅ Best Practices

- ✅ Use Page Object Model pattern
- ✅ Avoid hardcoding values (use config.py)
- ✅ Use explicit waits instead of implicit waits
- ✅ Follow naming conventions for test methods
- ✅ Keep tests independent and reusable
- ✅ Log important test steps
- ✅ Take screenshots on failures
- ✅ Clean up resources in teardown

---

## 📚 Resources

- [Selenium Python Documentation](https://www.selenium.dev/selenium/docs/api/py/)
- [Pytest Documentation](https://docs.pytest.org/)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)
- [Selenium Best Practices](https://www.selenium.dev/documentation/)

---

## 🎓 Learning Path

1. Start with `utils/config.py` to understand configuration
2. Review `utils/base_test.py` for WebDriver setup
3. Check `pages/login_page.py` for Page Object pattern
4. Study test files in `test/` folder
5. Run tests and observe the execution

---

## 🤝 Contributing

Contributions are welcome! Please:
- Follow the Page Object Model pattern
- Write clear test names
- Add comments for complex logic
- Ensure all tests pass
- Update this README if adding new features

---

## 📄 License

ISC License

---

**Happy Selenium Testing! 🎉**
