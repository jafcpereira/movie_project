import fresh_tomatoes

class Movie(object):
    """A python class that contains data about a movie"""

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url 

movie_list = [Movie("Mundo Jurassico - Reino Caido", 
"https://m.media-amazon.com/images/M/MV5BNzIxMjYwNDEwN15BMl5BanBnXkFtZTgwMzk5MDI3NTM@._V1_.jpg",
"https://www.youtube.com/watch?v=1FJD7jZqZEk"),
Movie("The Incredibles 2", 
"https://m.media-amazon.com/images/M/MV5BMTEzNzY0OTg0NTdeQTJeQWpwZ15BbWU4MDU3OTg3MjUz._V1_SY1000_CR0,0,674,1000_AL_.jpg",
"https://www.youtube.com/watch?v=i5qOzqD9Rms"),
Movie("Vingadores - Guerra do Infinito",
"https://m.media-amazon.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
"https://www.youtube.com/watch?v=6ZfuNTqbHE8")]

fresh_tomatoes.open_movies_page(movie_list)