class Property:
    def __init__(self, area: str, rooms: int, price: int, address: str):
        self.address = address
        self.price = price
        self.rooms = rooms
        self.area = area

    def __str__(self):
        return f'Posiadłość {self.address} z {self.rooms} pokojami. Powierzchnia: {self.area}m2. Cena: {self.price}zł'


class House(Property):
    def __init__(self, plot, area: str, rooms: int, price: int, address: str):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'Dom {self.address} z {self.rooms} pokojami. Powierzchnia domu: {self.area}m2, powierzchnia działki: {self.plot}m2. Cena: {self.price}zł'


class Flat(Property):
    def __init__(self, floor, area: str, rooms: int, price: int, address: str):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Mieszkanie {self.address} z {self.rooms} pokojami. Powierzchnia {self.area}m2, piętro {self.floor}. Cena: {self.price}zł'


h1 = House(300, 140, 4, 2500000, "Katowice")
print(h1)

f1 = Flat(2, 40, 1, 300000, "Gliwice")
print(f1)
