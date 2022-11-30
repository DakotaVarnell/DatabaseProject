#Webscraper for the imdb website

import requests
from bs4 import BeautifulSoup
from imdb import Cinemagoer

#Our top 250 movies website url
sample_website='https://www.imdb.com/chart/top/'
  
# call get method to request the page
page=requests.get(sample_website)
  
# method and html parser created soup
soup = BeautifulSoup(page.content, 'html.parser')

#Create an empty list of ids
list_of_ids = []

#Find all a tags that are hrefs in the page contents
for i in soup.find_all('a', href = True):

    #The current tag contains href and starts with /title so its a title id
    if(str(i['href']).startswith('/title')):

        #Temp variable that will convert our tag to a string for parsing
        temp = str(i['href'])
        #Convert the string to a list to allow for us to split it on particular indices
        temp = list(temp)
        #Split the string on the indices that contain the title id
        temp = temp[9:16]
        #Convert the list back to a string using the join function and joining it to an empty string
        temp = ''.join(temp)
        #Append the title id string to our list of ids list
        list_of_ids.append(temp)

#Convert our list of ids to a set because sets cannot contain duplicates thus removing all duplicates
set_of_ids = set(list_of_ids)
#Convert back to a list so that we now have a list of 250 title ids which makes it easier for me(dakota) to work with rather than sets
list_of_ids = list(set_of_ids)

#Here we will create lists for each table's information
movie_table_info = []
directs_table_info = []
writes_table_info = []
contains_table_info = []
reviews_table_info = []
genres_table_info = []
languages_table_info = []
award_table_info = []
person_table_info = []
soundtrack_table_info = []
works_for_table_info = []


#iterates through every movie in the top 250 list
#for id in (list_of_ids):

# create an instance of the Cinemagoer class
ia = Cinemagoer()

#Id for the sake of testing
id = '0441773'

# get a movie
movie = ia.get_movie('0441773')

#Update the keys of the movie to include these categories, not included by default
ia.update(movie, ['reviews'])
ia.update(movie, ['awards'])
ia.update(movie, ['soundtrack'])

#this will show you all available keys to search through
#print(sorted(movie.keys())) 

#Movie Table Information
#Add the movie title id, name, popularity, imdb rating, certification, budget, gross box office revenue
#Popularity is not a category we can get from cinemagoer
movie_table_info.append(str("Change to Id Var"))
movie_table_info.append(str(movie))
movie_table_info.append(0)
movie_table_info.append(movie['rating'])
movie_table_info.append(str(movie['certification'][-4]).split(':')[1])
movie_table_info.append((int(str(movie['box office']).split()[1].replace(',', '').replace('$', '').replace('}', '').replace("'", ''))))
movie_table_info.append((int(str(movie['box office']).split()[-1].replace(',', '').replace('$', '').replace('}', '').replace("'", ''))))

#Directs Table Information
name_and_id = ''
for name in movie['directors']:
    name_and_id = str(name) + ' , ' + id
    directs_table_info.append(name_and_id)

#Writes Table Information
name_and_id = ''
for name in movie['writers']:
    if(str(name) == ''):
        donothing = True
    else:
        name_and_id = str(name) + ' , ' + id
        writes_table_info.append(name_and_id)   

#Contains Table Information
name_and_id = ''
contains_table_info.append(str(movie) + " Soundtrack" + " , " + str(id))

#Reviews Table Information
for review in movie['reviews']:
    username = str(review['author'])
    content = str(review['content'])
    rating = str(review['rating'])
    date = str(review['date'])
    movie_id = id
    review_information = (username + " , " + content + " , " + rating + " , " + date + " , " + movie_id)
    reviews_table_info.append(review_information)

#Genres Table Information
combined_genres = ''
count = 1
for genre in movie['genres']:
    if(count == len(movie['genres'])):
        combined_genres += genre
    else:
        combined_genres += genre + ","
        count += 1    
genres_table_info.append(str(combined_genres) + " , " + str(id))

#Languages Table Information
combined_languages = ''
count = 1
for language in movie.data['languages']:
    if(count == len(movie['languages'])):
        combined_languages += language
    else:
        combined_languages += language + ","
        count += 1    
languages_table_info.append(str(combined_languages) + " , " + str(id))

#!!Dont really know how to do the movie/actor/director/writer receives part so skipping it!!
#Awards Table Information
for award in movie['awards']:
    movie_id = id
    award_name = str(award['award'])
    year = str(award['year'])
    event = str(award['category'])
    


# #Person Table Information
# people_list = movie['cast'] + movie['directors'] + movie['writers']
# person_id_list = []
# for i in range(len(people_list)):
#     person_id = str(people_list).split(",")[i].split(":")[1].replace("[http] name", "")
#     if(person_id == 'None'):
#         cont = True
#     else:
#         person_id_list.append(person_id)
   
# for person_id in person_id_list:
#     search = ia.get_person(person_id)
#     filmography = ia.get_person_filmography(person_id)
#     try:
#         birth_date  = search['birth date']
#         hometown = search['birth info']['birth place']
#         gender = 'not in cinemagoer'
#         spouse = 'not in cinemagoer'
#         children = 'not in cinemagoer'
#         parents = 'not in cinemagoer'
#         number_of_movies = len(filmography)
        
#         movie_name = filmography['data']['filmography'][0]['actor'][0]
#         print(movie_name)

        
#     except:
#         birth_date = ''
#         hometown = ''
#         gender = ''

#Soundtrack Table Information

#Works For Table Information



print(movie_table_info)
############################################################################
#Database Connection Section
import cx_Oracle
 
# Load data from a csv file into Oracle table using executemany
try:
    con = cx_Oracle.connect('system/password@localhost')
 
except cx_Oracle.DatabaseError as er:
    print('There is an error in Oracle database:', er)
 
else:
    try:
        cur = con.cursor()

        #All these tables will change to the proper information once we iterate through movies
        movie_data = [[movie_table_info[0], movie_table_info[1], movie_table_info[2], movie_table_info[3], movie_table_info[4] ,movie_table_info[5], movie_table_info[6]]]
        #review_data = [[reviews_table_info[0]], reviews_table_info[1], reviews_table_info[2], reviews_table_info[3], reviews_table_info[4]]
        cur = con.cursor()
        # Inserting multiple records into employee table
        # (:1,:2,:3) are place holders. They pick data from a list supplied as argument
        cur.executemany('insert into movie values(:1,:2,:3,:4,:5,:6,:7)', movie_data)
        #cur.executemany('insert into reviews values(:1,:2,:3,:4,:5)', review_data)

 
    except cx_Oracle.DatabaseError as er:
        print('There is an error in Oracle database:', er)
 
    except Exception as er:
        print(er)
 
    else:
        # To commit the transaction manually
        con.commit()
        print('Multiple records are inserted successfully')
 
finally:
    if cur:
        cur.close()
    if con:
        con.close()
