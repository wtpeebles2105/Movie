import webbrowser


"""This is the wider class of the two I used, all movies fall into it because
    it denotes both title of the move and its runtime which all videos
    contain

    Attributes:
    Title: The Title of the Movie
    Runtime: The Duration of the Movie from start to finish
"""

class Video():

    """Initalizing and creating space in memory for what is about to be
        created. "self" is the object or instance being created.
    """
    def __init__(self, runtime, movie_title):
        self.title = movie_title
        self.runtime = runtime

# I wanted to make sure I understood inheritance so I pulled out movie
# title and runtime to make the class Movie pull them in from Video.
"""This class provides more information about the movie, it also will pull
    from its parent class of Video for title and runtime

    New Attributes:
    Storyline: Brief description of the movie
    Director: Name of movie's Director
    release_date: The date the movie was released in theatres
    poster_image_url: The URL address of a poster to the movie
    trailer_youtube: A link to YouTube.com with a trailer of the movie

    Inherited Attributes From Video:
    Title: The Title of the Movie
    Runtime: The Duration of the Movie from start to finish
"""

class Movie (Video):
    def __init__(self, movie_title, runtime, storyline, director,
                 release_date, poster_image, trailer_youtube):
        """Below is where the Class video has its inheriance traits imported
        into the new class Movie
        """
        Video.__init__(self, runtime, movie_title)
        self.storyline = storyline
        self.director = director
        self.release = release_date
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This is a function built into Phython, since webbrowser was
        imported we can now call upon its open function using a class we
        defined above
        """
        webbrowser.open(self.trailer_youtube_url)
