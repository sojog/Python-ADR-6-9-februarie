from pprint import pprint, pp


class Profesor:
    pass


class Student:
    """
    Docstring (documentatia) for Student
    """
    def __init__(self):
        pass

    def __str__(self):
        pass

    def functie(self, parametru):
        pass


obiect = Student()
pprint(Student.__dict__)
pp(Student.__dict__)

print(Student.__doc__)

help(Student)

