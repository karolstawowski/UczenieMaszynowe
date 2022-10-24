class Order:
    def __init__(self, employee, student, books, order_date):
        self.order_date = order_date
        self.books = books
        self.student = student
        self.employee = employee

    def __str__(self):
        return f'Zamówienie studenta {self.student} ' \
               f'zrealizowane {self.order_date} ' \
               f'przez {self.employee} na książki: {self.books}'
