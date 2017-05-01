from  University_bd import  *
import tkinter
from tkinter import *

univer = University('localhost', 'university_anisov_dmitriy', 'root', '123456')
group = Group('localhost', 'university_anisov_dmitriy', 'root', '123456')
people = People('localhost', 'university_anisov_dmitriy', 'root', '123456')
student = Student('localhost', 'university_anisov_dmitriy', 'root', '123456')
#главное окно
root = Tk()
root.title("Информационная система 'Университет'")
root.minsize(380,300)
root.resizable(width=False, height=False)

#метод для просмотра всех групп в универе
def butt():
    texts = univer.printerGroups()
    for t in texts:
        output.insert("10.10",str(t)+"\n")

#метод для просмотра всех студентов в университете
def butt1():
    texts = univer.printerStudent()
    for t in texts:
        output.insert("0.0",str(t)+"\n")


#метод создания нового курса в университете
def butt3():
    # окно для добавления нового курса
    root1 = Tk()
    root1.title("Добавление нового курса")
    root1.minsize(270, 100)
    #поля для ввода данных о курсе
    a = Entry(root1, width=15)
    a.grid(row=1, column=2, padx=(10, 0))
    l = Label(root1,text = "Новый курс")
    l.grid(row=1, column=0, padx=(10, 0))
    a1 = Entry(root1, width=15)
    a1.grid(row=2, column=2, padx=(10, 0))
    l1 = Label(root1,text = "Индификатор курса для студента")
    l1.grid(row=2, column=0, padx=(10, 0))
    #метод для добавления нового курса
    def button1():
        t = univer.add_kyrs(a.get(), a1.get())
        output.insert("0.0", str(t) + "\n")
    #кнопка для добавления нового курса
    butt = tkinter.Button(root1, text = "Добавить", bg="white", fg="black", width=15,height=1,command=button1)
    butt.grid(row=4, column=0,padx=(10, 10))
    root1.mainloop()

#метод создания диалогового окна для удаления курса
def butt4():
    #окно для удаления курса
    root2 = Tk()
    root2.title("Удаление курса")
    root2.minsize(250, 50)
    # поле для ввода идентификатора удаляемого курса
    a = Entry(root2, width=17)
    a.grid(row=1, column=0, padx=(10, 10))
    l = Label(root2,text = "Номер курса")
    l.grid(row=1, column=1, padx=(10, 0))
    # метод для удаление курса
    def button2():
        output.edit_reset()
        t = univer.delete_kyrs(a.get())
        output.insert("0.0", str(t) + "\n")
    #кнопка для добавления нового автора
    butt = tkinter.Button(root2, text = "Удалить", bg="white", fg="black", width=15,height=1,command=button2)
    butt.grid(row=4, column=0,padx=(10, 0))
    root2.mainloop()
def butt5():
    #окно для вывода всех студентов конкретной группы
    root2 = Tk()
    root2.title("студенты конкретной группы")
    root2.minsize(250, 50)
    # поле для ввода группы
    a = Entry(root2, width=17)
    a.grid(row=1, column=0, padx=(10, 10))
    l = Label(root2,text = "id группы")
    l.grid(row=1, column=1, padx=(10, 0))
    # метод для поиска группы
    def button5():
        output.edit_reset()
        t = group.student_of_group(a.get())
        for t in t:
            output.insert("0.0", str(t) + "\n")
    #кнопка для посика студентов
    butt = tkinter.Button(root2, text = "Найти", bg="white", fg="black", width=15,height=1,command=button5)
    butt.grid(row=4, column=0,padx=(10, 0))
    root2.mainloop()
def butt6():
    # окно для добавления новой группы
    root1 = Tk()
    root1.title("Добавление новой группы")
    root1.minsize(270, 100)
    #поля для ввода данных о курсе
    a = Entry(root1, width=15)
    a.grid(row=1, column=2, padx=(10, 0))
    l = Label(root1,text = "Номер группы")
    l.grid(row=1, column=0, padx=(10, 0))
    a1 = Entry(root1, width=15)
    a1.grid(row=2, column=2, padx=(10, 0))
    l1 = Label(root1,text = "код факультета")
    l1.grid(row=2, column=0, padx=(10, 0))
    a2 = Entry(root1, width=15)
    a2.grid(row=3, column=2, padx=(10, 0))
    l2 = Label(root1, text="Курс")
    l2.grid(row=3, column=0, padx=(10, 0))
    #метод для добавления нового курса
    def button6():
        t = group.add_group(a.get(), a1.get(),a2.get())
        output.insert("0.0", str(t) + "\n")
    #кнопка для добавления нового курса
    butt = tkinter.Button(root1, text = "Добавить", bg="white", fg="black", width=15,height=1,command=button6)
    butt.grid(row=4, column=0,padx=(10, 10))
    root1.mainloop()
#окно для удаления курса

