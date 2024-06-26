import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)

actions = ActionChains(driver)
wait = WebDriverWait(driver, 15, poll_frequency=1)

# простой drag-and-drop с помощью drag_and_drop(source, target)
driver.get("https://the-internet.herokuapp.com/drag_and_drop")

COL_A_LOCATOR = ("xpath", "//div[@id='column-a']")
COL_B_LOCATOR = ("xpath", "//div[@id='column-b']")

A = driver.find_element(*COL_A_LOCATOR)
B = driver.find_element(*COL_B_LOCATOR)

actions.drag_and_drop(A, B).perform()
time.sleep(2)

# сложный drag-and-drop - применяется, когда target изначально недоступен. Алгоритм: выполнить click_and_hold(<source>)
#  -> выждать появления на странице target c помощью pause() -> выполнить move_to_element(<target>) -> отпустить
#  левую кнопку мыши с помощью release()
driver.get("https://tympanus.net/Development/DragDropInteractions/sidebar.html")

GRID_ELEMENT_LOCATOR = ("xpath", "//div[@class='grid__item'][2]")
# JS script - setTimeout(function() { debugger; }, 5000); - should be applied to identify the target locator
SIDEBAR_ELEMENT_LOCATOR = ("xpath", "//div[@class='drop-area__item'][1]")

actions.click_and_hold(driver.find_element(*GRID_ELEMENT_LOCATOR)).pause(1.5).\
    move_to_element(driver.find_element(*SIDEBAR_ELEMENT_LOCATOR)).release().perform()
time.sleep(2)


