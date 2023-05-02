from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# класс Service - появился в версии selenium4 - отвечает за установку/открытие/закрытие драйвера
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install()) # создадим объект класса Service
driver = webdriver.Chrome(service=service)