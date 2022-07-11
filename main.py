from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
driver.get('https://www.linkedin.com/')
time.sleep(2)


username = driver.find_element(By.ID, "session_key")
password = driver.find_element(By.ID, "session_password")

username.send_keys('YOUR EMAIL LINKDLN')
password.send_keys('YOUR LINKDLN PASSWORD')
time.sleep(2)

submit = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button").click()
time.sleep(2)

driver.get("https://www.linkedin.com/search/results/people/?origin=FACETED_SEARCH&page=2&sid=f%3B7")
time.sleep(3)

all_buttons = driver.find_elements(By.TAG_NAME, "button")
connect_buttons =[btn for btn in all_buttons if btn.text == "Conectar"]


for btn in connect_buttons:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)
    send = driver.find_element(By.XPATH,"//button[@aria-label='Enviar agora']")
    driver.execute_script("arguments[0].click();", send)
    time.sleep(2)
