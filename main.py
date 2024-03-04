
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://github.com/')

wait = WebDriverWait(driver, 10)

text_area = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[4]/main/div[1]/div[2]/div/div/div[2]/div[2]/form/div/dl/dd/input")))
text_area.send_keys("damian")

driver.close()
