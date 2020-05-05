import requests
from selenium import webdriver
import time
import os
from selenium.webdriver.support.ui import Select
import numpy as np
import lxml.html as lh
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup

url = "https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=label:agriculture&before_author=ri48_2CZAAAJ&astart=0"
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"))

driver.get(url)


#page = requests.get(url)

#doc = lh.fromstring(page.content)

for x in range(10):
    A_elements = driver.find_elements_by_class_name("gs_ai_name")
    for A in A_elements:
        print(A.text)
    driver.find_element_by_class_name("gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx").click()
