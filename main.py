import time
import csv
from hashTables import *
from hashFunctions import *
from movie import Movie

#function to load the data from a file
def dataLoader ( filename ):

    movies = [] #empty list to hold the movies
    with open ( filename, newline='', encoding = 'latin-1' ) as file: #open the file for reading
        reader = csv.reader ( file )
        next ( reader ) #skip the header row
        for row in reader:
            title, genre, release_date, director, box_office_revenue, rating, duration_minutes, production_company, quote = row
            movies.append ( Movie ( title, genre, release_date, director, box_office_revenue, rating, duration_minutes, production_company, quote ) )
    return movies

def testHashTables ( movies, tableType, hashFunc, keyType ):
    #insert the movies into the hash tables and time the insertions
    size = len ( movies ) * 2 #set the table size to be twice the number of records to reduce collisions

    if tableType == "linkedList":
        ht = HashTable1 ( size, hashFunc ) #create a hash table for the linked list implementation
    else:
        ht = HashTable2 ( size, hashFunc ) #create a hash table for the linear probing implementation

    #Insert Time
    startTime = time.time() #start the timer
    for movie in movies:
        if keyType == "title":
            ht.insert ( movie.movie_title, movie ) #insert the movie into the hash table using the title as the key
        else:
            ht.insert ( movie.quote, movie ) #insert the movie into the hash table using the quote as the key

    insertTime = time.time() - startTime #end the timer

    #lookup time
    startTime = time.time() #start the timer
    for movie in movies:
        if keyType == "title":
            ht.lookup ( movie.movie_title ) #lookup the movie in the hash table using the title as the key
        elif keyType == "quote":
            ht.lookup ( movie.quote ) #lookup the movie in the hash table using the quote as the key

    lookupTime = time.time() - startTime #end the timer

    print ( "\nTable Type:                   ", tableType, ",", keyType, "Search" )
    print ( "Hash Function:                ", hashFunc.__name__ )
    print ( "HashTable Construction time:  ", insertTime )
    print ( "HashTable lookup time:        ", lookupTime )
    print ( "HashTable collisions:         ", ht.collisions )
    print ( "HashTable wasted space:       ", ht.find_wasted_space() )

def main():
    movies = dataLoader ( 'MOCK_DATA.csv' ) #load the movies from the file
    tableSize = len ( movies ) * 2 #set the table size to be twice the number of records to reduce collisions
    
    # #attempt 1: linked list implementation with poor hash function
    # print ( "\nAttempt 1:" )
    # testHashTables ( movies, "linkedList", linkedList_poor, "title" )
    # #attempt 2: linked list implementation with good hash function
    # print ( "\nAttempt 2:" )
    # testHashTables ( movies, "linkedList", linkedList_good, "title" )
    # #attempt 3: linked list implementation with better hash function
    # print ( "\nAttempt 3:" )
    # testHashTables ( movies, "linkedList", linkedList_better, "title" )
    # #attempt 4: linked list implementation with better2 hash function
    # print ( "\nAttempt 4:" )
    # testHashTables ( movies, "linkedList", linkedList_better2, "title" )
    #attempt 5: linked list implementation with best hash function
    # print ( "\nAttempt 5:" )
    # testHashTables ( movies, "linkedList", linkedList_best, "title" )
    # #attempt 6: linear probing implementation with good hash function
    # print ( "\nAttempt 6:" )
    # testHashTables ( movies, "linearProbing", linearProbing_poor, "quote" )
    # #attempt 7: linear probing implementation with poor hash function
    # print ( "\nAttempt 7:" )
    # testHashTables ( movies, "linearProbing", linearProbing_good, "quote" )
    # #attempt 8: linear probing implementation with better hash function
    # print ( "\nAttempt 8:" )
    # testHashTables ( movies, "linearProbing", linearProbing_better, "quote" )
    # #attempt 9: linear probing implementation with better2 hash function
    # print ( "\nAttempt 9:" )
    # testHashTables ( movies, "linearProbing", linearProbing_better2, "quote" )
    #attempt 10: linear probing implementation with best hash function
    print ( "\nAttempt 10:" )
    testHashTables ( movies, "linearProbing", linearProbing_best, "quote" )

if __name__ == "__main__":
    main()
