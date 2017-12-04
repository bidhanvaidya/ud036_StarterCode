import fresh_tomatoes
import media
deadpool2= media.Movie("DeadPool2",
                       "https://upload.wikimedia.org/wikipedia/en/c/cf/Deadpool_2_poster.jpg",
                       "https://www.youtube.com/watch?v=5V2X6cnSoxM")
avengers= media.Movie("Avengers",
                      "https://upload.wikimedia.org/wikipedia/en/9/90/Avengers_Infinity_War.jpg",
                      "https://www.youtube.com/watch?v=6ZfuNTqbHE8")
black_panther= media.Movie("Black Panther",
                           "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
                           "https://www.youtube.com/watch?v=vt9UZo32KMk")
man_of_steel = media.Movie("Man of Steel 2",
                           "https://upload.wikimedia.org/wikipedia/en/8/85/ManofSteelFinalPoster.jpg",
                           "https://www.youtube.com/watch?v=dPl3_r9rf8E")
alpha = media.Movie("Alpha",
                    "https://upload.wikimedia.org/wikipedia/en/7/72/Alpha_%28film%29.jpg",
                    "https://www.youtube.com/watch?v=uIxnTi4GmCo")
dragonheart= media.Movie("DRAGONHEART",
                         "https://upload.wikimedia.org/wikipedia/en/1/18/Dragonheart_ver1.jpg",
                         "https://www.youtube.com/watch?v=1j1gfHwLICo")
movies_list=[deadpool2, avengers, black_panther, man_of_steel, alpha, dragonheart] #array of movies

fresh_tomatoes.open_movies_page(movies_list) # creating web page using list of movies from movie_list
