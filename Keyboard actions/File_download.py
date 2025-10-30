from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj=Service(r"C:\Drivers\edgedriver_win64\msedgedriver.exe")
    driver = webdriver.Edge(service=serv_obj)
    return driver

driver=edge_setup()



driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()




