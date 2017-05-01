from  University_bd import  *
import tkinter
from tkinter import *

univer = University('localhost', 'university_anisov_dmitriy', 'root', '123456')
group = Group('localhost', 'university_anisov_dmitriy', 'root', '123456')
people = People('localhost', 'university_anisov_dmitriy', 'root', '123456')
student = Student('localhost', 'university_anisov_dmitriy', 'root', '123456')

class Output():
    def __init__(self):
        roota.withdraw()
        self.root = Tk()
        self.root.title("Информационная система Университет")
        self.root.minsize(380, 300)
        self.root.resizable(width=False, height=False)

        self.bottom_frame_1 = Frame(self.root, bg='lightgreen', bd=8)
        self.bottom_frame_2 = Frame(self.root, bg='lightgreen', bd=8)
        self.bottom_frame_3 = Frame(self.root, bg='lightgreen', bd=8)
        self.bottom_frame_4  = Frame(self.root, bg='lightgreen', bd=8)

        self.top_frame = Frame(self.root)

        # Расстановка фреймов
        self.bottom_frame_1.pack(side=BOTTOM, fill='x')
        self.bottom_frame_2.pack(side=BOTTOM, fill='x')
        self.bottom_frame_3.pack(side=BOTTOM, fill='x')
        self.bottom_frame_4.pack(side=BOTTOM, fill='x')
        self.top_frame.pack(side=TOP)
        # Статус-бар
        self.statusbar = Label(self.top_frame, relief=SUNKEN, border=1, anchor=W)

        self.output = Text(self.top_frame, bg='white', font='Century', width=100, height=10, wrap=WORD)
        self.scrollbar = Scrollbar(self.top_frame, command=self.output.yview)
        self.output.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)  # Прилепить к правому краю фрейма и заполнить по высоте (ось y)
        self.output.pack(fill=BOTH)
        self.statusbar.pack(side=BOTTOM, fill=X)


class User(Output):
    # метод для просмотра всех групп в универе
    def butt(self):
        texts = univer.printerGroups()
        for t in texts:
            t = '{!s:<5}{!s:<20}{!s:<20}'.format(t[0], t[1], t[2])
            self.output.insert("1.0", str(t) + "\n")

    # метод для просмотра всех студентов в университете
    def butt1(self):
        texts = univer.printerStudent()
        for t in texts:

            t = '{!s:<5}{!s:<20}{!s:<20}{!s:<20}{!s:<12}{!s:<12}{!s:<12}'.format(t[0], t[1], t[2], t[3], t[4],t[5],t[6])
            self.output.insert("1.0", str(t) + "\n")

    def butt5(self):
        #окно для вывода всех студентов конкретной группы
        root2 = Tk()
        root2.minsize(350, 50)
        root2.title("студенты конкретной группы")
        # поле для ввода группы
        a = Entry(root2, width=17)
        a.grid(row=1, column=0, padx=(10, 10))
        l = Label(root2,text = "Номер группы")
        l.grid(row=1, column=1, padx=(10, 0))

        # метод для поиска группы
        def button5():
            self.output.edit_reset()
            if a.get().isdigit() == True:
                t = group.student_of_group(a.get())
                for t in t:
                    t = '{!s:<5}{!s:<20}{!s:<20}{!s:<20}{!s:<12}{!s:<12}'.format(t[0], t[1], t[2], t[3], t[4], t[5])
                    self.output.insert("0.0", str(t) + "\n")
            else:
                self.output.insert('0.0', str('Некорректный ввод!'+'\n'))
        #кнопка для посика студентов
        butt = tkinter.Button(root2, text = "Найти", bg="white", fg="black", width=15,height=1,command=button5)
        butt.grid(row=4, column=0,padx=(10, 0))
        root2.mainloop()

    def butt10(self):
        root2 = Tk()
        root2.title('Студент по Фамилии')
        root2.minsize(350,50)
        a = Entry(root2,width = 30)
        a.grid(row = 1,column = 2,padx = (10,10))
        l = Label(root2,text = 'Фамилия')
        l.grid(row =1,column = 0,padx=(10, 0))

        def button10():
            self.output.edit_reset()
            if a.get().isalpha() == True:

                t = student.get_student_second_name(a.get().title())
                for t in t:
                    t = '{!s:<5}{!s:<20}{!s:<20}{!s:<20}{!s:<12}{!s:<10}{!s:<10}{!s:<10}'.format(t[0], t[1], t[2], t[3],                                                                                                 t[4], t[5], t[6], t[7])
                    self.output.insert('0.0',str(t) +'\n')
            else:
                self.output.insert('0.0', str('Некорректный ввод!'+'\n'))
        butt = tkinter.Button(root2,text = 'Подробне о студенте', bg = 'white',fg = 'black',width = 30,height = 1,command = button10)
        butt.grid(row = 2, column=2, padx=(10,0))


