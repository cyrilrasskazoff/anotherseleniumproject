import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
import pickle

service = Service(executable_path=ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.freeconferencecall.com/global/pl")

# получение конкретной cookie по имени: результатом будет словарь
print(driver.get_cookie("country_code")) # {'domain': 'www.freeconferencecall.com', 'httpOnly': True,
# 'name': 'country_code', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'pl'}

# получение всех cookies: результатом будет список словарей
print(driver.get_cookies())

# добавление кастомной cookie
driver.add_cookie({
    "name": "testName",
    "value": "testValue"
})

time.sleep(2)
print(driver.get_cookie("testName")) # {'domain': 'www.freeconferencecall.com', 'httpOnly': False,
# 'name': 'testName', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'testValue'}

# замена суествующей cookie:
driver.delete_cookie("testName")
driver.add_cookie({
    "name": "testName",
    "value": "testValueUpdate"
})
print(driver.get_cookie("testName")) # {'domain': 'www.freeconferencecall.com', 'httpOnly': False,
# 'name': 'testName', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'testValueUpdate'}

# удаление всех cookies
driver.delete_all_cookies()
print(driver.get_cookies()) # []

# ********************************************
# работа с pickle
# пример: мы заходим на сайт -> логинимся -> получаем все куки (в том числе сессионные с авторизацией) -> сохраняем их
# в файл. После этого можно пропускать процесс логина просто подгружая сохраненные куки из файла

driver.get("https://www.freeconferencecall.com/global/pl")
# ...тут мы должны выполнить логин...

# сохраним все cookies в файл .pkl (его нужно предварительно создать)
pickle.dump(driver.get_cookies(), open(os.getcwd()+"/cookies/cookies.pkl", "wb"))

# снова заходим на сайт, но уже без логина -> удаляем все куки -> подгружаем куки из файла -> рефрешим страницу -
# мы залогинены
driver.get("https://www.freeconferencecall.com/global/pl")
driver.delete_all_cookies()
cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()
print(driver.get_cookies())








