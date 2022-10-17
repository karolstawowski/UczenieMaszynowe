class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Biblioteka w mieście {self.city} na ulicy {self.street}. Kod pocztowy: {self.zip_code}. Numer telefonu: {self.phone}. Godziny otwarcia: {self.open_hours}'


class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date, birth_date, city: str,
                 street: str, zip_code: str, phone: str):
        self.phone = phone
        self.zip_code = zip_code
        self.street = street
        self.city = city
        self.birth_date = birth_date
        self.hire_date = hire_date
        self.last_name = last_name
        self.first_name = first_name

    def __str__(self):
        return f'Pracownik {self.first_name} {self.last_name}. Zamieszkały: {self.street} {self.zip_code} {self.city}. Numer telefonu: {self.phone}. Zatrudniony {self.hire_date}. Urodzony {self.birth_date}'


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.number_of_pages = number_of_pages
        self.author_surname = author_surname
        self.author_name = author_name
        self.publication_date = publication_date
        self.library = library

    def __str__(self):
        return f'Książka autorstwa {self.author_name} {self.author_surname} opublikowana {self.publication_date} zawiera {self.number_of_pages} stron znajduje się w {self.library}'


class Order:
    def __init__(self, employee, student, books, order_date):
        self.order_date = order_date
        self.books = books
        self.student = student
        self.employee = employee

    def __str__(self):
        return f'Zamówienie studenta {self.student} zrealizowane {self.order_date} przez {self.employee} na książki: {self.books}'


l1 = Library("Katowice", "Chorzowska", "40-012", "10-18", "123456789")
l2 = Library("Katowice", "Mikołowska", "40-014", "8-18", "123456798")

b1 = Book(l1, "17/04/2001", "Jan", "Nowak", 310)
b2 = Book(l2, "12/07/2011", "Andrzej", "Adamski", 310)
b3 = Book(l1, "22/01/2022", "Halina", "Klementynowicz", 310)
b4 = Book(l1, "16/12/2008", "Jan", "Szpak", 310)
b5 = Book(l2, "02/03/1993", "Józef", "Mnich", 310)

e1 = Employee("Eugeniusz", "Smolarek", "20/08/2009", "10/02/1968", "Wadowice", "Biskupińska", "22-012", "654234765")
e2 = Employee("Stanisław", "Lato", "20/08/2009", "12/03/1985", "Kraków", "Biskupińska", "22-012", "686534765")
e3 = Employee("Stanisława", "Zima", "20/08/2009", "24/11/1998", "Dąbrowa Górnicza", "Wolności", "22-012", "654234235")

o1 = Order(e1, "Radosław Żółk", [b1, b2], "01/02/2010")
print(o1)
o2 = Order(e3, "Przemysław Gęś", [b3, b2], "04/03/2011")
print(o2)
