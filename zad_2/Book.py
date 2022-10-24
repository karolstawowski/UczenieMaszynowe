class Book:
    def __init__(self, library, publication_date, author_name, author_surname,
                 number_of_pages):
        self.number_of_pages = number_of_pages
        self.author_surname = author_surname
        self.author_name = author_name
        self.publication_date = publication_date
        self.library = library

    def __str__(self):
        return f'Książka autorstwa {self.author_name} {self.author_surname} ' \
               f'opublikowana {self.publication_date} ' \
               f'zawiera {self.number_of_pages} stron ' \
               f'znajduje się w {self.library}'
