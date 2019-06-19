class Patients:
    def __init__(self, patients=0):
        self.patients = patients


class Hospital(Patients):

    def get_patients(self):
        return self.__patients

    def set_patients(self, number):
        if number <= 1000:
            self.__patients = number
        else:
            self.__patients = 1000

    patients = property(get_patients, set_patients)


h = Hospital(1500)
print("\n Кількість паціентів в лікарні", h.patients)


class Chamber(Patients):
    def get_patients(self):
        return self.__patients

    def set_patients(self, number):
        if number <= 4:
            self.__patients = number
        else:
            self.__patients = 4

    patients = property(get_patients, set_patients)


c = Chamber(5)
print("\n", "Кількість паціентів в палаті", c.patients)


