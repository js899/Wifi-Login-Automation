#webscraping+python+selenium+webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #makes the driver wait until the whole page is loaded
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys         #used to send keyboard keys
from selenium.webdriver.common.by import By             #to select elements from webpage source code(inspect)
#import time
driver = webdriver.Chrome("C:\\Users\\hp\\mydriver\\chromedriver")
driver.get("https://login.gndec.ac.in/nebtree/login.php ")
username = driver.find_element_by_id("------")          #username input box
username.clear()                                          
username.send_keys("*****")                             #username keys sent
password = driver.find_element_by_id("-----")
password.clear()
password.send_keys("*****") 
driver.find_element_by_name("submit").click()           #submit button clicked
driver.close()                                          #browser closed
#send_keys(Keys.ENTER)