class Admin(User):
    # метод создания нового курса в университете
    def butt3(self):
        # окно для добавления нового курса
        root1 = Tk()
        root1.title("Добавление нового курса")
        root1.minsize(270, 100)
        # поля для ввода данных о курсе
        a = Entry(root1, width=30)
        a.grid(row=1, column=2, padx=(10, 0))
        l = Label(root1, text="Новый курс")
        l.grid(row=1, column=0, padx=(10, 0))
        a1 = Entry(root1, width=30)
        a1.grid(row=2, column=2, padx=(10, 0))
        l1 = Label(root1, text="Индификатор курса для студента")
        l1.grid(row=2, column=0, padx=(10, 0))

        # метод для добавления нового курса
        def button1():
            if (a.get().isdigit() & a1.get().isdigit()) == True:
                t = univer.add_kyrs(a.get(), a1.get())
                self.output.insert("0.0", str(t) + "\n")
            else:
                self.output.insert('0.0', str('Некорректный ввод!'+'\n'))
        # кнопка для добавления нового курса
        butt = tkinter.Button(root1, text="Добавить", bg="white", fg="black", width=15, height=1, command=button1)
        butt.grid(row=4, column=0, padx=(10, 10))
        root1.mainloop()

    # метод создания диалогового окна для удаления курса
    def butt4(self):
        # окно для удаления курса
        root2 = Tk()
        root2.title("Удаление курса")
        root2.minsize(250, 50)
        # поле для ввода идентификатора удаляемого курса
        a = Entry(root2, width=30)
        a.grid(row=1, column=0, padx=(10, 10))
        l = Label(root2, text="Номер курса")
        l.grid(row=1, column=1, padx=(10, 0))

        # метод для удаление курса
        def button2():
            self.output.edit_reset()
            if a.get().isdigit() == True:
                t = univer.delete_kyrs(a.get())
                self.output.insert("0.0", str(t) + "\n")
            else:
                self.output.insert('0.0', str('Некорректный ввод!'+'\n'))
        # кнопка для удаления курса
        butt = tkinter.Button(root2, text="Удалить", bg="white", fg="black", width=15, height=1, command=button2)
        butt.grid(row=4, column=0, padx=(10, 0))
        root2.mainloop()

    def butt6(self):
        # окно для добавления новой группы
        root1 = Tk()
        root1.title("Добавление новой группы")
        root1.minsize(300, 100)
        # поля для ввода данных о курсе
        a = Entry(root1, width=30)
        a.grid(row=1, column=2, padx=(10, 0))
        l = Label(root1, text="Номер группы")
        l.grid(row=1, column=0, padx=(10, 0))
        a1 = Entry(root1, width=30)
        a1.grid(row=2, column=2, padx=(10, 0))
        l1 = Label(root1, text="код факультета")
        l1.grid(row=2, column=0, padx=(10, 0))
        a2 = Entry(root1, width=30)
        a2.grid(row=3, column=2, padx=(10, 0))
        l2 = Label(root1, text="Курс")
        l2.grid(row=3, column=0, padx=(10, 0))

        # метод для добавления новой группы
        def button6():
            if (a.get().isdigit() & a1.get().isdigit()& a2.get().isdigit()) == True:
                t = group.add_group(a.get(), a1.get(), a2.get())
                self.output.insert("0.0", str(t) + "\n")
            else:
                self.output.insert('0.0', str('Некорректный ввод!'+'\n'))
        # кнопка для добавления нового курса
        butt = tkinter.Button(root1, text="Добавить", bg="white", fg="black", width=15, height=1, command=button6)
        butt.grid(row=4, column=0, padx=(10, 10))
        root1.mainloop()

    # окно для удаления курса
    def butt7(self):
        root2 = Tk()
        root2.title("Удаление группы")
        root2.minsize(250, 50)
        # поле для ввода номеру удаляемой группы
        a = Entry(root2, width=30)
        a.grid(row=1, column=0, padx=(10, 10))
        l = Label(root2, text="Номер группы")
        l.grid(row=1, column=1, padx=(10, 0))

        # метод для удаление группы
        def button2():
            self.output.edit_reset()
            if a.get().isdigit()  == True:
                t = group.delete_group(a.get())
                self.output.insert("0.0", str(t) + "\n")
            else:
                self.output.insert('0.0', str('Некорректный ввод!'+'\n'))

        # кнопка для удаления группы
        butt = tkinter.Button(root2, text="Удалить", bg="white", fg="black", width=15, height=1, command=button2)
        butt.grid(row=4, column=0, padx=(10, 0))
        root2.mainloop()

    def butt8(self):
        root2 = Tk()
        root2.title("Добавление студента")
        root2.minsize(350, 100)
        a = Entry(root2, width=30)
        a.grid(row=1, column=2, padx=(10, 10))
        l = Label(root2, text='Имя')
        l.grid(row=1, column=0, padx=(10, 0))
        a1 = Entry(root2, width=30)
        a1.grid(row=2, column=2, padx=(10, 10))
        l1 = Label(root2, text='Фамилия')
        l1.grid(row=2, column=0, padx=(10, 0))
        a2 = Entry(root2, width=30)
        a2.grid(row=3, column=2, padx=(10, 10))
        l2 = Label(root2, text='Отчество')
        l2.grid(row=3, column=0, padx=(10, 0))
        a3 = Entry(root2, width=30)
        a3.grid(row=4, column=2, padx=(10, 10))
        l3 = Label(root2, text='День рождения через /')
        l3.grid(row=4, column=0, padx=(10, 0))
        a4 = Entry(root2, width=30)
        a4.grid(row=5, column=2, padx=(10, 10))
        l4 = Label(root2, text='Телефон')
        l4.grid(row=5, column=0, padx=(10, 0))
        a5 = Entry(root2, width=30)
        a5.grid(row=6, column=2, padx=(10, 10))
        l5 = Label(root2, text='id Группы')
        l5.grid(row=6, column=0, padx=(10, 0))
        a6 = Entry(root2, width=30)
        a6.grid(row=7, column=2, padx=(10, 10))
        l6 = Label(root2, text='Староста')
        l6.grid(row=7, column=0, padx=(10, 0))

        def button8():
            self.output.edit_reset()
            if (a.get().isalpha() & a1.get().isalpha() & a2.get().isalpha() & a5.get().isdigit()) \
                    and re.match(r'[8-9]{1}[0-9]{9}',a4.get()) and re.match(r'^[+,-]$',a6.get()) \
                    and re.match(r'^[0-9]{2}/[0-9]{2}/[0-9]{4}$',a3.get()):
                t = student.add_student(a.get().title(), a1.get().title(), a2.get().title(), a3.get(), a4.get(), a5.get(), a6.get())
                self.output.insert('0.0', str(t) + '\n')
            else:
                self.output.insert('0.0', str('Некорректный ввод!'+'\n'))

        butt = tkinter.Button(root2, text='Добавить', bg='white', fg='black', width=15, height=1, command=button8)
        butt.grid(row=8, column=2, padx=(10, 0))
        root2.mainloop()

    def butt9(self):
        root2 = Tk()
        root2.title('Удаление студента')
        root2.minsize(350, 50)
        a = Entry(root2, width=30)
        a.grid(row=1, column=2, padx=(10, 10))
        l = Label(root2, text='Имя')
        l.grid(row=1, column=0, padx=(10, 0))
        a2 = Entry(root2, width=30)
        a2.grid(row=2, column=2, padx=(10, 10))
        l2 = Label(root2, text='Фамилия')
        l2.grid(row=2, column=0, padx=(10, 0))
        a3 = Entry(root2, width=30)
        a3.grid(row=3, column=2, padx=(10, 10))
        l3 = Label(root2, text='Отчество')
        l3.grid(row=3, column=0, padx=(10, 0))

        def button9():
            self.output.edit_reset()
            if (a.get().isalpha() & a2.get().isalpha() & a3.get().isalpha()):
                t = student.delete_student(a.get().title(), a2.get().title(), a3.get().title())
                self.output.insert('0.0', str(t) + '\n')
            else:
                self.output.insert('0.0', str('Некорректный ввод!'+'\n'))
        butt = tkinter.Button(root2, text='Удалить', bg='white', fg='black', width=15, height=1, command=button9)
        butt.grid(row=4, column=2, padx=(10, 0))

    def butt11(self):
        root2 = Tk()
        root2.title('Изменение студента по id')
        root2.minsize(350, 50)
        a0 = Entry(root2, width=30)
        a0.grid(row=0, column=2, padx=(10, 10))
        l0 = Label(root2, text='id Изменяемого студента')
        l0.grid(row=0, column=0, padx=(10, 0))
        a = Entry(root2, width=30)
        a.grid(row=1, column=2, padx=(10, 10))
        l = Label(root2, text='Имя')
        l.grid(row=1, column=0, padx=(10, 0))
        a1 = Entry(root2, width=30)
        a1.grid(row=2, column=2, padx=(10, 10))
        l1 = Label(root2, text='Фамилия')
        l1.grid(row=2, column=0, padx=(10, 0))
        a2 = Entry(root2, width=30)
        a2.grid(row=3, column=2, padx=(10, 10))
        l2 = Label(root2, text='Отчество')
        l2.grid(row=3, column=0, padx=(10, 0))
        a3 = Entry(root2, width=30)
        a3.grid(row=4, column=2, padx=(10, 10))
        l3 = Label(root2, text='День рождения через /')
        l3.grid(row=4, column=0, padx=(10, 0))
        a4 = Entry(root2, width=30)
        a4.grid(row=5, column=2, padx=(10, 10))
        l4 = Label(root2, text='Телефон')
        l4.grid(row=5, column=0, padx=(10, 0))
        a5 = Entry(root2, width=30)
        a5.grid(row=6, column=2, padx=(10, 10))
        l5 = Label(root2, text='id Группы')
        l5.grid(row=6, column=0, padx=(10, 0))
        a6 = Entry(root2, width=30)
        a6.grid(row=7, column=2, padx=(10, 10))
        l6 = Label(root2, text='Староста')
        l6.grid(row=7, column=0, padx=(10, 0))

        def button11():
            self.output.edit_reset()
            if (a0.get().isdigit() % a.get().isalpha() & a1.get().isalpha() & a2.get().isalpha() & a5.get().isdigit()) \
                    and re.match(r'[8-9]{1}[0-9]{9}',a4.get()) and re.match(r'^[+,-]$',a6.get()) \
                    and re.match(r'^[0-9]{2}/[0-9]{2}/[0-9]{4}$',a3.get()):
                t = student.update_student(a0.get(),a.get().title(), a1.get().title(), a2.get().title(), a3.get(), a4.get(), a5.get(),
                                           a6.get())
                self.output.insert('0.0', str(t) + '\n')
            else:
                self.output.insert('0.0', str('Некорректный ввод!'+'\n'))
        butt = tkinter.Button(root2, text='Изменение студента по id', bg='white', fg='black', width=30, height=1,
                              command=button11)
        butt.grid(row=8, column=2, padx=(10, 0))

        # метод создания диалогового окна для добавления пользователя
    def butt12(self):
        # окно для добавления нового Пользователя
        rootU = Tk()
        rootU.title("Добавление нового пользователя")
        rootU.minsize(270, 100)
        # поля для ввода данных о новом авторе

        a = Entry(rootU, width=15)
        a.grid(row=2, column=2, padx=(10, 0))
        l1 = Label(rootU, text="Роль")
        l1.grid(row=2, column=0, padx=(10, 0))
        a2 = Entry(rootU, width=15)
        a2.grid(row=3, column=2, padx=(10, 0))
        l2 = Label(rootU, text="Логин")
        l2.grid(row=3, column=0, padx=(10, 0))
        a3 = Entry(rootU, width=15)
        a3.grid(row=4, column=2, padx=(10, 0))
        l3 = Label(rootU, text="Пароль")
        l3.grid(row=4, column=0, padx=(10, 0))

        # метод для ограничения ввода логина
        def correct(event):
            data = a2.get()
            if len(data) > 3:
                if not data.isalpha():
                    self.output.insert("0.0", "Выводите не корректный логин!")
                    a2["bg"] = "red"
                else:
                    self.output.insert("0.0", "Логин введен в соответствии с правилами.")
                    a2["bg"] = "green"

        a2.bind("<Any-KeyRelease>", correct)

        # метод для добавления пароля
        def buttonAdd():
            result = re.findall(r'^[A-Z]{1}\w+[a-z]{1}$', a3.get())
            print(result)
            if (result != []):
                t = univer.add_user(a2.get(), a3.get(),a.get())
                self.output.insert("0.0", str(t) + "\n")
            else:
                self.output.insert("0.0", "Некорректный пароль!")

        # кнопка для добавления нового автора
        butt = tkinter.Button(rootU, text="Добавить", bg="white", fg="black", width=15, height=1, command=buttonAdd)
        butt.grid(row=5, column=0, padx=(10, 10))
        rootU.mainloop()


