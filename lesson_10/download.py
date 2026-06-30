import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
service = Service(executable_path=ChromeDriverManager().install())
options = Options()

# загрузка файла в директорию проекта
prefs = {
    "download.default_directory": f"{os.getcwd()}/downloads"
}
"""
Значение ключа задается через f-строку, чтобы автоматически объединить статическую часть пути (/downloads) с 
динамической текущей директорией проекта.
🔍 Почему это нужно?
os.getcwd() возвращает путь. Эта функция вычисляет место, где находится запущенный Python-скрипт (например, 
/Users/admin/project/main.py). Это может быть любой абсолютный путь у каждого пользователя или на каждом компьютере.
Нужно добавить папку downloads. Вы хотите скачивать файлы не в системную папку загрузок браузера (~/Downloads), а именно
в подпапку проекта, чтобы не засорять диск и легко находить результаты.
Сборка пути. Вам нужно превратить путь из os.getcwd() (например, /var/www/site) в итоговый строку 
/var/www/site/downloads.
"""
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://the-internet.herokuapp.com/download")
time.sleep(3)
driver.find_elements("xpath", "//a")[1].click()
time.sleep(3)
