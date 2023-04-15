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

    return hn


if __name__ == "__main__":
    final_ans = []
    for page_number in range(2):
        res = requests.get(f"https://news.ycombinator.com/news?p={page_number + 1}")
        if res.status_code != 200:
            print(f"Something went wrong {res.status_code}")
        else:
            soup = BeautifulSoup(res.text, "html.parser")
            links_list = soup.select(".titleline > a")
            subtext_list = soup.select(".subtext")

            final_ans.extend(create_custom_hn(links_list, subtext_list))

    final_ans = sort_stories_by_votes(final_ans)
    pprint.pprint(final_ans)
