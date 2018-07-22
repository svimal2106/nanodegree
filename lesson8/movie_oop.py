class Video:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def to_string(self):
        return "Video(" + self.title + "," + self.duration + ")"


class Movie(Video):
    def __init__(self, title, duration, poster_url, video_url):
        Video.__init__(self, title, duration)
        self.poster_url = poster_url
        self.video_url = video_url



class TVShow(Video):
    def __init__(self, title, duration, episode, season):
        Video.__init__(self, title, duration)
        self.episode = episode
        self.season = season

    def to_string(self):
        parent_str = Video.to_string(self)
        return parent_str + "," + "TVShow(" +  ",".join([self.episode, self.season]) + ")"


m = Movie("Swades", "3:00", "p1", "v1")
t = TVShow("Friends", "00:30", "5", "12")

print m.to_string()
print t.to_string()
