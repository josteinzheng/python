import webbrowser

class Movie():
    """This class represent a movie category"""
    def __init__(self, title, storyline, posterImage, trailerUrl):
        self.title = title
        storyline = storyline
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailerUrl
        
    def showTrailer(self):
        webbrowser.open(self.trailerUrl)
