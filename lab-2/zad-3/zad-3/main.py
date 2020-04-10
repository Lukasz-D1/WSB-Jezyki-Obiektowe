from register import Register
from student import Student


def main():
    dz = Register(register_name="Dziennik 1")
    dz.add_student_to_register(Student("Jan", "Kowalski"))
    dz.add_student_grade(5, 1, 1)
    dz.print_student_grades_average(1)

    dziennik_template = {
        "register_name": "Dziennik 2",
        "students_list": [
            {
                "student_id": 1,
                "student": Student("Adam", "Nowak")
            }
        ]
    }
    dz2 = Register(register=dziennik_template)
    print('-------------------------------------------------')
    dz.print_students()
    print('-------------------------------------------------')
    dz2.add_student_grade(3, 2, 1)
    dz2.add_student_grade(4, 1, 1)

    dz2.print_student_grades(1)


if __name__ == '__main__':
    main()
