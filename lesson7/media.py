class Video:
    """
    Base class which denotes a video entity
    """
    def __init__(self, title, duration, storyline, rating=None):
        self.title = title
        self.duration = duration
        self.storyline = storyline
        self.rating = rating


class Movie(Video):
    """
    Movie class which holds information related to a movie entity
    """
    def __init__(self, title, storyline, duration, poster_url, trailer_url, rating, release_date=None):
        Video.__init__(self, title, duration, storyline, rating)
        self.poster_url = poster_url
        self.trailer_url = trailer_url
        self.release_date = release_date


class TvEpisode(Video):
    """
    TV Episode class which holds information related to a TV serial episode
    """
    def __init__(self, title, storyline, duration, channel, rating, air_date):
        Video.__init__(title, duration, storyline, rating)
        self.channel = channel
        self.air_date = air_date
