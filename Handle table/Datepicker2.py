from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

# Create ChromeOptions instance
serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,"//input[@id='dob']").click()

monthpicker=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
monthpicker.select_by_visible_text("Dec")

yearpicker=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
yearpicker.select_by_visible_text("2020")

alldates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in alldates:
    if date.text=="20":
        date.click()
        break