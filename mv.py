import fresh_tomatoes
import media
#stoy_story = media.Movie("toy Story", "A story of a boy and his toys that com to life",
	                     #"https://upload.wikimedia.org/wikipedia/en/1/12/Toy_story.jpg",
	                     #"https://ww.youtube.com/wath?v=vwyZH85NQC4")

#avatar = media.Movie("avatar", "A marine on an alien planet",
	                     #"https://upload.wikimedia.org/wikipedia/id/b/b0/avatar-Teaset-poster.jpg",
	                     #"https://www.youtube.com/watch?v=cX0R3mXaod8")


#RainMan = media.Movie("Rain Man", "Raymond, the autistic genius who directed artist Dustin Hoffman, who won the Oscars in 1989 for his role as the best actor, is the main actor.",
	                     #"https://upload.wikimedia.org/wikipedia/id/b/b0/Rain-Man-poster.jpg",
	                     #"https://youtu.be/mlNwXuHUA8I")

toy_story = media.Movie('TOY STORY' , 'A story of a boy and his toys that come to life','https://www.impawards.com/1995/posters/toy_story_ver1.jpg','https://www.youtube.com/watch?v=KYz2wyBy3kc')
#print(toy_story.poster_image_url)

avatar = media.Movie('AVATAR','alien planet','https://www.impawards.com/2009/posters/avatar_ver4.jpg','https://www.youtube.com/watch?v=5PSNL1qE6VY')
#print(avatar.storyline)
#print(avatar.poster_image_url)
#toy_story.show_trailer()

Finding_Nemo = media.Movie('Finding_Nemo','A clown fish named Marlin lives in the Great Barrier Reef loses his son','https://www.impawards.com/2003/posters/finding_nemo.jpg','https://www.youtube.com/watch?v=yDPRaVX2p8c')
#print Finding_nemo.show_trailer()

Lord_of_the_rings = media.Movie('Lord_of_the_rings','is an epic high fantasy novel written by English author' ,'https://ia.media-imdb.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_SY999_CR0,0,673,999_AL_.jpg','https://www.youtube.com/watch?v=Pki6jbSbXIY')

RATATOUILLE = media.Movie('RATATOUILLE', '"Ratatouille" is the first one that made me positively desire one.','https://static.rogerebert.com/uploads/movie/movie_poster/ratatouille-2007/large_taAPNsf6G4EXBYSG7Jyvd9HHKnH.jpg','https://www.youtube.com/watch?v=ALUmKa_mpik')

Men_in_black =media.Movie('Men_in_black',' is a series of American science fiction action comedy films directed by Barry Sonnenfeld, and based on Malibu / Marvel comic book series ','https://ia.media-imdb.com/images/M/MV5BMTU2NTYxODcwMF5BMl5BanBnXkFtZTcwNDk1NDY0Nw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg','https://www.youtube.com/watch?v=1Q4mhYF9aQQ')

#RainMan.show_trialer()
movies = [toy_story, avatar, Finding_Nemo, Lord_of_the_rings,RATATOUILLE, Men_in_black]
fresh_tomatoes.open_movies_page(movies)
