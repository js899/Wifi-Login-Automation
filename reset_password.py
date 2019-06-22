
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
#from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
#import time
driver = webdriver.Chrome("C:\\Users\\hp\\mydriver\\chromedriver")
driver.get("http://academics.gndec.ac.in/forgotpassword/")
username=driver.find_element_by_name("username")
username.send_keys("-----")
driver.find_element_by_name("submitt").click()
#send_keys(Keys.ENTER)
