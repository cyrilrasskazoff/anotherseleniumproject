import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
service = Service(executable_path=ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()

# загрузка файла в директорию проекта
download_prefs = {
    "download.default_directory": f"{os.getcwd()}/downloads"
}
chrome_options.add_experimental_option("prefs", download_prefs)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/download")
time.sleep(3)
driver.find_elements("xpath", "//a")[1].click()
time.sleep(3)
