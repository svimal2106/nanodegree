import webbrowser
#from PIL import Image
import requests
from io import BytesIO


class Movie:

    def __init__(ref, movie_title, movie_storyline, poster_image, trailer_youtube):
        ref.title = movie_title
        ref.storyline = movie_storyline
        ref.poster_image_url = poster_image
        ref.trailer_url = trailer_youtube