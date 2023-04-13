import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

options = Options()
options.use_chromium = True
options.add_argument('--disable-gpu')

driver = webdriver.Edge(executable_path='/home/alex/Edge Web Drive/msedgedriver', options=options)
driver.execute_script('window.open("https://www.baidu.com");')

driver.switch_to.window(driver.window_handles[-1])
time.sleep(5)

driver.close()