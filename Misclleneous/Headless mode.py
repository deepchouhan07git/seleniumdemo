from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
    ops=webdriver.ChromeOptions()
    ops.headless=True
    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver

def headless_edge():
    from selenium.webdriver.edge.service import Service
    serv_obj=Service(r"C:\Drivers\edgedriver_win64\msedgedriver.exe")
    ops=webdriver.EdgeOptions()
    ops.headless=True
    driver = webdriver.Edge(service=serv_obj,options=ops)
    return driver

#driver=headless_chrome()
driver=headless_edge()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)