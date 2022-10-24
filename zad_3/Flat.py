from Property import Property


class Flat(Property):
    def __init__(self, floor, area, rooms: int, price: int, address: str):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Mieszkanie {self.address} z {self.rooms} pokojami. ' \
               f'Powierzchnia {self.area}m2. Piętro {self.floor}. ' \
               f'Cena: {self.price}zł'
