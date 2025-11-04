import requests
from bs4 import BeautifulSoup
url="https://en.wikipedia.org/wiki/Hair_loss"
#url=input("Enter wiki link: ")
headers = {"User-Agent": "Mozilla/5.0"}
page = requests.get(url, headers=headers)

html=page.text
soup=BeautifulSoup(html,"html.parser")

body = soup.find_all("div",{"class":"mw-body-content"})

for p in body:
    print(p.text)
