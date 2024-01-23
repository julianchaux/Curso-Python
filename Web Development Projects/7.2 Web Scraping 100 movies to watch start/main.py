import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
empire_online_webpage = response.text
 
soup = BeautifulSoup(empire_online_webpage, "html.parser")

titles_movies = soup.find_all(name="h3", class_="title")
best_movies = []

for title_movie in titles_movies:
    best_movies.append(title_movie.getText())

best_100_movies = best_movies[::-1]

with open("best_100_movies.txt", mode="w", encoding="utf8") as file:
    for movie in best_100_movies:
        file.write(movie + "\n")
