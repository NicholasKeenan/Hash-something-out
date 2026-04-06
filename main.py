import time
from hashTables import *
from hashFunctions import *
from movie import Movie

#function to load the data from a file
def dataLoader ( filename ):

    movies = [] #empty list to hold the movies
    with open ( filename, 'r' ) as file: #open the file for reading
        for line in file:
            title, genre, release_date, director, box_office_revenue, rating, duration_minutes, production_company, quote = line.strip().split ( ',' )
            movies.append ( Movie ( title, genre, release_date, director, box_office_revenue, rating, duration_minutes, production_company, quote ) )
    return movies

def testHashTables ( movies, hash_table1, hash_table2, keyType, tableSize, hashFunc1, hashFunc2 ):
    #insert the movies into the hash tables and time the insertions
    start_time = time.time()
    for movie in movies:
        if keyType == 'title':
            hash_table1.insert ( movie.movie_title, movie )
        else:
            hash_table1.insert ( movie.quote, movie )
    end_time = time.time()
    print ( f"Hash Table 1 ({hashFunc1}): {end_time - start_time} seconds to insert {len(movies)} records" )

    start_time = time.time()
    for movie in movies:
        if keyType == 'title':
            hash_table2.insert ( movie.movie_title, movie )
        else:
            hash_table2.insert ( movie.quote, movie )
    end_time = time.time()
    print ( f"Hash Table 2 ({hashFunc2}): {end_time - start_time} seconds to insert {len(movies)} records" )

    #lookup the movies in the hash tables and time the lookups
    start_time = time.time()
    for movie in movies:
        if keyType == 'title':
            hash_table1.lookup ( movie.movie_title )
        else:
            hash_table1.lookup ( movie.quote )
    end_time = time.time()
    print ( f"Hash Table 1 ({hashFunc1}): {end_time - start_time} seconds to lookup {len(movies)} records" )

    start_time = time.time()
    for movie in movies:
        if keyType == 'title':
            hash_table2.lookup ( movie.movie_title )
        else:
            hash_table2.lookup ( movie.quote )
    end_time = time.time()
    print ( f"Hash Table 2 ({hashFunc2}): {end_time - start_time} seconds to lookup {len(movies)} records" )

def main():
    movies = dataLoader ( 'MOCK_DATA.csv' ) #load the movies from the file
    tableSize = len ( movies ) * 2 #set the table size to be twice the number of records to reduce collisions

    #List containing the hash functions to be tested
    hashFunctions = [ 
        linkedList_poor, 
        linkedList_good, 
        linearProbing_poor, 
        linearProbing_good 
        ]
    
    for i in hashFunctions

if __name__ == "__main__":
    main()
