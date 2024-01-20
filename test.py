from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

username_field = driver.find_element(By.XPATH, value='//*[@id="user-name"]')
username_field.send_keys('standard_user')

password_field = driver.find_element(By.XPATH, value='//*[@id="password"]')
password_field.send_keys('secret_sauce')

login_button = driver.find_element(by='name', value='login-button')
login_button.click()
time.sleep(10)

driver.get_screenshot_as_file('screen.png')

driver.quit()
