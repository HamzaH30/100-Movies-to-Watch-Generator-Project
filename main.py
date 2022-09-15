import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Getting the website code / HTML code
response = requests.get(URL)

# Movie #59 called "E.T. – The Extra Terrestrial" has a dash in the name, it gets encoded when using python,
# this line of code fixes it and when the movie title is added to the .txt file, it displays the dash.
response.encoding = "utf-8"

top_100_movies_website = response.text

# Creating the BeautifulSoup object
soup = BeautifulSoup(top_100_movies_website, "html.parser")

# Creating a list of the top 100 movies, starting from #1
movie_title_tags = soup.find_all(name="h3", class_="title")
movie_titles = [movie_title_tag.getText() for movie_title_tag in movie_title_tags]
movie_titles.reverse()

# Creating the .txt file
with open("movies.txt", mode="w") as movie_file:
    for movie_title in movie_titles:
        movie_file.write(f"{movie_title}\n")
