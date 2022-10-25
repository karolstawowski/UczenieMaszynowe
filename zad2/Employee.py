class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date, birth_date,
                 city: str, street: str, zip_code: str, phone: str):
        self.phone = phone
        self.zip_code = zip_code
        self.street = street
        self.city = city
        self.birth_date = birth_date
        self.hire_date = hire_date
        self.last_name = last_name
        self.first_name = first_name

    def __str__(self):
        return f'Pracownik {self.first_name} {self.last_name}. ' \
               f'Zamieszkały: {self.street} {self.zip_code} {self.city}. ' \
               f'Numer telefonu: {self.phone}. ' \
               f'Zatrudniony {self.hire_date}. ' \
               f'Urodzony {self.birth_date}'
