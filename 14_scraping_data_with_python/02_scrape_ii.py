import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/news")
if res.status_code != 200:
    print(f"Something went wrong {res.status_code}")
else:
    soup = BeautifulSoup(res.text, "html.parser")
    # we use CSS selector to fine grain select the data we want
    print(soup.select("a"))

    # to select a class use "." and to select an id use "#"
    print(soup.select(".score"))
    print(soup.select("#score_35127063"))
