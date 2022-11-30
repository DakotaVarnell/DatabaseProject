#Webscraper for the imdb website
from imdb import Cinemagoer


#iterates through every movie in the top 250 list
#for id in (list_of_ids):

# create an instance of the Cinemagoer class
ia = Cinemagoer()

#Top 250 movies list
list_of_250 = ia.get_top250_movies()


#Update the keys of the movie to include these categories, not included by default
ia.update(list_of_250, ['reviews'])
ia.update(list_of_250, ['awards'])
ia.update(list_of_250, ['soundtrack'])

