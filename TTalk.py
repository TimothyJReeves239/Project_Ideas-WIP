import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from random import randrange
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("/Users/timreeves/Desktop/Python_Stuff/GxE/chromedriver.exe")

def get_random_link():
    url = "https://www.youtube.com/feed/trending"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    h3 = []
    h4 = []
    for a in soup.find_all('a', href=True): 
        if a.text: 
            h3.append(a['href'])
    for x in h3:
        if "watch" in x:
            h4.append(x)
    pick_random_link(h4)

def pick_random_link(urllist):
    v = random.randrange(0, len(urllist))
    t = ("youtube.com" + urllist[v])
    browser.get(("https://www.youtube.com" + urllist[v]))
    return ("https://www.youtube.com" + urllist[v])

def get_tags():
    url = "https://www.youtube.com/watch?v=jgWS4TdLFAE"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    print(soup.find_all('force-default-style', class_="style-scope ytd-video-primary-info-renderer"))

#get_tags()
    
        
###implement keywords -- https://www.lockedownseo.com/see-youtube-video-tags/
    


get_random_link()
