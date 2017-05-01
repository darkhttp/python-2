import mysql.connector
from mysql.connector import MySQLConnection, Error

class University:
    # конструктор, при создании объекта класса осуществляет подключение к экземпляру БД
    def __init__(self, host, database, user, password):
        # запоминаем параметры подключения, в первом варианте примера этого нету (ДОБАВИТЬ)
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='university_anisov_dmitriy',
                                           user='root',
                                           password='123456')
            if conn.is_connected():
                print('Connected to MySQL database')
        except Error as e:
            print(e)

    def stop_con(self):
        conn = mysql.connector.connect(host=self.host,
                                       database=self.database,
                                       user=self.user,
                                       password=self.password)
        conn.close()

    def printerGroups(self):
        try:
            sql = "SELECT B.idGroup,B.number_of_group,U.kyrs from University U, groups B where U.kyrs = B.kyrs;"
            conn = mysql.connector.connect(host=self.host,
                                       database=self.database,
                                       user=self.user,
                                       password=self.password)
            c = conn.cursor()
            c.execute(sql)
            print("Список Групп по курсам")
            rows = c.fetchall()
            return rows
        except Error as e:
            return e

    def printerStudent(self):
        try:
            sql = "SELECT S.idStudent,P.first_name, P.last_name,S.group,S._starosta, U.kyrs,G.number_of_group from University U,student S, People P,Groups G where U.kyrs = G.kyrs and G.idGroup = S.group and S.idStudent=P.idPeople;"
            conn = mysql.connector.connect(host=self.host,
                                       database=self.database,
                                       user=self.user,
                                       password=self.password)
            c = conn.cursor()
            c.execute(sql)
            print("Список всех студентов")
            rows = c.fetchall()
            return rows
        except Error as e:
            return(e)

    def add_kyrs(self,kyrs,student):
        try:
            sql = "INSERT INTO University(kyrs, student)"\
                    " VALUES(%s,%s)"
            args=(kyrs,student)
            conn = mysql.connector.connect(host=self.host,
                                       database=self.database,
                                       user=self.user,
                                       password=self.password)
            c = conn.cursor()
            c.execute(sql,args)
            conn.commit()
            return ('Курс {} добавлен'.format(kyrs))
        except Error as e:
            return (e)

    def delete_kyrs(self,kyrs):
        try:
            sql = "DELETE FROM University WHERE kyrs = %s"
            conn = mysql.connector.connect(host=self.host,
                                       database=self.database,
                                       user=self.user,
                                       password=self.password)
            c = conn.cursor()
            c.execute(sql, (kyrs,))
            conn.commit()
            return ('Курс {} удалён'.format(kyrs))
        except Error as e:
            return (e)


class Group(University):

    def student_of_group(self,number_of_group):
        try:
            sql = "SELECT S.idStudent,P.first_name, P.last_name,G.number_of_group,S._starosta, G.kyrs from Groups G, student S, People P where G.idGroup = S.group and S.group = %s and S.idStudent=P.idPeople;"
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)

            c = conn.cursor()
            c.execute(sql,(number_of_group,))
            print("Все студенты этой группы")
            rows = c.fetchall()
            return rows
        except Error as e:
            return (e)

    def add_group(self, number_of_group,s_code, kyrs):
        try:
            sql = "INSERT INTO Groups (number_of_group, s_code, kyrs)" \
                  " VALUES(%s,%s,%s)"
            args = ( number_of_group,s_code,kyrs)
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)
            c = conn.cursor()
            c.execute(sql, args)
            conn.commit()
            return ('Группа {} добавлена'.format(number_of_group))
        except Error as e:
            return(e)

    def delete_group(self, number_of_group):
        try:
            sql = "DELETE FROM Groups WHERE number_of_group = %s"
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)
            c = conn.cursor()
            c.execute(sql, (number_of_group,))
            conn.commit()
            return ('Группа {} удалена'.format(number_of_group))
        except Error as e:
            return (e)

#скрытый класс и скрытые методы от пользователя
class People:

    def __init__(self, host, database, user, password):
        # запоминаем параметры подключения, в первом варианте примера этого нету (ДОБАВИТЬ)
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def get_people(self, idPeople):
        try:
            sql = "SELECT P.idPeople, P.first_name, P.second_name, P.last_name, P.d_of_b, P.telephone FROM People P where P.idPeople = %s;"
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)
            c = conn.cursor()
            c.execute(sql, (idPeople,))
            print("Данные о человеке чьё id {}".format(idPeople))
            rows = c.fetchall()
            for row in rows:
                self.id,self.name,self.second_name,self.third_name,self.d_of_b,self.telephone = row
            return rows
        except Error as e:
            return (e)

    def add_people(self,first_name, second_name, last_name, d_of_bd,telephone):
        try:
            sql = "INSERT INTO `people` (`first_name`, `second_name`, `last_name`, `d_of_b`, `telephone`) " \
                  "VALUES (%s, %s, %s, %s, %s);"

            args = (first_name, second_name, last_name, d_of_bd, telephone)
            conn = mysql.connector.connect(host=self.host,
                                       database=self.database,
                                       user=self.user,
                                       password=self.password)
            c = conn.cursor()
            c.execute(sql, args)
            conn.commit()
            return ('{} {} {} добавлен '.format(first_name,second_name,last_name))
        except Error as e:
            return (e)

    def get_full_name(self): #получение полного имени из бд на основе граф

        return 'Полное имя '+self.second_name+' ' + self.name + ' ' + self.third_name




