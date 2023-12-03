import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from unidecode import unidecode
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re

username = "B20DCCN325XLAN4FA23"
password = "Aa167218@"

with open('chuong_8.json', 'r') as file:
    data = json.load(file)


driver = webdriver.Edge()
# driver.get("https://drnguyentt.com/moodle30/mod/quiz/view.php?id=3678")
driver.get("https://drnguyentt.com/moodle30/mod/quiz/view.php?id=3092")


username_input = driver.find_element(By.NAME,"username")
username_input.send_keys(username)
password_input = driver.find_element(By.NAME,"password")
password_input.send_keys(password)
login_button = driver.find_element(By.ID, "loginbtn")
login_button.click()
buttons = driver.find_elements(By.CSS_SELECTOR, 'button[id^="single_button"]')


for button in buttons:
    button.click()
    
while True:
    try:
        qtext_element = driver.find_element(By.CLASS_NAME, "qtext")
        qtext = qtext_element.text  
        print(qtext)
        option = driver.find_element(By.XPATH, f"//div[contains(text(), '{data[qtext]}')]")
        option.click()
        next_button = driver.find_element(By.NAME, "next")
        next_button.click()
        # time.sleep(1000) 
    except Exception as e:
        print(str(e))
        time.sleep(3) 

time.sleep(1000)
