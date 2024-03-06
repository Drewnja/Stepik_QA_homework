# Добавьте webdriver в PATH. На MacOS легче всего поставить вебдрайвер сразу через brew:
# brew install --cask chromedriver


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    value = browser.find_element(By.ID, "num1")
    x1 = value.text

    value2 = browser.find_element(By.ID, "num2")
    x2 = value2.text
    y = int(x1) + int(x2)

    print(y)

    browser.find_element(By.TAG_NAME, "select").click()
    browser.find_element(By.CSS_SELECTOR, f'[value="{y}"]').click()

    inp4 = browser.find_element(By.CLASS_NAME, "btn")
    inp4.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()