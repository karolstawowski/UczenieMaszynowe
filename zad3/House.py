from zad3.Property import Property


class House(Property):
    def __init__(self, plot, area, rooms: int, price: int, address: str):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'Dom {self.address} z {self.rooms} pokojami. ' \
               f'Powierzchnia domu: {self.area}m2. ' \
               f'Powierzchnia działki: {self.plot}m2. ' \
               f'Cena: {self.price}zł'
