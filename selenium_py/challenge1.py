from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
#from pwn import *

driver = webdriver.Chrome("/home/sterlite/learn/chromedriver")
url="https://hvdevops.prashantdey.in/challenges"
usrname="name"
pwd="password"
path='"//*[@id="-2022757"]/button"'
driver.get(url)
driver.implicitly_wait(50)
driver.find_element(By.NAME, usrname).send_keys("Ajit Rathor")
driver.find_element(By.ID, pwd).send_keys("Vlearn@77")
driver.implicitly_wait(500)
driver.find_element(By.NAME, "_submit").click()
time.sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(10)
driver.find_element(By.ID, "-2022757").click()
#ch1=driver.find_element("xpath", path).click()
#ch1txt=driver.find_element("xpath", '"//*[@id="-2022757"]/button/p"')
#print (ch1txt.text)
#ch1.click()
time.sleep(10)
driver.implicitly_wait(100)
#v.click()
ans=os.system('nc -dN 43.204.232.3 2001 ')
ans1=os.system(""awk -F ":" '{print $2}'"") 

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

v1=driver.find_element(By.ID, "challenge-input").send_key(ans)
