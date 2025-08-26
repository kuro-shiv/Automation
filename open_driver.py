from selenium import webdriver

# launch browser (make sure chromedriver is installed)
driver = webdriver.Chrome()

# open Google
driver.get("https://www.google.com")

# print the page title
print("Title of the page is:", driver.title)


# close browser
driver.quit()
