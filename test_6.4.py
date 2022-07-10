import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    r'C:\Users\user\Documents\VS\Selenium\Python\webdriver\chromedriver.exe')
driver.maximize_window()

driver.get("http://suninjuly.github.io/simple_form_find_task.html")

try:
    element = driver.find_element_by_xpath(
        "//*[@name='first_name']").send_keys("Ivan")
    element = driver.find_element_by_xpath(
        "//*[@name='last_name']").send_keys("Petrov")
    element = driver.find_element_by_xpath(
        "(//*[@name='firstname'])[1]").send_keys("Smolensk")
    element = driver.find_element_by_xpath(
        "(//*[@name='firstname'])[2]").send_keys("Russia")
    submit_button = driver.find_element_by_xpath(
        "//*[@id='submit_button']").click()

finally:
    time.sleep(5)
    driver.quit()
