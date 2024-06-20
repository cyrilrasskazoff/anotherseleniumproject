import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())


# для одновременной мультисессионной (под разными юзерами) работы необходимо для каждого юзера инициализировать свой
# объект вебдрайвера
driver_1 = webdriver.Chrome(service=service, options=options)
driver_1.get("")
driver_1.find_element("")

#......
driver_2 = webdriver.Chrome(service=service, options=options)
driver_2.get("")
#.....

# если нужна работа в разных окнах в рамках одной сессии, то используется один объект вебдрайвера и метод
# .switch_to.new_window()
