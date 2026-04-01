#movie class to hold data for each movie record, this will be used as the value in the hash tables
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
    