import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Задаём настройки для браузера
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--headless') # Опция запуска браузера в headless режиме
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
time.sleep(3)

# Создаём переменные для логина и пароля
login_standard_user = 'standard_use'
password_all = 'secret_sauce'

# Вводим логин
user_name = driver.find_element(By.XPATH,"//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print('Input Login')

# Вводим пароль
password = driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys(password_all)
print('Input Password')

# Кликаем на кнопку Login
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print('Click Button')

warning_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warning_text = warning_text.text
assert value_warning_text == 'Epic sadface: Username and password do not match any user in this service'
print('Good test')

driver.refresh()