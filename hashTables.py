class Movie:
    def __init__(self, title, quote):
        self.title = title
        self.quote = quote

    def __str__(self):
        return f"{self.title}: '{self.quote}'"