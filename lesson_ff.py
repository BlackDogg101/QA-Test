from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
import time
# from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(10)
driver.close()