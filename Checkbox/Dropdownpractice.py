from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

# Create ChromeOptions instance
options = webdriver.ChromeOptions()


# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

country=Select(driver.find_element(By.XPATH,"//select[@id='country']"))

allcount=country.options
print(len(allcount))

# country.select_by_value("canada")
# country.select_by_index(3)
# country.select_by_visible_text("India")


# Select India from dropdown without builtin method
for opt in allcount:
    if opt.text=="India":
        opt.click()
        break

