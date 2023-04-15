import requests
from bs4 import BeautifulSoup
import pprint


def sort_stories_by_votes(hn):
    return sorted(hn, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        vote = subtext[index].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})

    return sort_stories_by_votes(hn)


if __name__ == "__main__":
    res = requests.get("https://news.ycombinator.com/news")
    if res.status_code != 200:
        print(f"Something went wrong {res.status_code}")
    else:
        soup = BeautifulSoup(res.text, "html.parser")
        links_list = soup.select(".titleline > a")
        subtext_list = soup.select(".subtext")

    pprint.pprint(create_custom_hn(links_list, subtext_list))
