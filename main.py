import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"



response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="strong")
movies_titles = [movie.getText().split() for movie in all_movies]
clean_data = []
for item in movies_titles:
    text = " ".join(item).strip()
    if text and not text.startswith(('Starring:', 'Director:', 'Directors:', 'READ MORE:')):
        clean_data.append(text)
movies = clean_data[::-1]

with open ("movie.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")







