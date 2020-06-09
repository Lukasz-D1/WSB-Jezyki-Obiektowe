from ..grades import Grades


class Student:
    def __init__(self, student_name, student_surname):
        self.__student_name = student_name
        self.__student_surname = student_surname
        self.__grades = Grades()

    def print_student_data(self):
        print("{} {}".format(self.__student_name, self.__student_surname))
        self.print_grades()

    def add_grade(self, grade, weight):
        self.__grades.add_grade_with_weight(grade, weight)

    def print_grades(self):
        self.__grades.print_grades()

    def print_grades_average(self):
        print(self.__grades.count_grades_average())

    @property
    def student_name(self):
        return self.__student_name

    @property
    def student_surname(self):
        return self.__student_surname


if __name__ == "__main__":
    stud = Student("Test", "Testowy")
    stud.add_grade(5, 1)
    stud.add_grade(5, 2)
    stud.add_grade(5, 3)
    stud.print_grades()
