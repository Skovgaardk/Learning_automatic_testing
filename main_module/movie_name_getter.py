import requests
import os
import json
from dotenv import load_dotenv



## Function for calling movie db api
def get_movies_by_popularity():
    url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"

    auth = os.getenv("API_HEADER_AUTH")

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + auth,
    }

    response = requests.get(url, headers=headers)

    return response

## Function for just getting the moveie names
def get_movie_names(movies):
    movie_names = []
    for movie in movies:
        movie_names.append(movie["original_title"])


    return movie_names


if __name__ == "__main__":
    load_dotenv()
    movies = Get_movies_by_popularity()
    data = json.loads(movies.text)
    movies = data['results']
    movie_names = Get_movie_names(movies)

    print(movie_names)

