#Webscraper for the imdb website
from imdb import Cinemagoer
import cx_Oracle


def writeInsertFile(tableName, infoList):
    testFile = open('insertFile.sql', 'a')

    query = "\ninsert into " + tableName + "\n" + "\t" + "values("

    print("Still Running\n")

    for attribute in infoList:
        if (type(attribute) == int):
            query+= str(attribute) + ","
        elif (type(attribute) == float):
            query+= str(attribute) + ","
        else:
            query+= "\'" + attribute + "\'" + ","
    
    query = query.rstrip(query[-1])
    query += ');'

    testFile.write(query)

def write_movies(table_name, id):
    movie = ia.get_movie(id)

    try:
        revenue = int(str(movie['box office']['Cumulative Worldwide Gross']).split()[0].replace(',', '').replace('$', '').replace('}', '').replace("'", ''))
        budget = int(str(movie['box office']['Budget']).split()[0].replace(',', '').replace('$', '').replace('}', '').replace("'", ''))
    except:
        revenue = ''
        budget = ''


    info = [id, movie['title'], '', movie['rating'], str(movie['certification'][-4]).split(':')[1], revenue, budget]
    writeInsertFile('Movie', info)

ia = Cinemagoer()
list_of_250 = ia.get_top250_movies()

for movie in list_of_250:
    write_movies(0, movie.movieID)