from argparse import ArgumentParser
from util import Util
from media import Movie
from fresh_tomatoes import open_movies_page

# TODO
# Add logging

class EntertainmentCenter:
    """
    Class which acts as interface to backend system
    """
    def __init__(self):
        pass

    @staticmethod
    def construct_and_open_movie_page(movie_file):
        """
        Construct the movie list and open the trailer page

        :param movie_file: File name containing the details of favorite movies
        :return: None
        """
        movie_content = Util.read_file_as_json(movie_file)
        movie_list = []
        for movie_entry in movie_content:
            imdb_rating = Util.extract_rating(movie_entry["imdb_url"])
            movie_instance = Movie(movie_entry["title"], movie_entry["storyline"], movie_entry["duration"],
                                   movie_entry["poster_url"], movie_entry["trailer_url"], imdb_rating)
            movie_list.append(movie_instance)
        open_movies_page(movie_list)


if __name__ == "__main__":
    parser = ArgumentParser("Parser to get movie website related information")
    parser.add_argument("movie_file", type=str, help="File containing information about movies in JSON format")
    args = parser.parse_args()
    movie_content_file = args.movie_file
    EntertainmentCenter.construct_and_open_movie_page(movie_content_file)