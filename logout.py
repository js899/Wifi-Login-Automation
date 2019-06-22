# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 17:21:23 2019

@author: hp
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
#from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
#import time
driver = webdriver.Chrome("C:\\Users\\hp\\mydriver\\chromedriver")
driver.get("https://login.gndec.ac.in/nebtree/logout.php")
driver.find_element_by_name("submit").click()
driver.close()
#send_keys(Keys.ENTER)