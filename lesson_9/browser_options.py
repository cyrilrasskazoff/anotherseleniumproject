from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
service = Service(executable_path=ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--ignore-certificate-errors") # запуск браузера с игнорированием ошибок сертификата,
# например отсутствие ssl и т.д.
chrome_options.add_argument("--window-size=1920,1080")
# chrome_options.add_argument("--disable-cache")

driver = webdriver.Chrome(service=service, options=chrome_options)

# стратегия загрузки страницы: none, normal (дефолтная, ждет загрузки всех элементов страницы - картинок, JS скриптов
# и тд), eager (ждет загрузки только DOM)
# chrome_options.page_load_strategy = "normal"
chrome_options.page_load_strategy = "eager"

start_time = time.time()

driver.get("https://whatismyipaddress.com/")

end_time = time.time()
load_time = end_time - start_time
print(load_time)
# time.sleep(3)

