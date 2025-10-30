from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Create ChromeOptions instance
options = webdriver.ChromeOptions()

# Initialize WebDriver without passing the executable path
driver = webdriver.Chrome(options=options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1 Count total no. of rows and columns

NoOfRows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
NoOfColumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/th"))

print(NoOfRows) #7
print(NoOfColumns) #4

#2 Read specific row and column data

# data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[4]/td[3]").text
# print(data) # Javascript

#3 Read all the column and row data

# for r in range(2,NoOfRows+1):
#     for c in range(1,NoOfColumns+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data,end=" ")
#     print()

#4 Read data based on condition

for r in range(2,NoOfRows+1):
    authorname=driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[2]").text
    if authorname=="Mukesh":
        bookname=driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[1]").text
        print(bookname,"  ",authorname)