class Student(People):

    def add_student(self,first_name, second_name, last_name, d_of_bd,telephone,group,starosta):
        try:
            sql = "INSERT INTO `people` (`first_name`, `second_name`, `last_name`, `d_of_b`, `telephone`) VALUES ( %s, %s, %s, %s, %s);" \
                  "INSERT INTO `student` (`group`, `_starosta`)" \
                  " VALUES ( %s, %s)"
            #sql =  "INSERT INTO `student` (`group`, `_starosta`, `kyrs`) VALUES ( %s, %s, %s);" \
             #      "INSERT INTO `people` (`first_name`, `second_name`, `last_name`, `d_of_b`, `telephone`) VALUES ( %s, %s, %s, %s, %s);"

            args = (first_name, second_name, last_name, d_of_bd, telephone,group,starosta,)
            conn = mysql.connector.connect(host=self.host,
                                       database=self.database,
                                       user=self.user,
                                       password=self.password)
            c = conn.cursor()
            for result in c.execute(sql, args,multi=True):
                conn.commit()
                return ('Студент {} {} {} добавлен '.format(first_name, second_name, last_name))
        except Error as e:
            return (e)

    def delete_student(self, first_name, second_name, last_name):
        try:
            sql = "DELETE FROM People  WHERE first_name = %s and second_name = %s and last_name=%s"
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)
            c = conn.cursor()
            c.execute(sql, (first_name, second_name, last_name,))
            conn.commit()
            return ("Cтудент {} {} {} удалён".format(first_name, second_name, last_name))
        except Error as e:
            return (e)

    def get_student_second_name(self, second_name):
        try:
            sql = "SELECT P.idPeople, P.first_name, P.second_name, P.last_name, P.d_of_b, P.telephone,S.group,S._starosta FROM People P, Student S where P.idPeople=S.idStudent and P.second_name = %s"
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)
            c = conn.cursor()
            c.execute(sql, (second_name,))
            print("Данные о студенте  {}".format(second_name))
            rows = c.fetchall()
            for row in rows:
                self.id, self.name, self.second_name, self.third_name, self.d_of_b, self.telephone, self.group, self._starosta = row
            return rows
        except Error as e:
            print(e)

    def update_student(self, first_name, second_name, last_name, telephone,
                       group):  # изменение имени, фамилии и отчества в бд
        try:
            sql = "SET SQL_SAFE_UPDATES = 0;" \
                  "UPDATE People P,Student S SET P.first_name = %s,P.second_name = %s,P.last_name = %s,P.telephone = %s,S.group = %s" \
                  " WHERE P.idPeople=S.idStudent and P.second_name= %s"
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)

            c = conn.cursor()
            args = (first_name, second_name, last_name, telephone, group, second_name)

            for result in c.execute(sql, args, multi=True):
                conn.commit()
        except Error as e:
            return e

    @property
    def starosta(self):
        if self._starosta == '+':
            return 'Этот студент является старостой'
        elif self._starosta == '-':
            return 'Этот студент не является старостой'
        else:
            raise ValueError("Ошибка ввода,должнен быть + или -")

    @property
    def starosta(self):
        if self._starosta == '+':
            return 'Этот студент является старостой'
        elif self._starosta == '-':
            return 'Этот студент не является старостой'
        else:
            raise ValueError("Ошибка ввода,должнен быть + или -")

if __name__ == '__main__':

    univer = University('localhost','university_anisov_dmitriy','root','123456')
    group = Group('localhost','university_anisov_dmitriy','root','123456')
    people= People('localhost','university_anisov_dmitriy','root','123456')
    student= Student('localhost','university_anisov_dmitriy','root','123456')
    print('-'*100)
    #Cписок групп в университете с курсом
    univer.printerGroups()
    print('-'*100)
    #Все студенты университета
    univer.printerStudent()
    print('-'*100)

    #Все студенты определённой группы
    group.student_of_group(34000)
    print('-'*100)

    #Конкретный человек по id
    people.get_people(1)
    print(people.get_full_name())
    people.get_people(2)
    print(people.get_full_name())
    print('-'*100)

    #Добавление конкретного студента в бд
    student.add_student('Лера','Акаева','Cергеевна', '28/04/1995' ,'891111','35000','-','3',)
    #student.add_student('Аня','Агаева','Cергеевна', '28/04/1995' ,'891111','34000','-','3')
    print('-'*100)

    #Добавление группы в бд
    group.add_group('31000','12345','3')
    print('-'*100)

    #удаление группы из бд
    group.delete_group(31000)
    print('-'*100)

    #Добавление курса в университет
    univer.add_kyrs(2,2)
    print('-'*100)

    #Удаление курса из университета
    univer.delete_kyrs(2)
    print('-'*100)

    #Удаление студента(то есть класс человека)
    student.delete_student('Лера','Акаева','Cергеевна')
    print('-'*100)

    #Получение конкретного студента по фамилии и указание является ли он старостой
    student.get_student_second_name('Анисов')
    print(student.starosta)
    print('-'*100)

    #Обновление конкретного студента
    student.update_student('Дмитрий','Анисов', 'Александрович','89210010','34000')