class Men(Admin):
    def __init__(self):
        super().__init__()
        a = Menu(self.root)
        self.menubar = a
        #Меню просмотр для юзера и админа
        self.promenu = Menu(self.menubar, tearoff=0)
        self.promenu.add_command(label="Посмотреть все группы", command=self.butt)
        self.promenu.add_command(label="Посмотреть всех студентов", command=self.butt1)
        self.promenu.add_command(label="Список студентов группы", command=self.butt5)
        self.promenu.add_command(label="Студент по фамилии", command=self.butt10)
        self.promenu.add_separator()
        self.promenu.add_command(label="Выход", command=self.root.destroy)
        self.menubar.add_cascade(label="Просмотр", menu=self.promenu)
        #Отоборожение меню
        self.root.config(menu=self.menubar)

class MenuAdmin(Men):
    def __init__(self):
        super().__init__()
        #меню удаления для админа
        self.deletemenu = Menu(self.menubar, tearoff=0)
        self.deletemenu.add_command(label="Удалить курс", command=self.butt4)
        self.deletemenu.add_command(label="Удаление студента", command=self.butt9)
        self.deletemenu.add_command(label="Удаление группы", command=self.butt7)
        self.menubar.add_cascade(label="Удаление", menu=self.deletemenu)

        # меню добавления для админа
        self.newmenu = Menu(self.menubar, tearoff=0)
        self.newmenu.add_command(label="Добавить новый курс", command=self.butt3)
        self.newmenu.add_command(label="Добавление новой группы", command=self.butt6)
        self.newmenu.add_command(label="Добавление студента", command=self.butt8)
        self.newmenu.add_command(label="Измененеи студента по id", command=self.butt11)
        self.newmenu.add_command(label="Добавление Пользователя", command=self.butt12)
        self.menubar.add_cascade(label="Добавление", menu=self.newmenu)
        self.root.config(menu=self.menubar)

