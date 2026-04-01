#A simple implementation of a hash table in python

#movie class to hold title and quote
class Movie:
    def __init__ ( self, movie_title, genre, release_date, director, box_office_revenue, rating, duration_minutes, production_company, quote ):
        self.movie_title = movie_title
        self.genre = genre
        self.release_date = release_date
        self.director = director
        self.box_office_revenue = box_office_revenue
        self.rating = rating
        self.duration_minutes = duration_minutes
        self.production_company = production_company
        self.quote = quote

    def __str__(self):
        return f"{self.movie_title} ({self.genre}): '{self.quote} ' - Directed by {self.director}, Released on {self.release_date}, Box Office: ${self.box_office_revenue}, Rating: {self.rating}/10, Duration: {self.duration_minutes} minutes, Produced by {self.production_company}"

#function to load the data from a file
def dataLoader ( filename ):

    movies = [] #empty list to hold the movies
    with open ( filename, 'r' ) as file: #open the file for reading
        for line in file:
            title, genre, release_date, director, box_office_revenue, rating, duration_minutes, production_company, quote = line.strip().split ( ',' )
            movies.append ( Movie ( title, genre, release_date, director, box_office_revenue, rating, duration_minutes, production_company, quote ) )
    return movies

###Hash Table 1###
#This implementation will use a movie class as the backbone
#where the title of the movie will be the key to store and retrieve the records
