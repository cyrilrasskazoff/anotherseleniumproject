import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# класс ActionChains применяется для выполнения действий,
# которые не могут быть выполнены стандартными средствами Selenium
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)

actions = ActionChains(driver)
wait = WebDriverWait(driver, 15, poll_frequency=1)

LEFT_CLICK_BTN_LOCATOR = ("xpath", "//button[@id='leftClick']")
DOUBLE_CLICK_BTN_LOCATOR = ("xpath", "//button[@id='doubleClick']")
CONTEXT_CLICK_BTN_LOCATOR = ("xpath", "//button[@id='rightClick']")
HOVER_BTN_LOCATOR = ("xpath", "//button[@id='colorChangeOnHover']")
driver.get("https://testkru.com/Elements/Buttons")
time.sleep(2)

left_btn = driver.find_element(*LEFT_CLICK_BTN_LOCATOR)
# цtпочка действий замыкается методом perform()
actions.click(left_btn).perform()
time.sleep(2)

double_btn = driver.find_element(*DOUBLE_CLICK_BTN_LOCATOR)
actions.double_click(double_btn).perform()
time.sleep(2)

# context_click - это клик правой кнопкой мыши - открывает контекстное меню
context_btn = driver.find_element(*CONTEXT_CLICK_BTN_LOCATOR)
actions.context_click(context_btn).perform()
time.sleep(2)

# move_to_element() - наведение на элемент
hover_btn = driver.find_element(*HOVER_BTN_LOCATOR)
actions.move_to_element(hover_btn).perform()
time.sleep(2)

# соединим в цепочку действия
driver.refresh()
time.sleep(2)
actions.click(wait.until(EC.element_to_be_clickable(LEFT_CLICK_BTN_LOCATOR))).\
    double_click(wait.until(EC.element_to_be_clickable(DOUBLE_CLICK_BTN_LOCATOR))).\
    context_click(wait.until(EC.element_to_be_clickable(CONTEXT_CLICK_BTN_LOCATOR))).perform()
time.sleep(3)

# добавим паузы в цепочку с пом. метода pause()
driver.refresh()
time.sleep(2)
actions.click(wait.until(EC.element_to_be_clickable(LEFT_CLICK_BTN_LOCATOR))).pause(2).\
    double_click(wait.until(EC.element_to_be_clickable(DOUBLE_CLICK_BTN_LOCATOR))).pause(2).\
    context_click(wait.until(EC.element_to_be_clickable(CONTEXT_CLICK_BTN_LOCATOR))).perform()
time.sleep(2)

# real_life
MAIN_MENU_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
SUB_MENU_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
driver.get(" https://demoqa.com/menu")

actions.move_to_element(driver.find_element(*MAIN_MENU_LOCATOR)).pause(2).\
    move_to_element(driver.find_element(*SUB_MENU_LOCATOR)).pause(2).\
    perform()
