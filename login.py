from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
#from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
#import time
driver = webdriver.Chrome("C:\\Users\\hp\\mydriver\\chromedriver")
driver.get("https://login.gndec.ac.in/nebtree/login.php ")
username = driver.find_element_by_id("username2")
username.clear()
username.send_keys("1815032")
password = driver.find_element_by_id("cd-Password2")
password.clear()
password.send_keys("Aalam*99") 
driver.find_element_by_name("submit").click()
driver.close()
#send_keys(Keys.ENTER)