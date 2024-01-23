from bs4 import BeautifulSoup
import requests
 
response = requests.get("https://news.ycombinator.com")
yc_web_page = response.text
 
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
article_upvotes = []

for article in articles:
    text = article.text
    article_texts.append(text)
    link = article.find(name="a").get("href")
    article_links.append(link)

upvotes = soup.find_all(name="span", class_="score")
for article_upvote in upvotes:
    article_upvotes.append(int(article_upvote.getText().split()[0]))

print(len(article_texts))
print(len(article_links))
print(len(article_upvotes))
print(article_upvotes)