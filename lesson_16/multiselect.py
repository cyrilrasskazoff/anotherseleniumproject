from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
import time

service = Service(executable_path=ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=service, options=chrome_options)

# современная разработка не использует 'select' в дропдаунах - используется оычный 'div'
# первый способ работы с такими дропдаунами (с помощью инпута):

SELECT_LOCATOR = ("xpath", "//input[@id='react-select-3-input']")
driver.get("https://demoqa.com/select-menu")

driver.find_element(*SELECT_LOCATOR).send_keys("Ms.")
driver.find_element(*SELECT_LOCATOR).send_keys(Keys.ENTER)
time.sleep(2)

# второй способ работы с такими дропдаунами (с помощью скрипта):
# видео по инспектированию исчезающих элементов: https://www.youtube.com/watch?v=ZgmJmgelZOM&t=58s
# JS скрипт для работы с исчезающими элементами: setTimeout(function() { debugger; }, 5000);

SELECT_DROPDOWN = ("xpath", "//div[@id='selectOne']")
PROF_OPTION = ("xpath", "//div[text()='Prof.']")

driver.get("https://demoqa.com/select-menu")
driver.find_element(*SELECT_DROPDOWN).click()
time.sleep(2)
driver.find_element(*PROF_OPTION).click()
time.sleep(2)

# мультиселект
MULTI_SEL_LOCATOR = ("xpath", "//input[@id='react-select-4-input']")

driver.get("https://demoqa.com/select-menu")
time.sleep(2)
driver.find_element(*MULTI_SEL_LOCATOR).send_keys("Green")
driver.find_element(*MULTI_SEL_LOCATOR).send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(*MULTI_SEL_LOCATOR).send_keys("Red")
driver.find_element(*MULTI_SEL_LOCATOR).send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(*MULTI_SEL_LOCATOR).send_keys("Bla")
driver.find_element(*MULTI_SEL_LOCATOR).send_keys(Keys.TAB) # при инпуте части текста можно использовать Tab



