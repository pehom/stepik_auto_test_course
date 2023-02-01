from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
import os


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def test(link):
    browser = webdriver.Chrome()

    try:
        browser.get(link)

        # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
        WebDriverWait(browser, 13).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
        button = browser.find_element(By.CSS_SELECTOR, "#book")
        button.click()
        x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
        x = x_element.text
        y = calc(x)
        input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
        input1.send_keys(y)
        button = browser.find_element(By.CSS_SELECTOR, "#solve")
        button.click()
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':
    test('http://suninjuly.github.io/explicit_wait2.html')
