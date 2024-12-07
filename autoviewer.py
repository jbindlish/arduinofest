from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("http://127.0.0.1")
time.sleep(5)
driver.find_element(By.ID,"component-14-button").click()
while True:
    driver.find_element(By.ID,"component-16").click()
    time.sleep(40)
