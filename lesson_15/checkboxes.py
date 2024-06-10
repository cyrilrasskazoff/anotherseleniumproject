from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path=ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")


driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(2)
CHECKBOX_1 = ("xpath", "(//input[@type='checkbox'])[1]")
# получим:
# 1. значение атрибута 'checked' до клика на чекбокс
# 2. значение встроенного метода 'is_selected' до клика на чекбокс
print(driver.find_element(*CHECKBOX_1).get_attribute("checked")) # None
print(driver.find_element(*CHECKBOX_1).is_selected()) # False
# кликнем по чекбоксу и получим:
# 1.значение атрибута 'checked' после клика
# 2. значение встроенного метода 'is_selected' после клика
driver.find_element(*CHECKBOX_1).click()
time.sleep(2)
print(driver.find_element(*CHECKBOX_1).get_attribute("checked")) # true
assert driver.find_element(*CHECKBOX_1).get_attribute("checked") is not None
assert driver.find_element(*CHECKBOX_1).get_attribute("checked") == "true"
print(driver.find_element(*CHECKBOX_1).is_selected()) # True

# *****************************
# Нюансы
# 1. иногда элемент чекбокса перекрыт другим элементом = не кликабелен; в таком случае нужно кликнуть по этому элементу,
# а в качестве проверки получить статус чекбокса
driver.get("https://demoqa.com/checkbox")
time.sleep(2)
CHECKBOX_ELEMENT_STATUS = ("xpath", "//input[@type='checkbox']")
CHECKBOX_ELEMENT_ACTION = ("xpath", "//span[@class='rct-checkbox']")

print(driver.find_element(*CHECKBOX_ELEMENT_STATUS).is_selected()) # False

driver.find_element(*CHECKBOX_ELEMENT_ACTION).click()
time.sleep(2)
print(driver.find_element(*CHECKBOX_ELEMENT_STATUS).is_selected()) # True

# 2. Нестандартная реализация чекбоксов (не в виде input[@type='checkbox']. В таком случае мы не можем получить
# значение метода is_selected()). Нужно кликнуть по пcевдочекбоксу и наблюдать, что изменится в состоянии элемента в
# dev tools
# wait = WebDriverWait(driver, 15, poll_frequency=1)
driver.get("https://demoqa.com/selectable")
time.sleep(2)
CHECKBOX_LIKE_ELEMENT = ("xpath", "//li[text()='Cras justo odio']")
# получим отрибут class элемента:
# до клика
before = driver.find_element(*CHECKBOX_LIKE_ELEMENT).get_attribute("class")
print(before)
# после клика
# wait.until(EC.element_to_be_clickable(CHECKBOX_LIKE_ELEMENT)).click()
driver.find_element(*CHECKBOX_LIKE_ELEMENT).click()
after = driver.find_element(*CHECKBOX_LIKE_ELEMENT).get_attribute("class")
print(after)

assert "active" in after