# главное окно
roota = Tk()
roota.title("Аутентификация")
roota.minsize(150, 100)
roota.resizable(width=False, height=False)
log = Entry(roota, width=15)
log.grid(row=2, column=1, padx=(1, 1))
passwd = Entry(roota, width=15)
passwd.grid(row=3, column=1, padx=(1, 1))

# метод для авторизации пользователей
def aft():
    text = univer.aft(log.get(), passwd.get())
    if (str(text[0]) == "0"):
        # вызов метода для отображения интерфейса администратора
        admin()
    else:
        if (str(text[0]) == "1"):
            # вызов метода для отображения интерфейса простого пользователя
            user()
        else:
            # создание окна для отображения ошибки авторизации
            rooter = Tk()
            rooter.title("ERROR")
            rooter.minsize(50, 50)
            out = Text(rooter, bg="white", font="Arial 12", width=50, height=10)
            out.grid(row=1, column=1, padx=(1, 1))
            out.insert("0.0",
                       "ERROR!: Вы ввели не верный логин или пароль." + "\n" + " Либо Вы не зарегистрированны в приложении.")
            rooter.mainloop()

l = Label(roota, text="Логин")
p = Label(roota, text="Пароль")
b = Button(roota, text="Авторизация", bg="white", fg="black", font="Arial", width=22, height=1, command=aft)
b.grid(row=4, column=1, padx=(1, 1))

