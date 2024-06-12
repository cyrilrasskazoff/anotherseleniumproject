from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
import time

service = Service(executable_path=ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=service, options=chrome_options)

DROPDOWN_LOCATOR = ("xpath", "//select[@id='dropdown']")
driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(2)

DROPDOWN = Select(driver.find_element(*DROPDOWN_LOCATOR)) # инициализируем объект класса Select

DROPDOWN.select_by_visible_text('Option 1')
time.sleep(2)
DROPDOWN.select_by_value('2')
time.sleep(2)
DROPDOWN.select_by_index(1)
time.sleep(2)

#*****************
driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(2)

DROPDOWN = Select(driver.find_element(*DROPDOWN_LOCATOR))
all_options = DROPDOWN.options
print(all_options)

# перебор по тексту

for option in all_options:
    time.sleep(2)
    DROPDOWN.select_by_visible_text(option.text)
    print(option.text)

for option in all_options:
    if 'Option 1' in option.text:
        print("Option 1 присутствует")


# перебор по индексу
driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(2)

DROPDOWN = Select(driver.find_element(*DROPDOWN_LOCATOR))
all_options = DROPDOWN.options

for option in all_options:
    time.sleep(2)
    DROPDOWN.select_by_index(all_options.index(option))
    print(all_options.index(option))


# перебор по value
driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(2)

DROPDOWN = Select(driver.find_element(*DROPDOWN_LOCATOR))
all_options = DROPDOWN.options

for option in all_options:
    time.sleep(2)
    DROPDOWN.select_by_value(option.get_attribute("value"))
    print(option.get_attribute("value"))


