from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("C:\\Drivers\\chromedriver-win64\\chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://admin-demo.nopcommerce.com/login")


driver.find_element(By.NAME, "Email").clear()
driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")


driver.find_element(By.NAME, "Password").clear()
driver.find_element(By.NAME, "Password").send_keys("admin")


# Use find_element_by_css_selector to locate the element by its class names
driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()

act_title = driver.title
exp_title = "Dashboard / nopCommerce administration"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()