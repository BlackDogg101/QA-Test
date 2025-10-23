import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Задаём настройки для браузера
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument('--headless')
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
time.sleep(3)

# Создаём переменные для логина и пароля
login_standard_user = 'standard_user'
password_all = 'secret_sauce'

# Вводим логин
user_name = driver.find_element(By.XPATH,"//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print('Input Login')
 
# Вводим пароль
password = driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys(password_all)
print('Input Password')
password.send_keys(Keys.RETURN)

# Кликаем на фильтр
filter = driver.find_element(By.XPATH,"//select[@data-test='product-sort-container']")
filter.click()
time.sleep(5)
filter.send_keys(Keys.DOWN)
time.sleep(5)
filter.send_keys(Keys.RETURN)

driver.save_screenshot('screenshot.png')