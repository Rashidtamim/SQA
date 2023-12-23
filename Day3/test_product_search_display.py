import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys


# Step 1: Navigate to the nopCommerce demo website and login
driver = webdriver.Chrome(executable_path="C:\\path\\to\\chromedriver.exe")
driver.get("https://demo.nopcommerce.com/")
# Implement the login steps according to your nopCommerce website

# Step 2: Add Product to the Shopping Cart
driver.find_element(By.CSS_SELECTOR, ".product-item .product-title a").click()
driver.find_element(By.NAME, "addtocart").click()

# Adding a delay to allow the cart to update (you might need to adjust this)
time.sleep(3)

# Step 3: Verify Product in Shopping Cart
driver.find_element(By.CSS_SELECTOR, ".cart-qty").click()
cart_product_name = driver.find_element(By.CSS_SELECTOR, ".product-name a").text
cart_product_quantity = driver.find_element(By.NAME, "itemquantity11215").get_attribute("value")
cart_product_price = driver.find_element(By.CSS_SELECTOR, ".product-unit-price").text

assert cart_product_name != "" and cart_product_quantity != "" and cart_product_price != "", "Product details not displayed correctly in the cart"

# Step 4: Update Product Quantity
driver.find_element(By.NAME, "itemquantity11215").clear()
driver.find_element(By.NAME, "itemquantity11215").send_keys("2")
driver.find_element(By.NAME, "updatecart").click()

# Adding a delay to allow the cart to update (you might need to adjust this)
time.sleep(3)

# Verify updated quantity and total price
updated_quantity = driver.find_element(By.NAME, "itemquantity11215").get_attribute("value")
total_price = driver.find_element(By.CSS_SELECTOR, ".product-total").text

assert updated_quantity == "2" and total_price != "", "Product quantity not updated correctly"

# Step 5: Remove Product from Shopping Cart
driver.find_element(By.NAME, "removefromcart").click()

# Adding a delay to allow the cart to update (you might need to adjust this)
time.sleep(3)

# Verify product removal
assert "Your Shopping Cart is empty!" in driver.page_source, "Product removal failed"

# Step 6: Continue Shopping
driver.find_element(By.CSS_SELECTOR, ".header-logo a").click()

# Closing the browser
driver.quit()



