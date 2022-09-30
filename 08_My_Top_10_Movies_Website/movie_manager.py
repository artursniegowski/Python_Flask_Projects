# class for retriving data from 
# https://www.themoviedb.org/
# https://developers.themoviedb.org/3/search/search-movies
import requests

class MovieSeeker:
    """class for retriving data from the API"""

    def __init__(self, the_moviedb_api_key: str) -> None:
        self.the_moviedb_api_key = the_moviedb_api_key

    def get_data_movies(self, title: str) -> list[dict]:
        """
        get json data from the https://www.themoviedb.org/ api
        and return a list of dictionaries
        """
        # example
        # https://api.themoviedb.org/3/search/movie?api_key=your_key&language=en-US&query=star%20wars&page=1&include_adult=false
        base_api_endpoint = "https://api.themoviedb.org/3/search/movie"
        params = {
            'api_key': self.the_moviedb_api_key,
            'language': 'en-US',
            'query': title,
            'page': 1,
            'include_adult': 'false',
        }

        response = requests.get(base_api_endpoint, params=params)
        response.raise_for_status()

        data = response.json()
   
        if data['total_results'] > 0:
            # return a list of dictionaries
            new_movies = []
            for element in data['results']:
                new_dict = {
                    'title': element['title'],
                    'release_date': element['release_date'],
                    'overview': element['overview'],
                    'movie_id': element['id'],
                    # https://developers.themoviedb.org/3/getting-started/images
                    # example : https://image.tmdb.org/t/p/w500/kqjL17yufvn9OVLyXYpvtyrFfak.jpg
                    'poster_path': f"https://image.tmdb.org/t/p/w500{element['poster_path']}",
                }
                new_movies.append(new_dict)

            return new_movies
        else:
            return None


    def get_data_movie_detail(self, id: int) -> dict:
        """
        get json data from the https://www.themoviedb.org/ api
        and return a list of dictionaries
        """
        # example
        # https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_key>>&language=en-US
        base_api_endpoint = f"https://api.themoviedb.org/3/movie/{id}"
        params = {
            'api_key': self.the_moviedb_api_key,
            'language': 'en-US',
        }

        response = requests.get(base_api_endpoint, params=params)
        response.raise_for_status()

        data = response.json()

  
        # return a dictionary
        new_dict = {
            'title': data['title'],
            'release_date': data['release_date'],
            'overview': data['overview'],
            'movie_id': data['id'],
            'tagline': data['tagline'],
            # https://developers.themoviedb.org/3/getting-started/images
            # example : https://image.tmdb.org/t/p/w500/kqjL17yufvn9OVLyXYpvtyrFfak.jpg
            'poster_path': f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
        }
       
        return new_dict
