from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By

def link_t(link):
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Kesa')
    browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Lisa')
    browser.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys('KL@google.com')
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
    return welcome_text



def test_reg1():
    assert link_t("http://suninjuly.github.io/registration1.html") == "Поздравляем! Вы успешно зарегистировались!", "registration is failed"


def test_reg2():
    assert link_t("http://suninjuly.github.io/registration2.html") == "Поздравляем! Вы успешно зарегистировались!", "registration is failed"

if __name__ == "__main__":
    pytest.main()