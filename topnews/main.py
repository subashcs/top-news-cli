from bs4 import BeautifulSoup
import inquirer
import requests
from urllib.request import urlopen

news_url = "https://news.google.com/news/rss"
Client = urlopen(news_url)
xml_page = Client.read()
Client.close()

soup_page = BeautifulSoup(xml_page, "xml")
news_list = soup_page.findAll("item")
# Print news title, url and publish date
choices = []
links = []
for news in news_list:
  print(news.title.text)
  choices.append(news.title.text)
  links.append(news.link.text)
  print(news.link.text)
  print(news.pubDate.text)
  print("-"*60)

questions = [
  inquirer.List('size',
                message="Choose preferred news?",
                choices=choices,
            ),
]
answers = inquirer.prompt(questions)
url = "https://news.google.com/__i/rss/rd/articles/CBMiaWh0dHBzOi8vc2NpdGVjaGRhaWx5LmNvbS9zZWNyZXRzLXRvLWFnaW5nLWdyYWNlZnVsbHktcmVzZWFyY2hlcnMtdW5jb3Zlci1mYWN0b3JzLWxpbmtlZC10by1vcHRpbWFsLWFnaW5nL9IBbWh0dHBzOi8vc2NpdGVjaGRhaWx5LmNvbS9zZWNyZXRzLXRvLWFnaW5nLWdyYWNlZnVsbHktcmVzZWFyY2hlcnMtdW5jb3Zlci1mYWN0b3JzLWxpbmtlZC10by1vcHRpbWFsLWFnaW5nL2FtcC8?oc=5"
# Fetch raw HTML content
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "html.parser")
print(soup.prettify())
# print(answers)

