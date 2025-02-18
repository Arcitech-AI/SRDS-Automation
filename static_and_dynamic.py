from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(2)