rom selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = " http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID,'num1')
    x = int(x_element.text)
    y_element = browser.find_element(By.ID,'num2')
    y = int(y_element.text)
    sum = str(x + y)

    box_element = Select(browser.find_element(By.ID, "dropdown"))

    sum_element = box_element.select_by_value(sum)

    button = browser.find_element(By.CSS_SELECTOR,'button.btn').click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
