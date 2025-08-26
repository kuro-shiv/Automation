import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") #
driver.maximize_window()  # maximize the browser window
driver.implicitly_wait(10)  # wait for elements to be available

# find username and password fields
username = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
password = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")

time.sleep(2)
print("Login page opened successfully")
# type values
username.send_keys("Admin")
time.sleep(2)
password.send_keys("admin123")

#wait lets see
time.sleep(4)

# click login button
login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
login_btn.click()
time.sleep(4)

print("Login successful!")
driver.quit()
