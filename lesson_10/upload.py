import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
# загрузка файла осуществляется через тэг input у которого type = "file", он может быть скрыт, поэтому нужно искать
# этот элемент на странице
driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(3)
choose_file_btn = driver.find_element("xpath", "//input[@id='file-upload']")
choose_file_btn.send_keys(f"{os.getcwd()}/downloads/Student.json")
time.sleep(3)