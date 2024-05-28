from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/global/pl")
login_btn = driver.find_element("xpath", "//a[@id='login-desktop']")
login_btn.click()
email_field = driver.find_element("xpath", "//input[@id='login_email']")
email_field.send_keys("test@test.com")

# чтобы получить значение введенных данных в текстовое поле, используеся отрибут value
print(email_field.get_attribute("value")) # test@test.com

# чтобы очистить поле ввода, используем метод clear()
email_field.clear()
print(f"new email: ", email_field.get_attribute("value")) # new email:
time.sleep(5)
