import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# для вебдрайвера нет разницы между окном и вкладкой; дескриптор - это id окна/вкладки

FOR_BUSINESS_BTN_LOCATOR = ("xpath", "//a[text()=' For Business ']")
START_FOR_FREE_BTN_LOCATOR = ("xpath", "//a[text()='Start for Free']")

driver.get("https://hyperskill.org/tracks")

# параметр драйвера current_window_handle - хранит активное окно/вкладку
print(driver.current_window_handle) # 4201A8BAA2CEE2B4BAF46D4EB63519FB - дескриптор текущего окна

driver.find_element(*FOR_BUSINESS_BTN_LOCATOR).click()
time.sleep(2)

# параметр драйвера window_handles - хранит все открытые окна/вкладки в виде списка
print(driver.window_handles) # ['A2FC556A27BC4B8F3ECCAA264C0F3D31', '7FFEC402181F732743BE09D93FDE1E1D', ...]
tabs = driver.window_handles
driver.switch_to.window(tabs[1])

# another way:
# new_tab = driver.window_handles[1]
# driver.switch_to.window(new_tab)

# another way:
# driver.switch_to.window(driver.window_handles[1])

driver.find_element(*START_FOR_FREE_BTN_LOCATOR).click()
time.sleep(2)

#*****************
# новый метод switch_to.new_window - принимает в кач-ве параметра tab или window - автоматически переключает вебдрайвер
# на новую вкладку/окно   !!!! новая вкладка/окно открыввется в ТОЙ ЖЕ сессии !!!
driver.switch_to.new_window("tab")
driver.get("https://onliner.by")
time.sleep(2)
driver.switch_to.new_window("window")
driver.get("https://google.com")
time.sleep(2)





