import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from scrolls import Scrolls

options = Options()
options.add_argument("--window-size=1920,1080")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)
actions = ActionChains(driver)
scrolls = Scrolls(driver, actions)

driver.get("https://seiyria.com/bootstrap-slider/")

driver.execute_script("alert('hello')")
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()

driver.refresh()
time.sleep(2)
ELEMENT_LOCATOR = ("xpath", "//h3[text()='Example 3: ']")
element = driver.find_element(*ELEMENT_LOCATOR)

# default selenium scroll execution
actions.scroll_to_element(element).perform()
time.sleep(2)

# custom scroll execution
scrolls.scroll_to_element(element)
time.sleep(2)

