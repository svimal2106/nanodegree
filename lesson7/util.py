import json
import requests


class Util:
    """
    Utility class which contains reusable static functions
    """
    def __init__(self):
        pass

    @staticmethod
    def read_file_as_json(file_name):
        """
        Read and return the JSON content in a file
        :param file_name: Name of the file
        :return: Dictionary object corresponding to the JSON in file
        """
        with open(file_name) as file:
            content = json.load(file)

        return content

    @staticmethod
    def __fetch_movie_info(imdb_url):
        """
        Fetch the content from an IMDb URL
        :param imdb_url: IMDb URL
        :return: Page content in string form or None
        """
        response = requests.get(imdb_url)
        if response.status_code == 200:
            return response.content
        else:
            None

    @staticmethod
    def __remove_html_if_present(rating_str):
        """
        Prune HTML content if present in the rating string
        :param rating_str: Rating string
        :return: IMDb rating
        """
        return rating_str.split('<')[0] if '<' in rating_str else rating_str

    @staticmethod
    def extract_rating(imdb_url):
        """
        Extract IMDb rating from the movie page URL
        :param imdb_url: IMDb URL
        :return: Rating of the movie
        """
        content = Util.__fetch_movie_info(imdb_url)
        if content:
            rating_index = content.find('<span class="rating">') + 21
            rating_str = content[rating_index:rating_index + 3]
            rating = Util.__remove_html_if_present(rating_str)
            return rating
        else:
            return "NA"

