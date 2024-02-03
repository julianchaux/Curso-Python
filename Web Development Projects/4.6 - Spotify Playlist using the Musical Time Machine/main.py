import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(URL + date)
# Buscamos el playlist de Billboard en la fecha ingresada
# https://www.billboard.com/charts/hot-100/1983-11-17
 
soup = BeautifulSoup(response.text, "html.parser")

song_names_spans = soup.select("li ul li h3")
for song in song_names_spans:
    song_names = [song.getText().strip() for song in song_names_spans]
