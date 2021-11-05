from dotenv import load_dotenv
import requests

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movies.settings")

import django
django.setup()

from movies.models import Movie

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")


class TMDBHelper:
    def __init__(self, api_key=None):
        self.api_key = api_key

    def get_request_url(self, method="/movie/popular", **kwargs):
        base_url = "https://api.themoviedb.org/3"
        request_url = base_url + method
        request_url += f"?api_key={self.api_key}"

        for k, v in kwargs.items():
            request_url += f"&{k}={v}"

        return request_url


def get_popular_movie():
    method = "/movie/popular"
    query_set = {"region": "KR", "language": "ko-KR"}
    mv = TMDBHelper(API_KEY)
    request_url = mv.get_request_url(method, **query_set)
    data = requests.get(request_url).json()

    return data.get("results")


# insert data into sqlite
if __name__ == '__main__':
    popular_mv_lst = get_popular_movie()
    for movie in popular_mv_lst:
        Movie(title=movie["title"],
              release_date=movie["release_date"],
              popularity=movie["popularity"],
              vote_count=movie["vote_count"],
              vote_average=movie["vote_average"],
              overview=movie["overview"],
              poster_path=movie["poster_path"],
              tmdb_id=movie["id"]
              ).save()
