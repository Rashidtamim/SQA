import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductSearchTest(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.driver = None

    def setUp(self):
        # Set up the WebDriver with the full path to the ChromeDriver executable
        service = ChromeService("C:\\Drivers\\chromedriver-win64\\chromedriver")
        self.driver = webdriver.Chrome(service=service)

        # Navigate to the nopCommerce demo website
        self.driver.get("https://demo.nopcommerce.com/")

    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

    def test_product_search(self):
        # Test the product search functionality
        search_box = self.driver.find_element_by_name("q")
        search_box.send_keys("laptop")
        search_box.send_keys(Keys.RETURN)

        # Verify that search results are displayed
        results = self.driver.find_elements_by_css_selector(".product-item")
        self.assertGreater(len(results), 0, "No search results found")

        # Check product details on the first search result
        first_result = results[0]
        product_name = first_result.find_element_by_css_selector(".product-title a").text
        product_price = first_result.find_element_by_css_selector(".price").text

        # Verify that product details are correctly displayed
        self.assertNotEqual(product_name, "", "Product name is empty")
        self.assertNotEqual(product_price, "", "Product price is empty")

        # Click on the first search result to view the product page
        first_result.find_element_by_css_selector(".product-title a").click()

        # Verify that the product page displays the correct product information
        product_page_name = self.driver.find_element_by_css_selector(".product-name").text

        # Extract the product price from the product page
        product_page_price_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".price"))
        )
        product_page_price = product_page_price_element.text

        self.assertEqual(product_page_name, product_name, "Product name mismatch on product page")

        # Verify that the product image is clickable
        product_image = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-image img"))
        )
        product_image.click()

        # Verify that the product price on the product page matches the expected price
        self.assertEqual(product_page_price, product_price, "Product price mismatch on product page")

if __name__ == "__main__":
    unittest.main()



