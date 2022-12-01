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

def write_directors(table_name, id):
    movie = ia.get_movie(id)
    director_list = []
    
    try:
        for name in movie['directors']:
            
            if(str(name) == ''):
                doNothing = True
            elif(str(name) in director_list):
                doNothing = True
            else:
                director_list.append(str(name))
        
        for name in director_list:
            info = [str(name), id]
            writeInsertFile('Directs', info)
    except:
        info = ['', id]
        writeInsertFile('Directs', info)


def write_writers(table_name, id):
    movie = ia.get_movie(id)
    writer_list = []
    
    try:
        for name in movie['writers']:
            
            if(str(name) == ''):
                doNothing = True
            elif(str(name) in writer_list):
                doNothing = True
            else:
                writer_list.append(str(name))
        
        for name in writer_list:
            info = [str(name), id]
            writeInsertFile('Writes', info)
    except:
        info = ['', id]
        writeInsertFile('Writes', info)

ia = Cinemagoer()
list_of_250 = ia.get_top250_movies()

for movie in list_of_250:
    #write_movies('Movie', movie.movieID)
    write_directors('Directs', movie.movieID)
    write_writers('Writes', movie.movieID)