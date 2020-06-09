from ..student import Student


class Register:
    def __init__(self, register_name=None, register=None):
        if register is not None and register_name is None:
            self.__register = register
            tmp = []
            for el in register["students_list"]:
                tmp.append(el["student_id"])
            last_id = max(tmp)
            self.__current_student_id = last_id
        else:
            self.__register = {
                "register_name": register_name,
                "students_list": []
            }
            self.__current_student_id = 0
        self._obs_list = dict()

    def add_observer(self, obs):
        if obs.name not in self._obs_list:
            self._obs_list[obs.name] = obs

    def remove_observer(self, name):
        if name in self._obs_list:
            del self._obs_list[name]

    def add_student_to_register(self, student):
        self.__current_student_id += 1
        self.__register["students_list"].append({
            "student_id": self.__current_student_id,
            "student": student
        })
        for obs in self._obs_list.values():
            obs.update_register(self.__current_student_id)

    def add_student_grade(self, grade, weight, student_id):
        for el in self.__register["students_list"]:
            if el["student_id"] == student_id:
                tmp = el["student"]
        tmp.add_grade(grade, weight)
        for obs in self._obs_list.values():
            obs.update_student(student_id, grade)

    def print_student_grades(self, student_id):
        for el in self.__register["students_list"]:
            if el["student_id"] == student_id:
                tmp = el["student"]
        for obs in self._obs_list.values():
            obs.get_student_grades(tmp.student_name, tmp.student_surname)

        print("Grades for {}:".format(tmp.student_name + " " + tmp.student_surname))
        tmp.print_grades()

    def print_student_grades_average(self, student_id):
        for el in self.__register["students_list"]:
            if el["student_id"] == student_id:
                tmp = el["student"]
        print("Average for {}:".format(tmp.student_name + " " + tmp.student_surname))
        tmp.print_grades_average()

    def print_students(self):
        for el in self.__register["students_list"]:
            print(el["student_id"], end=': ')
            el["student"].print_student_data()


if __name__ == "__main__":
    reg = Register("Test Register")
    std1 = Student("Test", "Testowy")
    reg.add_student_to_register(std1)
    reg.add_student_grade(5, 1, 1)
    std2 = Student("Test2", "Testowy2")
    reg.add_student_to_register(std2)
    reg.print_students()
    print("-----------------------------------------")
    reg.print_student_grades_average(1)
