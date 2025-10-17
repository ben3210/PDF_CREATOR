class Book:
    def __init__(self, title = "", year_of_release = "", publisher = "", genre = "", author = "", price = ""):
        self.title = title
        self.year_of_release = year_of_release
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price
    
    def input_data(self):
        self.title = input("Title: ")
        self.year_of_release = input("Year of release: ")
        self.publisher = input("Publisher: ")
        self.genre = input("Genre: ")
        self.author = input("Author: ")
        self.price = input("Price: ")

    def output_data(self):
        print(f"Title: {self.title}")
        print(f"Year of release: {self.year_of_release}")
        print(f"Publisher: {self.publisher}")
        print(f"Genre: {self.genre}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")

    def print_title(self):
        print(f"Title: {self.title}")

    def print_year_of_release(self):
        print(f"Year of release: {self.year_of_release}")

    def print_publisher(self):
        print(f"Publisher: {self.publisher}")

    def print_genre(self):
        print(f"Genre: {self.genre}")

    def print_author(self):
        print(f"Author: {self.author}")

    def print_price(self):
        print(f"Price: {self.price}")

book = Book()
book.input_data()
print("-" * 20)
book.output_data()
print("-" * 20)
book.print_title()