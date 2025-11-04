import requests
from bs4 import BeautifulSoup

url="https://www.yelp.com/search?find_desc=restaurants&find_loc=Atlanta%2C+GA+30303"

response = requests.get(url)
html = response.text

soup=BeautifulSoup(html,'html.parser')
mylinks=soup.find_all('h3',{"class":"y-css-hcgwj4"})

print(len(mylinks))