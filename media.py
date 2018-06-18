import webbrowser
"""You got it! When we create the instance brad, the init function inside the class Turtle gets called."""
class Movie():
	def __init__(udacity, movie_tiles, story, poster_image_url, trailer_youtube_url):
		udacity.title = movie_tiles
		udacity.storyline = story
		udacity.poster_image_url = poster_image_url
		udacity.trailer_youtube_url = trailer_youtube_url
	def show_trialer(udacity):
		webbrowser.open(udacity.trailer_youtube_url)