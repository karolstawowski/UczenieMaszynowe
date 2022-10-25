from zad2.Book import Book
from zad2.Employee import Employee
from zad2.Library import Library
from zad2.Order import Order

l1 = Library("Katowice", "Chorzowska", "40-012", "10-18", "123456789")
l2 = Library("Katowice", "Mikołowska", "40-014", "8-18", "123456798")

b1 = Book(l1, "17/04/2001", "Jan", "Nowak", 310)
b2 = Book(l2, "12/07/2011", "Andrzej", "Adamski", 310)
b3 = Book(l1, "22/01/2022", "Halina", "Klementynowicz", 310)
b4 = Book(l1, "16/12/2008", "Jan", "Szpak", 310)
b5 = Book(l2, "02/03/1993", "Józef", "Mnich", 310)

e1 = Employee("Eugeniusz", "Smolarek", "20/08/2009", "10/02/1968",
              "Wadowice", "Biskupińska", "22-012", "654234765")
e2 = Employee("Stanisław", "Lato", "20/08/2009", "12/03/1985",
              "Kraków", "Biskupińska", "22-012", "686534765")
e3 = Employee("Stanisława", "Zima", "20/08/2009", "24/11/1998",
              "Dąbrowa Górnicza", "Wolności", "22-012", "654234235")

o1 = Order(e1, "Radosław Żółk", [b1, b2], "01/02/2010")
print(o1)
o2 = Order(e3, "Przemysław Gęś", [b3, b2], "04/03/2011")
print(o2)
