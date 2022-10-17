class Student:
    def __init__(self, name: str, marks: []):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if (sum(self.marks) / len(self.marks)) > 50:
            return True
        return False


s1 = Student("Jan", [80, 60, 45])
print(s1.is_passed())

s2 = Student("Zosia", [10, 30, 63])
print(s2.is_passed())
