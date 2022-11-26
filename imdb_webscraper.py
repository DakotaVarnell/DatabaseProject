#Webscraper for the imdb website

import requests
from bs4 import BeautifulSoup

#Our top 250 movies website url
sample_website='https://www.imdb.com/chart/top/'
  
# call get method to request the page
page=requests.get(sample_website)
  
# with the help of BeautifulSoup
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
#Convert back to a list so that we now have a list of 250 title ids whcih makes it easier for me(dakota) to work with rather than sets
list_of_ids = list(set_of_ids)

print('Len of list: '  + str(len((list_of_ids))))
print("\nList of ID's:")
print(list_of_ids)
        
