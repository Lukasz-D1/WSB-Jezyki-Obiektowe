class Grades:
    def __init__(self):
        # note to self: if you set named arguments here with default value of [] it will (for some reason)
        # get shared across all instances of this class, so don't do that unless you want all students with same grades
        self.__grades_list = []
        self.__weights_list = []

    def add_grade_with_weight(self, grade, weight):
        self.__grades_list.append(grade)
        self.__weights_list.append(weight)

    def count_grades_average(self):
        return sum(self.__grades_list)/len(self.__grades_list)

    def print_grades(self):
        for i in range(len(self.__grades_list)):
            print("Ocena: {}, Waga: {}".format(self.__grades_list[i], self.__weights_list[i]))


if __name__ == '__main__':
    grades = Grades()
    grades.add_grade_with_weight(5, 1)
    grades.add_grade_with_weight(1, 5)
    grades.add_grade_with_weight(3, 3)
    print(grades.count_grades_average())
