import fresh_tomatoes
import media
deadpool2 = media.Movie("DeadPool2",
                        "http://bit.ly/2jeoMge",
                        "https://www.youtube.com/watch?v=5V2X6cnSoxM"  # Noqa
                        )
avengers = media.Movie("Avengers",
                       "http://bit.ly/2AsrtV8",
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8"  # Noqa
                       )
black_panther = media.Movie("Black Panther",
                            "http://bit.ly/2iP99Pv",
                            "https://www.youtube.com/watch?v=vt9UZo32KMk"  # Noqa
                            )
man_of_steel = media.Movie("Man of Steel 2",
                           "http://bit.ly/1r978vW",
                           "https://www.youtube.com/watch?v=dPl3_r9rf8E"  # Noqa
                           )
alpha = media.Movie("Alpha",
                    "http://bit.ly/2ijAl4Z",
                    "https://www.youtube.com/watch?v=uIxnTi4GmCo"  # Noqa
                    )
dragonheart = media.Movie("DRAGONHEART",
                          "http://bit.ly/2nuYc7i",
                          "https://www.youtube.com/watch?v=1j1gfHwLICo"  # Noqa
                          )
# array of movies
movies_list = [deadpool2, avengers, black_panther,
               man_of_steel, alpha, dragonheart]
# creating web page using list of movies from movie_list
fresh_tomatoes.open_movies_page(movies_list)
