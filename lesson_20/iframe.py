import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)

NAME_FIELD_LOCATOR = ("xpath", "//input[@id='RESULT_TextField-0']")
COPY_TEXT_BTN_LOCATOR = ("xpath", "//button[text()='Copy Text']")

driver.get("https://testautomationpractice.blogspot.com/")

# iframe - это тэг, который помогает встраивать html-страницу внутрь другой html-страницы
# ➖ driver.switch_to.frame("id/name/index/WebElement") - переключение на iframe
# ➖ driver.switch_to.default_content() - переключение на дефолтный контент
# ➖ driver.switch_to.parent_frame() - переключение на родительский iframe

driver.switch_to.frame("frame-one796456169")
driver.find_element(*NAME_FIELD_LOCATOR).send_keys("Kirill")
time.sleep(2)

driver.switch_to.default_content() # переключение на дефолтный контент
driver.find_element(*COPY_TEXT_BTN_LOCATOR).click()
time.sleep(2)

# вложенные iframe-ы (Nested Frames) - переключение между parent,  child, default content
driver.get("https://demoqa.com/nestedframes")
driver.switch_to.frame("frame1")
print(driver.find_element("xpath", "//body").text) # Parent frame
driver.switch_to.frame(0)
print(driver.find_element("xpath", "//body").text) # Child Iframe
driver.switch_to.parent_frame()
print(driver.find_element("xpath", "//body").text) # Parent frame

driver.switch_to.default_content()
print(driver.find_element("xpath", "//h1").text) # Nested Frames



