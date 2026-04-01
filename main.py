import time
from hashTables import *
from movie import Movie

#function to load the data from a file
def dataLoader ( filename ):

    movies = [] #empty list to hold the movies
    with open ( filename, 'r' ) as file: #open the file for reading
        for line in file:
            title, genre, release_date, director, box_office_revenue, rating, duration_minutes, production_company, quote = line.strip().split ( ',' )
            movies.append ( Movie ( title, genre, release_date, director, box_office_revenue, rating, duration_minutes, production_company, quote ) )
    return movies