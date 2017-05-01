class University:
    def __init__(self):
        #first_par,second_par,third_par,fourth_par,add_student)

        #self.first_par = first_par
        #self.second_par = second_par
        #self.third_par = third_par
        #self.fourth_par = fourth_par
        self._student = []
        self.groups = []

    def get_all_students(self):
        return self._student

    def get_all_groups(self):
        return self.groups

    def get_group(self, number_of_group):
        for group in self.groups:
            if group.number_of_group == number_of_group:
                return group


    def add_all_student(self,new_student):
        self._student.append(new_student)
        return self._student


class People:
    def __init__(self,second_name,first_name,last_name,d_of_b,telephone):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.d_of_b = d_of_b
        self.telephone = telephone

    def get_full_name(self):
        return self.second_name + self.first_name + self.last_name

    def set_new_name(self,second_name,first_name,last_name):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name


class Group:
    def __init__(self,number_of_group,s_code):
        self.number_of_group = number_of_group
        self._students = []
        self.s_code = s_code

    @property
    def number_of_group(self):
        return self.__number_of_group

    @number_of_group.setter
    def number_of_group(self,next_group):
        self.__number_of_group = next_group

    def get_all_students_group(self):
        return self._students

    def add_student(self, new_student):
        self._students.append(new_student)
        new_student.group = self


class Student(People,University):
    def __init__(self,second_name,first_name,last_name,d_of_b,telephone,id,starosta,group = None ):
        super().__init__(second_name,first_name,last_name,d_of_b,telephone)
        self.id = id
        self.__starosta = starosta
        self.group = group

    @property
    def starosta(self):
        if self.__starosta == '+':
            return 'Этот студент является старостой'
        elif self.__starosta == '-':
            return 'Этот студент не является старостой'
        else:
            raise ValueError("Ошибка ввода,должнен быть + или -")

univer = University()

g1 = Group('34675','1')
g2 = Group('12312','2')
g3 = Group('123132','3')

univer.groups.append(g1)
univer.groups.append(g2)
univer.groups.append(g3)

s1 = Student('Анисов','Дмитрий','Александрович','24/03/1996','89041111111','1','+')
s2 = Student('Фамилия1','Дмитрий','Александрович','24/03/1996','89041111111','1','+')
s3 = Student('Фамилия2','Дмитрий','Александрович','24/03/1996','89041111111','1','+')
s4 = Student('Фамилия3','Дмитрий','Александрович','24/03/1996','89041111111','1','+')
s5 = Student('Фамилия4','Дмитрий','Александрович','24/03/1996','89041111111','1','+')
s6 = Student('Фамилия5','Дмитрий','Александрович','24/03/1996','89041111111','1','+')

univer.add_all_student(s1)
univer.add_all_student(s2)
univer.add_all_student(s3)
univer.add_all_student(s4)
univer.add_all_student(s5)
univer.add_all_student(s6)


g1.add_student(s1)
g1.add_student(s2)
g2.add_student(s3)
g2.add_student(s4)
g3.add_student(s5)
g3.add_student(s6)

#получаем список всех групп в универе
for g in univer.get_all_groups():
    print(g.number_of_group)
#Получаем всех студентов определённой группы
gr1  = univer.get_group('34675')
for student in gr1.get_all_students_group():
    print(student.second_name)
#Получаем группу конкретного студента
print(s1.group.number_of_group)
#Проверка является ли студент старостой
print(s1.starosta)
#Получаем всех студентов университета -- не знаю как
for student in univer.get_all_students():
    print(student.second_name)