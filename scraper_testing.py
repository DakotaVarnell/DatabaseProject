def write_movies(table_name, id):

    ia = Cinemagoer()
    movie = ia.get_movie(id)

    try:
        revenue = int(str(movie['box office']['Cumulative Worldwide Gross']).split()[0].replace(',', '').replace('$', '').replace('}', '').replace("'", ''))
        budget = int(str(movie['box office']['Budget']).split()[0].replace(',', '').replace('$', '').replace('}', '').replace("'", ''))
    except:
        revenue = None
        budget = None


    info = [id, movie['title'], None, movie['rating'], str(movie['certification'][-4]).split(':')[1], revenue, budget]
    print(info)
    
    #writeInsertFile(info)

# def writeInsertFile(data):
#     print(data)





#Webscraper for the imdb website
from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

#Top 250 movies list
list_of_250 = ia.get_top250_movies()


for movie in list_of_250:
    write_movies(0, movie.movieID)


# ia = Cinemagoer()

# #Id for the sake of testing
# id = '0441773'

# # get a movie
# movie = ia.get_movie('0441773')

# #Update the keys of the movie to include these categories, not included by default
# ia.update(movie, ['reviews'])
# ia.update(movie, ['awards'])
# ia.update(movie, ['soundtrack'])

# #this will show you all available keys to search through
# print(sorted(movie.keys())) 


   

