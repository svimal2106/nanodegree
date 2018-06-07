from media import Movie
from fresh_tomatoes import open_movies_page

toy_story = Movie("Toy Story", "A Story of boy with hi toys",
                  "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                  "https://www.youtube.com/watch?v=rNk1Wi8SvNc")

ted = Movie("Ted", "A Teddy bear comes to life",
            "https://upload.wikimedia.org/wikipedia/en/6/62/Ted_poster.jpg",
            "https://www.youtube.com/watch?v=9fbo_pQvU7M")

rnbdj = Movie("Rab ne bana di jodi", "SRK and Anushka",
              "https://upload.wikimedia.org/wikipedia/en/a/ab/Rab_Ne_Bana_Di_Jodi.jpg",
              "https://www.youtube.com/watch?v=eBi8syxPd14")

swades = Movie("Swades", "SRK All time favorite",
               "https://upload.wikimedia.org/wikipedia/en/8/85/Swades_poster.jpg",
               "https://www.youtube.com/watch?v=vc7AZNWvs0M")

warrior = Movie("Warrior", "Two brothers against each other in wrestling",
                "https://upload.wikimedia.org/wikipedia/en/e/e3/Warrior_Poster.jpg",
                "https://www.youtube.com/watch?v=I5kzcwcQA1Q")

rdb = Movie("Rang De Basanti", "Youngsters with situational patriotism",
            "https://upload.wikimedia.org/wikipedia/en/0/08/Rang_De_Basanti_poster.jpg",
            "https://www.youtube.com/watch?v=jW0Io8yB638")

movie_list = [toy_story, ted, rnbdj, swades, warrior, rdb]
open_movies_page(movie_list)