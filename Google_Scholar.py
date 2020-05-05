import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from random import randrange
import time

def get_university_link(university):
    university.replace(" ", "+")
    page = requests.get("https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors={}&btnG=".format(quote_plus(university)))
    soup = BeautifulSoup(page.text, "html.parser")
    h3 = soup.find("h3", attrs={ "class": "gsc_inst_res" })
    return "https://scholar.google.com{}".format(h3.a.get("href"))

def get_researchers(soup):
    users = soup.find_all("div", attrs={ "class": "gsc_1usr" })
    researchers = []
    for user in users:
        areas = user.find("div", attrs={ "class": "gs_ai_int" })
        if areas.find("a", string="Agriculture") is None: 
            continue
        id_link = user.div.a.get("href")
        citations = user.find("div", { "class": "gs_ai_cby" }).string
        researchers.append((id_link[id_link.rfind("=") + 1:], citations[citations.rfind(" ") + 1:]))
    return researchers

def get_next_link(soup):
    js = soup.find("button", attrs={ "class": "gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx" }).get("onclick")

    link = js[js.find("'") + 1:js.rfind("'")]

    link = link.replace("\\x26", "&")
    link = link.replace("\\x3d", "=")

    return "https://scholar.google.com{}".format(link)

def get_researchers_for_university(university):
    link = get_university_link(university)
    loop(link)

def loop(link):
    try:
        while True:
            page = requests.get(link)
            soup = BeautifulSoup(page.text, "html.parser")

            for r in get_researchers(soup):
                print(r)
            
            link = get_next_link(soup)
            time.sleep(randrange(5, 20))
    except:
        print(link)


        


get_researchers_for_university("Cornell University")

# l1 = get_university_link("Alabama A&M University")
# print(l1)

# p1 = requests.get("https://scholar.google.com{}".format(l1))
# s1 = BeautifulSoup(p1.text, "html.parser")

# print(get_next_link(s1))



# p2 = requests.get("https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=cornell&after_author=UymYAAxE__8J&astart=30")
# s2 = BeautifulSoup(p2.text, "html.parser")
# print(get_researchers(s2))

#Code from Ed Buckler
