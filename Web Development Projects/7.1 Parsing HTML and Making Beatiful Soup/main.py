# pip install bs4
from bs4 import BeautifulSoup
#import lxml

with open("./website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)
#print(soup)
#print(soup.prettify())
#print(soup.li)

all_anchors_tag = soup.find_all(name="a")
#print(all_anchors_tag)

#for tag in all_anchors_tag:
    #print(type(tag)) #<class 'bs4.element.Tag'>
    #print(tag.getText())
    #print(tag.get("href"))

heading = soup.find(name="h1", id="name")
#print(heading)

section_heading = soup.find(name="h3", class_="heading")
#print(section_heading)
#print(section_heading.getText())
#print(section_heading.get("class"))
#print(section_heading.name)

company_url = soup.select_one(selector="p a")
#print(company_url)
#print(company_url.getText())
#print(company_url.get("href"))
page_name = soup.select_one(selector="#name")
#print(page_name)

print(soup.select(selector=".heading"))
