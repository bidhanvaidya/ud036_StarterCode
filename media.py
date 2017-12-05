class Movie():
    """
        Movies, also known as films, are a type of visual communication which 
        uses moving pictures and sound to tell stories.
    """
    def __init__(self, movie_title, poster_image_url, trailer_youtube_id):
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_id
