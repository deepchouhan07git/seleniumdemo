from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import XLUtils

serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//*[@id='wzrk-cancel']").click()

file="C:\\Users\\user\\Downloads\\Book1.xlsx"
row=XLUtils.getRowCount(file, "Data")

# Read data from the sheet
for r in range(2, row+1):
    princ=XLUtils.readData(file, "Data", r, 1)
    roi=XLUtils.readData(file, "Data", r, 2)
    tp1=XLUtils.readData(file, "Data", r, 3)
    tp2=XLUtils.readData(file, "Data", r, 4)
    freq=XLUtils.readData(file, "Data", r, 5)
    exp=XLUtils.readData(file, "Data", r, 6)

# Put the data into the application
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(princ)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(roi)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(tp1)

    prddrp=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    prddrp.select_by_visible_text(tp2)

    freqdrp=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    freqdrp.select_by_visible_text(freq)
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]").click()
    act_value=driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text

# Validation
    if float(exp)==float(act_value):
        print("Test passed")
        XLUtils.writeData(file, "Data", r,8,"Passed")
        XLUtils.fillGreencolor(file,"Data",r,8)
    else:
        print("Test failed")
        XLUtils.writeData(file, "Data", r, 8, "Failed")
        XLUtils.fillRedcolor(file, "Data", r, 8)

    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]").click()
    time.sleep(5)


driver.close()