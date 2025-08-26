from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.maximize_window()
driver.implicitly_wait(10)

time.sleep(4)

# Fill form fields
driver.find_element(By.NAME, "my-text").send_keys("John Doe")
time.sleep(2)
driver.find_element(By.NAME, "my-password").send_keys("SecurePass123")
time.sleep(2)
driver.find_element(By.NAME, "my-textarea").send_keys("Hello, this is a test!")
time.sleep(2)

# Click submit
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(5)
print("Form submitted successfully!")
driver.quit()
