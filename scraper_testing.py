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
    try:
        testFile.write(query)
    except:
        print("Error writing to file\n")

def write_movies(table_name, id):
    movie = ia.get_movie(id)

    try:
        revenue = int(str(movie['box office']['Cumulative Worldwide Gross']).split()[0].replace(',', '').replace('$', '').replace('}', '').replace("'", ''))
        budget = int(str(movie['box office']['Budget']).split()[0].replace(',', '').replace('$', '').replace('}', '').replace("'", ''))
    except:
        revenue = ''
        budget = ''

    info = [id, str(movie['title']).replace("'", ''), '', movie['rating'], str(movie['certification'][-4]).split(':')[1], revenue, budget]
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
            info = [str(name).replace("'", ''), id]
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
            info = [str(name).replace("'", ''), id]
            writeInsertFile('Writes', info)
    except:
        info = ['', id]
        writeInsertFile('Writes', info)

def write_reviews(table_name, id):
    movie = ia.get_movie(id)
    ia.update(movie, ['reviews'])
    reviews = []
    try:
        for review in movie['reviews']:
            username = str(review['author'])
            content = str(review['content']).replace("'", '')
            if review['rating'] == None:
                rating = 0  
            else:
                rating = int(str(review['rating']))  

            info = [username, content, rating, str(review['date']), id]
            reviews.append(info)
    except:
           info = [username, content, 0, str(review['date']), id]
    writeInsertFile('Reviews', info)


ia = Cinemagoer()
list_of_250 = ia.get_top250_movies()

for movie in list_of_250:
    write_movies('Movie', movie.movieID)
    write_directors('Directs', movie.movieID)
    write_writers('Writes', movie.movieID)
    write_reviews('Reviews', movie.movieID)