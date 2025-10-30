from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Create ChromeOptions instance
options = webdriver.ChromeOptions()

# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(options=options)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.find_element(By.LINK_TEXT,"Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Regis").click()

links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))

for link in links:
    print(link.text)