class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str,
                 phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Biblioteka w mieście {self.city} na ulicy {self.street}. ' \
               f'Kod pocztowy: {self.zip_code}. ' \
               f'Numer telefonu: {self.phone}. ' \
               f'Godziny otwarcia: {self.open_hours}'
