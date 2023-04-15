import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/news")
if res.status_code != 200:
    print(f"Something went wrong {res.status_code}")
else:
    soup = BeautifulSoup(res.text, "html.parser")

    # return all the body content in the html body tag
    print(soup.body)

    # return a list of all the body content in the html body tag
    print(soup.body.contents)

    # to find all div objects
    print(soup.find_all("div"))

    # to find all anchor tags
    print(soup.find_all("a"))

    # find returns the first item while find_all returns the list

    # find using id
    print(soup.find(id="score_20514755"))

