from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-blink-features=AutomationControlled") # отключение WebDriver-мода =
# скроет от сайта тот факт, что браузер контролируется Веб Драйвером. Это не всегда помогает,особеннов в случае работы в
# headless mode, поэтому используем следующую опцию:
chrome_options.add_argument("user-agent=insert any legit user agent here")

driver = webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(driver, 15, poll_frequency=1)

# make a screenshot
driver.get("https://dzen.ru")
driver.save_screenshot("screen.png")

# ресурс ниже распознает, кем контролируется браузер (автоматика либо человек): чтобы увидеть разницу - закоментить,
# раскоментить chrome_options.add_argument("--disable-blink-features=AutomationControlled"). Этот же ресурс позволяет
# увидеть user agent. Список валидных user agent-ов можно взять тут: https://www.useragents.me/
driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
time.sleep(5)