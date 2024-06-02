from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://demoqa.com/dynamic-properties")

BTN_VISIBLE_AFTER = ("xpath", "//button[@id='visibleAfter']")
wait.until(EC.visibility_of_element_located(BTN_VISIBLE_AFTER)).click() # метод visibility_of_element_located автоматически
# распаковывает кортеж BTN_VISIBLE_AFTER, поэтому распаковщик (*) не нужен

BTN_ENABLE_AFTER = ("xpath", "//button[@id='enableAfter']")
wait.until(EC.element_to_be_clickable(BTN_ENABLE_AFTER)).click()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")
REMOVE_BTN = ("xpath", "//button[text()='Remove']") # данная кнопка исчезает через определенное время после нажатия
driver.find_element(*REMOVE_BTN).click()

wait.until(EC.invisibility_of_element_located(REMOVE_BTN))
print("Button disappeared")

ENABLE_BTN = ("xpath", "//button[text()='Enable']")
INPUT = ("xpath", "//input[@type='text']")
wait.until(EC.element_to_be_clickable(ENABLE_BTN)).click()
wait.until(EC.element_to_be_clickable(INPUT)).send_keys('Hello!')
wait.until(EC.text_to_be_present_in_element_value(INPUT, 'Hello!'))






