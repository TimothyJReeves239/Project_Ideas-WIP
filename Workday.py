import requests
import lxml.html as lh
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
from selenium.webdriver.support.ui import Select
import numpy as np

print("Enter your NetId")
input(Name)
print("Enter your Password")
input(Pass)

url="https://www.myworkday.com/cornell/d/home.htmld"
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"))
driver.get(url)
driver.find_element_by_xpath('//a[@href="https://shibidp.cit.cornell.edu/idp/profile/SAML2/Unsolicited/SSO?providerId=http://www.workday.com"]').click()

    
NetId = driver.find_element_by_name('NetId')
Password = driver.find_element_by_name('Password').click()

username.send_keys(Name)
password.send_keys(Pass)

driver.find_element_by_name("submit").click()

driver.find_element_by_name('time').click()
