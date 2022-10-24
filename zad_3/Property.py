class Property:
    def __init__(self, area, rooms: int, price: int, address: str):
        self.address = address
        self.price = price
        self.rooms = rooms
        self.area = area

    def __str__(self):
        return f'Posiadłość {self.address} z {self.rooms} pokojami. ' \
               f'Powierzchnia: {self.area}m2. Cena: {self.price}zł'