#метод отображения интерфейса администратора
def admin():
    b = MenuAdmin()

    but = Button(b.bottom_frame_1, text="Посмотреть все группы", bg="white",command=b.butt)
    but1 = Button(b.bottom_frame_2, text="Посмотреть всех студентов", command=b.butt1)
    but3 = Button(b.bottom_frame_3, text="Список студентов группы", command=b.butt5)
    but4 = Button(b.bottom_frame_1, text='Студент по фамилии', command=b.butt10)

    but5 = Button(b.bottom_frame_2, text="Добавить новый курс",command=b.butt3)
    but6 = Button(b.bottom_frame_3, text="Добавление новой группы", command=b.butt6)
    but7 = Button(b.bottom_frame_1, text='Добавление студента',command=b.butt8)
    but8 = Button(b.bottom_frame_2, text='Изменение студента по id', command=b.butt11)
    but9 = Button(b.bottom_frame_3, text='Добавление пользователя', command=b.butt12)

    but10 = Button(b.bottom_frame_1, text="Удалить курс", command=b.butt4)
    but11 = Button(b.bottom_frame_2, text='Удаление студента', command=b.butt9)
    but12 = Button(b.bottom_frame_3, text="Удаления группы", command=b.butt7)
    buttons = []
    buttons.extend([but,but1,but3, but4,but5,but6,but7,but8,but9,but9,but10,but11,but12])
    for button in buttons[:10]:
        button.configure(bg="lightblue", fg="blue", font="Century", width=25, height=1)
    for button in buttons[10:]:
        button.configure(bg="lightblue", fg="red", font="Century", width=25, height=1)
    # Расстановка кнопок и элементов
    but.pack(side=LEFT)
    but1.pack(side=LEFT)
    but3.pack(side=LEFT)

    but4.pack(side=LEFT)
    but5.pack(side=LEFT)
    but6.pack(side=LEFT)

    but7.pack(side=LEFT)
    but8.pack(side=LEFT)
    but9.pack(side=LEFT)

    but10.pack(side=LEFT)
    but11.pack(side=LEFT)
    but12.pack(side=LEFT)

    b.root.update()
    b.root.mainloop()

def user():
    a = Men()
    but = Button(a.bottom_frame_1, text="Посмотреть все группы",
                 command=a.butt)
    but1 = Button(a.bottom_frame_2, text="Посмотреть всех студентов",
                  command=a.butt1)
    but5 = Button(a.bottom_frame_3, text="Список студентов группы",
                  command=a.butt5)
    but10 = Button(a.bottom_frame_4, text='Студент по фамилии',
                   command=a.butt10)
    buttons = []
    buttons.extend([but,but1,but5,but10,])
    for button in buttons:
        button.configure(bg="lightblue", fg="blue", font="Century'", width=100, height=1)
    # Расстановка кнопок и элементов
    but.pack(side=TOP)
    but1.pack(side=TOP)
    but5.pack(side=TOP)
    but10.pack(side=TOP)
    a.root.update()
    a.root.mainloop()
    #кнопки управленя информацией

roota.mainloop()