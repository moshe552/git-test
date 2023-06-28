from person import Person


class Student(Person):

    id_auto_increment = 1

    def __init__(self, name, phone, email):
        super().__init__(name, phone, email)
        self.__id = Student.id_auto_increment
        Student.id_auto_increment += 1

