from .abstract_view import AbstractView


class ConsoleRegisterView(AbstractView):
    def __init__(self, name, model):
        super().__init__(name, model)

    def add_component(self, comp):
        pass

    def update_register(self, *args, **kwargs):
        print('Added new student to reigster - ID: {0}'.format(args[0]))

    def update_student(self, *args, **kwargs):
        print("Added new grade for student: ID - {}, grade - {}".format(args[0], args[1]))

    def get_student_grades(self, *args, **kwargs):


    def show(self):
        self.model.notify()
