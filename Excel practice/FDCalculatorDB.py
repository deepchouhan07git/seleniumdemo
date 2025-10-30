from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import mysql.connector

serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//*[@id='wzrk-cancel']").click()

try:
    con=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="123@123Dc",database="mydb")
    curs=con.cursor()  # create cursor
    curs.execute("select * from caldata")

    for row in curs:  # Read data from the sheet
        princ = row[0]
        roi = row[1]
        tp1 = row[2]
        tp2 = row[3]
        freq = row[4]
        exp = row[5]

        # Put the data into the application
        driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(princ)
        driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(roi)
        driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(tp1)

        prddrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
        prddrp.select_by_visible_text(tp2)

        freqdrp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
        freqdrp.select_by_visible_text(freq)
        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]").click()
        act_value = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

        # Validation
        if float(exp) == float(act_value):
            print("Test passed")
        else:
            print("Test failed")

        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]").click()
        time.sleep(5)
    con.close()

except:
    print("connection unsuccessfull.....")

driver.close()