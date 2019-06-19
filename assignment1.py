from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path=r'C:/Users/vaishnavi/Downloads/chromedriver_win32/chromedriver.exe')
driver.get("https://health.policybazaar.com/")
name = driver.find_element_by_id("inputname")
name.send_keys('Suraj Tiwari')
number = driver.find_element_by_name("mobilenumber")
number.send_keys('9898329930')
number.submit()
driver.find_element_by_xpath(".//*[contains(text(), 'Spouse')]").click()
driver.implicitly_wait(10)
b = driver.find_element_by_xpath(".//button[@type='submit' and contains(., 'CONTINUE')]")
b.click()
driver.implicitly_wait(500)
element = driver.find_element_by_xpath("//select[@name='selectSelf']")
driver.execute_script("arguments[0].click();", element)
element.click()
element = driver.find_element_by_xpath("//select[@name='selectSpouse']")
driver.execute_script("arguments[0].click();", element)
element.click()
number = driver.find_element_by_name("city")
number.send_keys('Bengaluru(Karnataka)')
number.submit()