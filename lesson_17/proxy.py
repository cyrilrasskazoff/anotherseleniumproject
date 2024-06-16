import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# http://free-proxy.cz/ru/
PROXY_SERVER = "155.94.241.134:3128"

options = Options()
# options.add_argument(f"--proxy-server=ip_proxy:port_proxy")
options.add_argument(f"--proxy-server={PROXY_SERVER}")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://2ip.ru") # 178.120.63.25 //

time.sleep(2)