def butt7():
    root2 = Tk()
    root2.title("Удаление группы")
    root2.minsize(250, 50)
    # поле для ввода номеру удаляемой группы
    a = Entry(root2, width=17)
    a.grid(row=1, column=0, padx=(10, 10))
    l = Label(root2,text = "Номер группы")
    l.grid(row=1, column=1, padx=(10, 0))
    # метод для удаление группы
    def button2():
        output.edit_reset()
        t = group.delete_group(a.get())
        output.insert("0.0", str(t) + "\n")
    #кнопка для удаления группы
    butt = tkinter.Button(root2, text = "Удалить", bg="white", fg="black", width=15,height=1,command=button2)
    butt.grid(row=4, column=0,padx=(10, 0))
    root2.mainloop()

def butt8():
    root2 = Tk()
    root2.title("Добавление студента")
    root2.minsize(350, 100)
    a = Entry(root2,width =30)
    a.grid(row=1,column = 2, padx=(10,10))
    l = Label(root2,text = 'Имя')
    l.grid(row = 1, column=0,padx =(10,0))
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
        output.edit_reset()
        t = student.add_student(a.get(),a1.get(),a2.get(),a3.get(),a4.get(),a5.get(),a6.get())
        output.insert('0.0',str(t)+'\n')
    butt = tkinter.Button(root2,text = 'Добавить',bg = 'white',fg = 'black',width = 15,height =1,command = button8)
    butt.grid(row = 8,column = 2,padx = (10,0))
    root2.mainloop()
def butt9():
    root2 = Tk()
    root2.title('Удаление студента')
    root2.minsize(350,50)
    a = Entry(root2,width = 30)
    a.grid(row = 1,column = 2,padx = (10,10))
    l = Label(root2,text = 'Имя')
    l.grid(row =1,column = 0,padx=(10, 0))
    a2 = Entry(root2,width = 30)
    a2.grid(row=2,column = 2, padx =(10,10))
    l2 = Label(root2, text = 'Фамилия')
    l2.grid(row = 2,column = 0,padx=(10, 0))
    a3= Entry(root2, width=30)
    a3.grid(row=3, column=2, padx=(10, 10))
    l3 = Label(root2, text='Отчество')
    l3.grid(row=3, column=0,padx=(10, 0))
    def button9():
        output.edit_reset()
        t = student.delete_student(a.get(),a2.get(),a3.get())
        output.insert('0.0',str(t) +'\n')
    butt = tkinter.Button(root2,text = 'Удалить', bg = 'white',fg = 'black',width = 15,height = 1,command = button9)
    butt.grid(row = 4, column=2, padx=(10,0))

def butt10():
    root2 = Tk()
    root2.title('Студент по Фамилии')
    root2.minsize(350,50)
    a = Entry(root2,width = 30)
    a.grid(row = 1,column = 2,padx = (10,10))
    l = Label(root2,text = 'Фамилия')
    l.grid(row =1,column = 0,padx=(10, 0))

    def button10():
        output.edit_reset()
        t = student.get_student_second_name(a.get())
        output.insert('0.0',str(t) +'\n')
    butt = tkinter.Button(root2,text = 'Подробне о студенте', bg = 'white',fg = 'black',width = 30,height = 1,command = button10)
    butt.grid(row = 2, column=2, padx=(10,0))
#кнопки управленя информацией
but = Button(root, text="Посмотреть все группы", bg="white", fg="black", font="Arial", width=22,height=1,command=butt).grid(row=1, column=1, padx=(1, 1))
but1 = Button(root, text="Посмотреть всех студентов", bg="white", fg="black", font="Arial", width=22,height=1,command=butt1).grid(row=1, column=2, padx=(1, 1))
but3 = Button(root, text="Добавить новый курс",bg="white", fg="black", font="Arial", width=22,height=1, command=butt3).grid(row=2, column=1, padx=(1, 1))
but4 = Button(root, text="Удалить курс", bg="white", fg="black", font="Arial", width=22,height=1, command=butt4).grid(row=2, column=2, padx=(1, 1))
but5 = Button(root, text="Студенты конкретной группы", bg="white", fg="black", font="Arial", width=22,height=1,command=butt5).grid(row=3, column=1, padx=(1, 1))
but6 = Button(root, text="Добавление новой группы", bg="white", fg="black", font="Arial", width=22,height=1,command=butt6).grid(row=3, column=2, padx=(1, 1))
but7 = Button(root, text="удаления группы", bg="white", fg="black", font="Arial", width=22,height=1,command=butt7).grid(row=4, column=1, padx=(1, 1))
but8 = Button(root,text = 'Добавление студента',bg = 'white',fg='black',font = 'Arial',width = 22,height = 1, command = butt8).grid(row=4, column=2,padx=(1,1))
but9 = Button(root,text = 'Удаление студента',bg = 'white',fg='black',font = 'Arial',width = 22,height = 1, command = butt9).grid(row=5, column=1,padx=(1,1))
but10 = Button(root,text = 'Студент по фамилии',bg = 'white',fg='black',font = 'Arial',width = 22,height = 1, command = butt10).grid(row=5, column=2,padx=(1,1))
output = Text(root, bg="white", font="Arial 12", width=50, height=10)
output.grid(row=6, column=1,  columnspan=7)
scr = Scrollbar(root,command=output.yview)
output.configure(yscrollcommand=scr.set)
scr.grid(row=6, column=8)

root.mainloop()