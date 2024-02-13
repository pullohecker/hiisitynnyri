from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

email = input()
passw = "asdjhasd2"

web = webdriver.Chrome()

web.get('https://vantaa.inschool.fi')

sleep(1)

for i in range(40):
    osoite = web.find_element(By.ID, "login-frontdoor")
    osoite.send_keys(email)
    salakala = web.find_element(By.ID, "password")
    salakala.send_keys(passw + Keys.ENTER)
    print(i)
web.quit()
