from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://freeconferencecall.com/login")
driver.set_window_size(1440, 900)
print(type(driver.find_element("id", "loginformsubmit")))  # <class 'selenium.webdriver.remote.webelement.WebElement'>
driver.find_element("id", "loginformsubmit").click()

