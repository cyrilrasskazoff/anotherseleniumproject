from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://wikipedia.org")
driver.set_window_size(1440, 900)

# получение url страницы
url = driver.current_url
print(url) # https://www.wikipedia.org/

# получение title страницы
title = driver.title
print(title) # Wikipedia

# валидация данных + кастомное сообщение об ошибке
assert url == 'https://www.wikipedia.org/' and title == 'Wikipedia', 'Wrong url or title'

# получение исходного кода страницы: полученный html-код можно парсить с пом. спец. библиотек, проверять тэги, и т.д.
code = driver.page_source
print(code) # выведет исходный код страницы