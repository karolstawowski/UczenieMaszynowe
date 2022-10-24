class Student:
    def __init__(self, name: str, marks: []):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if (sum(self.marks) / len(self.marks)) > 50:
            return True
        return False
