from selenium import webdriver

from  selenium.webdriver.chrome.service import Service

import time

url = "https://www.ajio.com/c/830307006"

s = Service("C:/Users/cs/PycharmProjects/pythonProject4/chromedriver.exe")

driver = webdriver.Chrome(service = s)

driver.get(url)
height=driver.execute_script("return document.body.scrollHeight")
time.sleep(5)
while True:
    height=driver.execute_script("return document.body.scrollHeight")
    # print(height)

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if height==new_height:
        break
    height= new_height