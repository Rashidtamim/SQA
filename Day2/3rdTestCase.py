
from selenium.webdriver.chrome.service import Service


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


service = Service("C:\\Drivers\\chromedriver-win64\\chromedriver")
driver = webdriver.Chrome(service=service)


driver.get("https://demo.nopcommerce.com/")


register_link = driver.find_element(By.LINK_TEXT, "Register")
register_link.click()


first_name_input = driver.find_element(By.ID, "FirstName")
first_name_input.send_keys("YourFirstName")

last_name_input = driver.find_element(By.ID, "LastName")
last_name_input.send_keys("YourLastName")

email_input = driver.find_element(By.ID, "Email")
email_input.send_keys("email@example.com")

password_input = driver.find_element(By.ID, "Password")
password_input.send_keys("your_password")

confirm_password_input = driver.find_element(By.ID, "ConfirmPassword")
confirm_password_input.send_keys("your_password")

# Click on the "Register" button
register_button = driver.find_element(By.ID, "register-button")
register_button.click()


time.sleep(2)


try:
    confirmation_message = driver.find_element(By.CSS_SELECTOR, ".result").text
    assert "Your registration completed" in confirmation_message
    print("Registration successful!")
except:
    print("Registration failed or confirmation message not found.")


driver.quit()

