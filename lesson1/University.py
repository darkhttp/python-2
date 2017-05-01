class University:
    def __init__(self):
        self.student = []
    def add_all_student(self,student):
        self.student = []
        return self.student


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
    def __init__(self,number_of_group):
        self.number_of_group = number_of_group

    @property
    def number_of_group(self):
        return self.__number_of_group

    @number_of_group.setter
    def number_of_group(self,next_group):
        self.__number_of_group = next_group


class Student(People,University):
    def __init__(self,second_name,first_name,last_name,d_of_b,telephone,id,number_of_group,starosta,code):
        super().__init__(second_name,first_name,last_name,d_of_b,telephone)
        Group.__init__(self,number_of_group)
        self.id = id
        self.__starosta = starosta
        self.code = code
    @property
    def starosta(self):
        if self.__starosta == '+' or self.__starosta == '-':
            return self.__starosta
        else:
            raise ValueError("Ошибка ввода,должнен быть + или -")
    def add_student(self):
        self.student.append()



a = Student('Анисов','Дмитрий','Александрович','24/03/1996','89041111111','1','000000','-','24859302')

print(c.student)
