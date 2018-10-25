# http://www.practicepython.org/solution/2014/07/10/17-decode-a-web-page-solutions.html

import requests
from bs4 import BeautifulSoup


base_url = input("Enter the URL :  ")

resp = requests.get(base_url)

soup = BeautifulSoup(resp.text, features="html.parser")

for story_heading in soup.find_all(class_="summary"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())

