from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(10)
driver.get("https://demoqa.com/dynamic-properties")
# далее локатор элемента будем представлять в виде кортежа и обращаться к нему через распаковщик (*)
# кортеж - tuple - неизменяемая последоватеьность элементов любого типа, e.g., a = (1, 'str', True, [1, 2, 3])

BTN_VISIBLE_AFTER = ("xpath", "//button[@id='visibleAfter']")
driver.find_element(*BTN_VISIBLE_AFTER).click()


