#Webscraper for the imdb website
from imdb import Cinemagoer
import cx_Oracle
actor_IDs = set()
director_IDs = set()
writer_IDs = set()

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


def update_person_flag(type, id):
    testFile = open('insertFile.sql', 'a')
    print("Still Running\n")
    person = ia.getperson(id)  #########underscore
    try:
        name = person['name']
        print(name)
    except KeyError:
        name = person.myName
        print(name)
    query = "\nUPDATE Person\n\t" + "SET " + type +"_Flag = 'y'\n\tWHERE Name = '" + name + "';"
    try:
        testFile.write(query)
    except:
        print("Error writing to file\n")


def write_person(table_name, mID):

    #get all actors/actresses, directors, writers in movie
    movie = ia.get_movie(mID)
    personIDs = set()
    a_list = movie['cast']
    aIDs = []
    d_list = movie['directors']
    dIDs = []
    w_list = movie['writers']
    wIDs = []

    #checks for person row and updates flags if needed otherwise appends ids to be added
    for i in range(len(a_list)):
        person_id = str(a_list).split(",")[i].split(":")[1].replace("[http] name", "")
        if(person_id == 'None'):
            cont = True
        else:
            if person_id in actor_IDs:
                print('Actor')
                update_person_flag('Actor', person_id)
            else:
                aIDs.append(person_id)
            actor_IDs.add(person_id)
    for i in range(len(d_list)):
        person_id = str(d_list).split(",")[i].split(":")[1].replace("[http] name", "")
        if(person_id == 'None'):
            cont = True
        else:
            if person_id in director_IDs:
                print('Director')
                update_person_flag('Director', person_id)
            else:
                dIDs.append(person_id)
            director_IDs.add(person_id)
    for i in range(len(w_list)):
        person_id = str(w_list).split(",")[i].split(":")[1].replace("[http] name", "")
        if(person_id == 'None'):
            cont = True
        else:
            if person_id in writer_IDs:
                print('Writer')
                update_person_flag('Writer', person_id)
            else:
                wIDs.append(person_id)
            writer_IDs.add(person_id)

    #adds all actors, directors, and writers to be added on one list
    personIDs = aIDs + dIDs + wIDs
    print(personIDs)
    print(len(personIDs))

    #iterates through each person
    for id in personIDs:
        person = ia.get_person(id)
        
        print(person.infoset2keys)

        try:
            name = person.data['name']
            print(name)
        except KeyError:
            name = person.myName
            print(name)
            # try:
            #     name = person['name']
            #     print(name)
            # except:
            #     name = ''
        try:
            birth_date  = person['birth date']
            print(birth_date)
        except:
            birth_date = ''
        try:
            hometown = person['birth notes']        
            print('notes: ',hometown)
        except:
            hometown = ''        
        try:
            gender = 'x'
        except:
            gender = 'z'
        try:
            number_of_movies=0
            for film in person['filmography'].keys():
                for movie in person['filmography'][film]:
                    number_of_movies+=1
            print('num films',number_of_movies)
        except:
            number_of_movies = 1
            print('num movies',number_of_movies)

        aFlag, wFlag, dFlag = '', '', ''
        if id in actor_IDs:
            print('Actor')
            aFlag = 'y'
        if id in writer_IDs:
            print('Writer')
            wFlag = 'y'
        if id in director_IDs:
            print('Director')
            dFlag = 'y'

        info = [name, str(birth_date), hometown, gender, number_of_movies, aFlag, wFlag, dFlag]
        writeInsertFile(table_name,info)

def write_soundtrack(table_name, id):
    movie = ia.get_movie(id)
    ia.update(movie, ['soundtrack'])
    soundtrack = []
    try:
        for soundtrack in movie['soundtrack']:
           individual_items = str(soundtrack).split(":")
           song_title = individual_items[0].replace("{", '')
           writer = individual_items[2].split(",")[0]
           performer = individual_items[3].split(",")[0]
           soundtrack = [str(movie) + "Soundtrack", song_title, writer, performer]            
    except:
           soundtrack = [str(movie) + "Soundtrack", '', '', '']
    writeInsertFile('Soundtrack', soundtrack)

def write_contains(table_name, id):
    movie = ia.get_movie(id)
    ia.update(movie, ['soundtrack'])
    contains = []
    try:
        for contains in movie['soundtrack']:
            contains = [str(movie) + "Soundtrack", id]            
    except:
           contains = [str(movie) + "Soundtrack", id]
    writeInsertFile('Contains', contains)


# create an instance of the Cinemagoer class
ia = Cinemagoer()
list_of_250 = ia.get_top250_movies()

for movie in list_of_250:
    # write_movies('Movie', movie.movieID)
    # write_directors('Directs', movie.movieID)
    # write_writers('Writes', movie.movieID)
    # write_reviews('Reviews', movie.movieID)
    # write_soundtrack('Contains', movie.movieID)
    # write_contains('Contains', movie.movieID)
    write_person('Person', movie.movieID)