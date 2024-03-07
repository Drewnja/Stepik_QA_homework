from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try: 
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    price = WebDriverWait(browser, 13).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    browser.find_element(By.ID, "book").click()

    value = browser.find_element(By.ID, "input_value")
    val_txt = int(value.text)

    y = calc(val_txt)

    browser.find_element(By.ID, "answer").send_keys(y)

    browser.find_element(By.ID, "solve").click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()