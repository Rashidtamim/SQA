from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("C:\\Drivers\\chromedriver-win64\\chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/")

# Use WebDriverWait to wait for the element to be present
wait = WebDriverWait(driver, 10)
username_element = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username_element.send_keys("Admin")

driver.find_element(By.NAME, "password").send_keys("admin123")

# Use find_element_by_css_selector to locate the element by its class names
driver.find_element_by_css_selector(".oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()


