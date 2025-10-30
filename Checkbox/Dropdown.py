from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

# Create ChromeOptions instance
options = webdriver.ChromeOptions()


# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(50)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

country=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))

country.select_by_visible_text("India")
# country.select_by_value("10")
# country.select_by_index(4)

allcount=country.options
print(len(allcount))

for opt in allcount:
    print(opt.text)