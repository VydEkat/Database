import tkinter as tk
import tkinter.ttk as ttk
from logging import root
import pygame

import numpy as np
import pandas as pd
from tkinter import *
from tkinter import colorchooser

import library.script as ms
import library.base as base
import library.reports as rp

from library.colors import color_main
from library.colors import color_dop
from library.colors import color_button
from library.colors import color_text


def main_menu():
    """
    Функция интерфейса главного меню
    Автор: Ляпунова Софья, Выдренкова Екатерина
    Входные параметры: нет
    Выходные параметры: нет
    """
    root2 = tk.Tk()
    root2.geometry("850x600")
    x = 350
    y = 170
    root2.wm_geometry("+%d+%d" % (x, y))
    root2.title("Меню")
    root2.configure(bg=color_main)

    pygame.mixer.init()

    def play():
        """
        Функция включения фоновой музыки
        Автор: Выдренкова Екатерина
        Входные параметры: нет
        Выходные параметры: нет
        """
        pygame.mixer.music.load(r'data/python_muse.mp3')
        pygame.mixer.music.play(loops=0)

    def stop():
        """
            Функция выключения фоновой музыки
            Автор: Выдренкова Екатерина
            Входные параметры: нет
            Выходные параметры: нет
        """
        pygame.mixer.music.stop()

    def click():
        """
        Функция выхода из главного меню
        Автор: Ляпунова Софья, Выдренкова Екатерина
        Входные параметры: нет
        Выходные параметры: нет
        """

        def click_close():
            """
            Функция закрытия окна
            Автор: Ляпунова Софья
            Входные параметры: нет
            Выходные параметры: нет
            """
            root.destroy()

        newtable = base.table_n1

        def Show_clients():
            """
            Функция открытия и отрисовки таблицы "Клиенты"
            Автор: Ляпунова Софья
            Входные параметры: нет
            Выходные параметры: нет
            """

            def Add_newline():
                """
                Функция добавления новой строки
                Автор: Выдренкова Екатерина
                Входные параметры: нет
                Выходные параметры: нет
                """

                input = Toplevel(root)
                input.geometry("375x250")
                x = 400
                y = 150
                input.wm_geometry("+%d+%d" % (x, y))
                input.config(bg=color_main)

                def check(k):
                    return k.isdigit()

                def digit(c):
                    """
                    Функция преобразования строки в число
                    Автор: Ляпнунова Софья
                    Входные параметры: строка
                    Выходные параметры: число
                    """
                    if (c.isdigit() == True):
                        return int(c)

                def get():
                    """
                    Функция получения новых значений
                    Автор: Ляпунова Софья
                    Входные параметры: нет
                    Выходные параметры: нет
                    """
                    t = 1
                    id_ = entry_id.get()
                    if (id_.isdigit() == False):
                        t = 2
                    name_ = entry_name.get()
                    surname_ = entry_surname.get()
                    age_ = entry_age.get()
                    if (age_.isdigit() == False):
                        t = 2
                    gender_ = entry_gender.get()
                    if (gender_.isdigit() == False):
                        t = 2
                    phone_ = entry_phone.get()
                    if (phone_.isdigit() == False):
                        t = 2
                    sport_ = entry_sport.get()
                    if (sport_.isdigit() == False):
                        t = 2
                    attendance_ = entry_attendance.get()
                    if (attendance_.isdigit() == False):
                        t = 2

                    # print(id_, name_, surname_, age_, gender_, phone_, sport_, attendance_)

                    if (t == 2):
                        Err = Toplevel(input)
                        Err.geometry("365x60")
                        Err.config(bg=color_main)
                        x = 400
                        y = 200
                        Err.wm_geometry("+%d+%d" % (x, y))
                        lbl = tk.Label(Err, text="Ошибка. Неверно\nвведенны данные!", bg=color_button,
                                       fg=color_text, bd=2,
                                       font=("Times", 18))
                        lbl.grid(column=1, row=1)
                    else:
                        k = ms.Add_line(id_, name_, surname_, age_, gender_, phone_, sport_, attendance_)
                        if (k == 0):
                            Err = Toplevel(input)
                            Err.geometry("300x200")
                            Err.config(bg=color_main)
                            x = 400
                            y = 200
                            Err.wm_geometry("+%d+%d" % (x, y))
                            lbl = tk.Label(Err, text="Пользователь добавлен. \nОбновить таблицу? ",
                                           bg=color_button,
                                           fg=color_text, font=('Arial', 12), bd=1, width=35, height=2)
                            lbl.grid(column=1, row=1)

                            def deln():
                                Err.destroy()
                                input.destroy()
                                root.destroy()
                                Show_clients()

                            def deln2():
                                Err.destroy()
                                input.destroy()

                            btn = tk.Button(Err, text="Да", bg=color_button, fg=color_text, bd=2,
                                            font=("Arial", 14), height=1, width=10, command=deln)
                            btn2 = tk.Button(Err, text="Нет", bg=color_button, fg=color_text, bd=2,
                                             font=("Arial", 14), height=1, width=10, command=deln2)
                            btn.place(x=95, y=60)
                            btn2.place(x=95, y=120)
                            Err.mainloop()
                        else:
                            if (k == 1):
                                Err = Toplevel(input)
                                Err.geometry("180x120")
                                Err.config(bg=color_main)
                                x = 400
                                y = 200
                                Err.wm_geometry("+%d+%d" % (x, y))
                                lbl = tk.Label(Err, text="Строка не изменена, \nсуществует дубликат.", bg=color_main,
                                               fg=color_text, bd=2,
                                               font=('Arial', 13))
                                lbl.grid(column=1, row=1)

                                def deln():
                                    """
                                    Функция закрытия окона с ошибкой
                                    Автор: Выдренкова Екатерина
                                    Входные параметры: нет
                                    Выходные параметры: нет
                                    """

                                    Err.destroy()

                                btn = tk.Button(Err, text="Ок", bg=color_button, fg=color_text, bd=2,
                                                font=('Arial', 13), command=deln)
                                btn.grid(column=1, row=2)
                                Err.mainloop()

                lbl = tk.Label(input, text="Номер", bg=color_button, fg=color_text, bd=1, relief=tk.SUNKEN,
                               font=("Arial", 12), width=20)
                lbl.grid(column=0, row=0)

                lbl3 = tk.Label(input, text="Фамилия", bg=color_button, fg=color_text, bd=1, relief=tk.SUNKEN,
                                font=("Arial", 12), width=20)
                lbl3.grid(column=0, row=2)

                lbl2 = tk.Label(input, text="Имя", bg=color_button, fg=color_text, bd=1, relief=tk.SUNKEN,
                                font=("Arial", 12), width=20)
                lbl2.grid(column=0, row=1)

                lbl4 = tk.Label(input, text="Возраст", bg=color_button, fg=color_text, bd=1, relief=tk.SUNKEN,
                                font=("Arial", 12), width=20)
                lbl4.grid(column=0, row=3)

                lbl5 = tk.Label(input, text="Номер пола", bg=color_button, fg=color_text, bd=1, relief=tk.SUNKEN,
                                font=("Arial", 12), width=20)
                lbl5.grid(column=0, row=4)

                lbl6 = tk.Label(input, text="Телефон", bg=color_button, fg=color_text, bd=1, relief=tk.SUNKEN,
                                font=("Arial", 12), width=20)
                lbl6.grid(column=0, row=5)

                lbl7 = tk.Label(input, text="Номер спорта", bg=color_button, fg=color_text, bd=1, relief=tk.SUNKEN,
                                font=("Arial", 12), width=20)
                lbl7.grid(column=0, row=6)

                lbl8 = tk.Label(input, text="Посещаемость", bg=color_button, fg=color_text, bd=1, relief=tk.SUNKEN,
                                font=("Arial", 12), width=20)
                lbl8.grid(column=0, row=7)

                entry_id = tk.Entry(input, width=30)
                entry_id.grid(column=1, row=0)

                entry_name = tk.Entry(input, width=30)
                entry_name.grid(column=1, row=2)

                entry_surname = tk.Entry(input, width=30)
                entry_surname.grid(column=1, row=1)

                entry_age = tk.Entry(input, width=30)
                entry_age.grid(column=1, row=3)

                entry_gender = ttk.Combobox(input, state="readonly", width=27, values=("1", "2"))
                entry_gender.grid(column=1, row=4)

                entry_phone = tk.Entry(input, width=30)
                entry_phone.grid(column=1, row=5)

                entry_sport = ttk.Combobox(input, state="readonly", width=27, values=("1", "2", "3", "4", "5", "6"))
                entry_sport.grid(column=1, row=6)

                entry_attendance = tk.Entry(input, width=30)
                entry_attendance.grid(column=1, row=7)

                butt = tk.Button(input, text="Добавить", bg=color_button, fg=color_text, bd=2,
                                 font=("Arial", 15), height=1, width=15, command=get)
                butt.place(x=100, y=205)

            def report():
                """
                Функция открытия и отрисовки окна отчетов
                Автор: Выдренкова Екатерина, Ляпунова Софья
                Входные параметры: нет
                Выходные параметры: нет
                """

                new = Toplevel(root)
                new.geometry("300x200")
                x = 500
                y = 30
                new.wm_geometry("+%d+%d" % (x, y))
                new.config(bg=color_main)

                def click():
                    """
                    Функция открытия и отрисовки окна отчётов
                    Автор: Ляпунова Софья
                    Входные параметры: нет
                    Выходные параметры: нет
                    """

                    rp.report1(base.table_n1, base.table_n2)

                def click_8():
                    """
                    Функция закрытия окна отчётов
                    Автор: Ляпунова Софья
                    Входные параметры: нет
                    Выходные параметры: нет
                    """
                    new.destroy()

                lbl = tk.Label(new, text="Графические \n отчеты: ", bg=color_main, fg=color_text, bd=3,
                               font=("Arial", 15), height=2, width=18)
                lbl.place(x=50, y=20)

                btn = tk.Button(new, text="Отчет", bg=color_button, fg=color_text, bd=2,
                                font=("Arial", 14), height=1, width=10,
                                command=click)
                btn.place(x=90, y=100)

                btn8 = tk.Button(new, text="Назад", bg=color_button, fg=color_text, bd=2,
                                 font=("Arial", 14), height=1, width=10,
                                 command=click_8)
                btn8.place(x=90, y=150)

            def report_text():
                """
                Функция открытия и отрисовки окна "Текстовые Отчёты"
                Автор: Выдренкова Екатерина
                Входные параметры: нет
                Выходные параметры: нет
                """

                new = Toplevel(root)
                new.geometry("300x300")
                x = 500
                y = 30
                new.wm_geometry("+%d+%d" % (x, y))
                new.config(bg=color_main)

                def click():
                    """
                    Функция открытия и отрисовки окна отчётов
                    Автор: Ляпунова Софья, Выдренкова Екатерина
                    Входные параметры: нет
                    Выходные параметры: нет
                    """

                    Err = Toplevel(new)
                    Err.geometry("505x355")
                    Err.config(bg=color_main)
                    x = 400
                    y = 200
                    Err.wm_geometry("+%d+%d" % (x, y))

                    def click1():
                        """
                        Функция экспорта детских групп
                        Автор: Ляпунова Софья
                        Входные параметры: нет
                        Выходные параметры: нет
                        """
                        df = pd.pivot_table(base.table_n1[base.table_n1["Возраст"] < 18], index="Номер",
                                            columns="Номер спорта", values="Посещаемость")
                        with open(r'output\child_gropus.txt', encoding='utf-8', mode='w') as f:
                            print(df, file=f)
                        Err1 = Toplevel(Err)
                        Err1.geometry("505x100")
                        Err1.config(bg=color_main)
                        x = 400
                        y = 200
                        Err1.wm_geometry("+%d+%d" % (x, y))
                        lblh = tk.Label(Err1, text="Отчет child_groups находится в папке Output",
                                        bg=color_main, fg=color_text, bd=2, font=('Arial', 15))
                        lblh.place(x=10, y=10)

                    def click2():
                        """
                        Функция экспорта фитнесс группы
                        Автор: Выдренкова Екатерина
                        Входные параметры: нет
                        Выходные параметры: нет
                        """
                        df = pd.pivot_table(base.table_n1[base.table_n1["Номер спорта"] == 2], index="Номер",
                                            values="Посещаемость")
                        with open(r'output\fitness_group.txt', encoding='utf-8', mode='w') as f:
                            print(df, file=f)
                        Err1 = Toplevel(Err)
                        Err1.geometry("505x100")
                        Err1.config(bg=color_main)
                        x = 400
                        y = 200
                        Err1.wm_geometry("+%d+%d" % (x, y))
                        lblh = tk.Label(Err1, text="Отчет fitness_group находится в папке Output",
                                        bg=color_main, fg=color_text, bd=2, font=('Arial', 15))
                        lblh.place(x=10, y=10)

                    def click3():
                        """
                        Функция экспорта скидочной карты
                        Автор: Ляпунова Софья, Выдренкова Екатерина
                        Входные параметры: нет
                        Выходные параметры: нет
                        """
                        df = pd.pivot_table(base.table_n1[base.table_n1["Посещаемость"] > 15], index="Номер",
                                            values="Телефон")
                        with open(r'output\loyalty_card.txt', encoding='utf-8', mode='w') as f:
                            print(df, file=f)

                        Err1 = Toplevel(Err)
                        Err1.geometry("505x100")
                        Err1.config(bg=color_main)
                        x = 400
                        y = 200
                        Err1.wm_geometry("+%d+%d" % (x, y))
                        lblh = tk.Label(Err1, text="Отчет loyalty_card находится в папке Output",
                                        bg=color_main, fg=color_text, bd=2, font=('Arial', 15))
                        lblh.place(x=10, y=10)

                    def click4():
                        """
                        Функция экспорта статистики посещаемости
                        Автор: Ляпунова Софья
                        Входные параметры: нет
                        Выходные параметры: нет
                        """
                        df = base.table_n1[['Посещаемость']]
                        count = len(df)
                        df = df.groupby(['Посещаемость']).size().reset_index(name='count')
                        df['Частота'] = (df['count'] / count) * 100
                        np.savetxt(r'output\attendance_statistic.txt', df, fmt='%s')
                        Err1 = Toplevel(Err)
                        Err1.geometry("505x100")
                        Err1.config(bg=color_main)
                        x = 400
                        y = 200
                        Err1.wm_geometry("+%d+%d" % (x, y))
                        lblh = tk.Label(Err1, text="Отчет attendance_statistic находится в папке Output",
                                        bg=color_main, fg=color_text, bd=2, font=('Arial', 15))
                        lblh.place(x=10, y=10)

                    lblh = tk.Label(Err, text="Выберите вид текстового отчета: ",
                                    bg=color_main, fg=color_text, bd=2, font=('Arial', 15))
                    lblh.place(x=100, y=30)

                    btn1 = tk.Button(Err, text="Детская группа", bg=color_button, fg=color_text, bd=3,
                                     font=("Arial", 12), height=1, width=30,
                                     command=click1)
                    btn1.place(x=115, y=90)

                    btn2 = tk.Button(Err, text="Фитнес", bg=color_button, fg=color_text, bd=3,
                                     font=("Arial", 12), height=1, width=30,
                                     command=click2)
                    btn2.place(x=115, y=150)

                    btn3 = tk.Button(Err, text="Карта постоянного посетителя", bg=color_button, fg=color_text, bd=3,
                                     font=("Arial", 12), height=1, width=30,
                                     command=click3)
                    btn3.place(x=115, y=210)

                    btn4 = tk.Button(Err, text="Статистика посещений", bg=color_button, fg=color_text, bd=3,
                                     font=("Arial", 12), height=1, width=30,
                                     command=click4)
                    btn4.place(x=115, y=270)


                def click_8():
                    """
                    Функция закрытия окна отчётов
                    Автор: Выдренкова Екатерина
                    Входные параметры: нет
                    Выходные параметры: нет
                    """
                    new.destroy()

                def PivotTables():
                    """
                    Функция открытия окна сводных таблиц
                    Автор: Ляпунова Софья
                    Входные параметры: нет
                    Выходные параметры: нет
                    """

                    def export():
                        """
                        Функция экспорта сводной таблицы в эксель
                        Автор: Выдренкова Екатерина, Ляпунова Софья
                        Входные параметры: нет
                        Выходные параметры: нет
                        """
                        A1 = Atr1.get()
                        A2 = Atr2.get()
                        Ag = Agg.get()
                        df = base.table_n1.pivot_table(index=A1, columns=A2, aggfunc=Ag)
                        writer = pd.ExcelWriter(r'output\pivottable.xlsx', engine='xlsxwriter')
                        df.to_excel(writer, 'Sheet1')
                        writer.save()

                    def clicks():
                        """
                        Функция закрытия окна сводных таблиц
                        Автор: Выдренкова Екатерина
                        Входные параметры: нет
                        Выходные параметры: нет
                        """
                        Err.destroy()

                    Err = Toplevel(new)
                    Err.geometry("230x250")
                    Err.config(bg=color_main)
                    x = 400
                    y = 200
                    Err.wm_geometry("+%d+%d" % (x, y))
                    Atr1 = ttk.Combobox(Err, state="readonly", width=27,
                                        values=("Номер", "Фамилия", "Имя", "Возраст", "Номер пола", "Номер спорта"
                                                , "Посещаемость"))
                    Atr1.place(x=20, y=10)

                    Atr2 = ttk.Combobox(Err, state="readonly", width=27,
                                        values=("Номер", "Фамилия", "Имя", "Возраст", "Номер пола", "Номер спорта"
                                                , "Посещаемость"))
                    Atr2.place(x=20, y=40)

                    Agg = ttk.Combobox(Err, state="readonly", width=27, values=('mean', 'sum', 'count', 'min',
                                                                                'max'))
                    Agg.place(x=20, y=70)

                    btns = tk.Button(Err, text="Экспорт", bg=color_button, fg=color_text, bd=3,
                                     font=("Arial", 14), height=1, width=15,
                                     command=export)
                    btns.place(x=25, y=110)
                    btns2 = tk.Button(Err, text="Закрыть", bg=color_button, fg=color_text, bd=3,
                                      font=("Arial", 14), height=1, width=15,
                                      command=clicks)
                    btns2.place(x=25, y=160)

                lbl = tk.Label(new, text="Текстовые \n отчеты: ", bg=color_main, fg=color_text, bd=3,
                               font=("Arial", 15), height=2, width=18)
                lbl.place(x=50, y=20)

                btn = tk.Button(new, text="Отчет", bg=color_button, fg=color_text, bd=3,
                                font=("Arial", 14), height=1, width=15,
                                command=click)
                btn.place(x=60, y=100)

                btn2 = tk.Button(new, text="Сводная таблица", bg=color_button, fg=color_text, bd=3,
                                 font=("Arial", 14), height=1, width=15,
                                 command=PivotTables)
                btn2.place(x=60, y=150)

                btn8 = tk.Button(new, text="Назад", bg=color_button, fg=color_text, bd=3,
                                 font=("Arial", 14), height=1, width=15,
                                 command=click_8)
                btn8.place(x=60, y=200)

            def Delete_line(index):
                """
                Функция удаления строки
                Автор: Ляпунова Софья
                Входные параметры: нет
                Выходные параметры: нет
                """
                Err = Toplevel(labelframe)
                Err.geometry("320x200")
                Err.config(bg=color_main)
                x = 400
                y = 200
                Err.wm_geometry("+%d+%d" % (x, y))
                btn2 = tk.Button(Err, text="Точно хотите удалить?",
                                 bg=color_button, fg=color_text, font=('Arial', 12), bd=1, width=35, height=2)
                btn2.place(x=0, y=0)

                def deln():
                    """
                    Функция открытия окна + подтверждение обновления
                    Автор: Ляпунова Софья
                    Входные параметры: нет
                    Выходные параметры: нет
                    """
                    Err = Toplevel(labelframe)
                    Err.geometry("320x200")
                    Err.config(bg=color_main)
                    x = 400
                    y = 200
                    Err.wm_geometry("+%d+%d" % (x, y))
                    btn2 = tk.Button(Err, text="Обновите таблицу",
                                     bg=color_button, fg=color_text, font=('Arial', 12), bd=1, width=35, height=2)
                    btn2.place(x=0, y=0)

                    def update_button():
                        """
                        Функция обновления окна таблицы
                        Автор: Выдренкова Екатерина
                        Входные параметры: нет
                        Выходные параметры: нет
                        """

                        root.destroy()
                        Show_clients()

                    btn = tk.Button(Err, text="Обновить", bg=color_button, fg=color_text, font=('Arial', 13), bd=1,
                                    width=16, height=2, command=update_button)
                    btn.place(x=80, y=125)
                    ms.Del_line(index)

                def deln2():
                    """
                    Функция закрытия окна
                    Автор: Ляпунова Софья
                    Входные параметры: нет
                    Выходные параметры: нет
                    """
                    Err.destroy()

                btn = tk.Button(Err, text="Да", bg=color_button, fg=color_text, font=('Arial', 13), bd=1, width=8,
                                height=2, command=deln)
                btn2 = tk.Button(Err, text="Нет", bg=color_button, fg=color_text, font=('Arial', 13), bd=1, width=8,
                                 height=2, command=deln2)
                btn.place(x=40, y=125)
                btn2.place(x=190, y=125)
                Err.mainloop()

            def click_close():
                """
                Функция закрытия окна
                Автор: Ляпунова Софья
                Входные параметры: нет
                Выходные параметры: нет
                """

                root.destroy()

            def update_button():
                """
                Функция обновления таблицы
                Автор: Выдренкова Екатерина
                Входные параметры: нет
                Выходные параметры: нет
                """

                root.destroy()
                Show_clients()

            def export_to_txt():
                """
                Функция вывода текстовых отчётов
                Автор: Выдренкова Екатерина, Ляпунова Софья
                Входные параметры: нет
                Выходные параметры: нет
                """
                Err = Toplevel(labelframe)
                Err.geometry("500x400")
                Err.config(bg=color_main)
                x = 500
                y = 400
                Err.wm_geometry("+%d+%d" % (x, y))

                lblh = tk.Label(Err, text="Параметры для текстового файла: ",
                                bg=color_main, fg=color_text, bd=2, font=('Arial', 14))
                lblh.place(x=100, y=10)

                btn1 = tk.Button(Err, text="Вид спорта - Фамилия", bg=color_button, fg=color_text, font=('Arial', 10),
                                 bd=1, width=30, height=1, command=rp.text1)
                btn1.place(x=15, y=70)

                btn14 = tk.Button(Err, text="Пол - Вид спорта", bg=color_button, fg=color_text, font=('Arial', 10),
                                  bd=1, width=30, height=1, command=rp.text7)
                btn14.place(x=15, y=110)

                btn2 = tk.Button(Err, text="Фамилия - Имя - Телефон", bg=color_button, fg=color_text, font=('Arial', 10),
                                 bd=1, width=30, height=1, command=rp.text2)
                btn2.place(x=15, y=150)

                btn7 = tk.Button(Err, text="Фамилия - Вид спорта - Телефон", bg=color_button, fg=color_text,
                                 font=('Arial', 10),
                                 bd=1, width=30, height=1, command=rp.text4)
                btn7.place(x=15, y=190)

                btn3 = tk.Button(Err, text="Фамилия - Вид спорта - Посещаемость", bg=color_button, fg=color_text,
                                 font=('Arial', 10),
                                 bd=1, width=30, height=1, command=rp.text3)
                btn3.place(x=15, y=230)

                btn12 = tk.Button(Err, text="Объединенная \n таблица", bg=color_button, fg=color_text, font=('Arial', 10),
                                  bd=1, width=20, height=2, command=rp.text5)
                btn12.place(x=310, y=100)

                btn13 = tk.Button(Err, text="Общая \n таблица", bg=color_button, fg=color_text, font=('Arial', 10),
                                  bd=1, width=20, height=2, command=rp.text6)
                btn13.place(x=310, y=180)

                def export_close():
                    Err.destroy()

                close = tk.Button(Err, text="Назад", bg=color_button, fg=color_text, font=('Arial', 13), bd=1,
                                  width=15, height=2, command=export_close)
                close.place(x=325, y=340)

                lbl = tk.Label(Err, text="Отчет сохарняется автомачтически\nв папку output",
                               bg=color_main, fg=color_text, bd=2, font=('Arial', 13))
                lbl.place(x=15, y=340)

            def export_to_excel():
                """
                Функция вывода общей таблицы клиентов
                Автор: Ляпунова Софья
                Входные параметры: нет
                Выходные параметры: нет
                """
                rp.export_excel()

                Err = Toplevel(labelframe)
                Err.geometry("300x170")
                Err.config(bg=color_main)
                x = 400
                y = 200
                Err.wm_geometry("+%d+%d" % (x, y))
                btn2 = tk.Button(Err, text="Общая таблица клиентов \n сохранена в папке output",
                                 bg=color_button, fg=color_text, font=('Arial', 12), bd=1, width=35, height=2)
                btn2.place(x=0, y=10)

                def close_export_txt():
                    """
                    Функция закрытия окна
                    Автор: Выдренкова Екатерина
                    Входные параметры: нет
                    Выходные параметры: нет
                    """
                    Err.destroy()

                close = tk.Button(Err, text="Назад", bg=color_button, fg=color_text, font=('Arial', 13), bd=1,
                                  width=15, height=2, command=close_export_txt)
                close.place(x=150, y=115)

            def Edit_line(index):
                """
                Функция редактирования строки
                Автор: Ляпунова Софья, Выдренкова Екатерина
                Входные параметры: нет
                Выходные параметры: нет
                """

                def check(k, kn):
                    """
                    Функция проверки измененных данных
                    Автор: Ляпунова Софья, Выдренкова Екатерина
                    Входные параметры: атрибут и его значение
                    Выходные параметры: 1 - при правильном вводе,  0 - в неправильном
                    """

                    if (k == 'Номер'):
                        if (kn.isdigit() == False):
                            return 0
                        else:
                            return 1
                    else:
                        if (k == "Возраст"):
                            if (kn.isdigit() == True):
                                return 1
                            else:
                                return 0
                        else:
                            if (k == "Номер пола"):
                                if (kn.isdigit() == True):
                                    return 1
                                else:
                                    return 0
                            else:
                                if (k == "Телефон"):
                                    if (kn.isdigit() == True):
                                        return 1
                                    else:
                                        return 0
                                else:
                                    if (k == "Номер спорта"):
                                        if (kn.isdigit() == True):
                                            return 1
                                        else:
                                            return 0
                                    else:
                                        if (k == "Посещаемость"):
                                            if (kn.isdigit() == True):
                                                return 1
                                            else:
                                                return 0
                                        else:
                                            return 1

                def take():
                    """
                    Функция изменений строки
                    Автор: Выдренкова Екатерина
                    Входные параметры: нет
                    Выходные параметры: нет
                    """

                    def get1():
                        """
                        Функция получения значений и изменения строки
                        Автор: Ляпунова Софья
                        Входные параметры: нет
                        Выходные параметры: нет
                        """

                        kn = cr.get()
                        k = en.get()
                        s = check(k, kn)
                        if (s == 1):
                            sran = ms.Modification(index, k, kn)
                            # print(sran)
                            if (sran == 0):
                                Err = Toplevel(mag)
                                Err.geometry("300x200")
                                Err.config(bg=color_main)
                                x = 400
                                y = 200
                                Err.wm_geometry("+%d+%d" % (x, y))
                                btn2 = tk.Button(Err, text="Строка успешно изменена!\nОбновить таблицу?",
                                                 bg=color_button, fg=color_text, font=('Arial', 12), bd=1, width=35,
                                                 height=2)
                                btn2.place(x=0, y=0)

                                def deln():
                                    """
                                   Функция закрытия окон изменения и обновления таблицы
                                   Автор: Выдренкова Екатерина
                                   Входные параметры: нет
                                   Выходные параметры: нет
                                    """

                                    Err.destroy()
                                    mag.destroy()
                                    root.destroy()
                                    Show_clients()

                                def deln2():
                                    """
                                   Функция закрытия окон изменения без обновления
                                   Автор: Ляпунова Софья
                                   Входные параметры: нет
                                   Выходные параметры: нет
                                    """

                                    Err.destroy()
                                    mag.destroy()

                                btn = tk.Button(Err, text="Да", bg=color_button, fg=color_text, font=('Arial', 13), bd=1,
                                                width=8, height=2, command=deln)
                                btn2 = tk.Button(Err, text="Нет", bg=color_button, fg=color_text, font=('Arial', 13),
                                                 bd=1, width=8, height=2, command=deln2)
                                btn.place(x=40, y=125)
                                btn2.place(x=190, y=125)
                                Err.mainloop()
                            else:
                                if (sran == 1):
                                    Err = Toplevel(mag)
                                    Err.geometry("180x120")
                                    Err.config(bg=color_main)
                                    x = 400
                                    y = 200
                                    Err.wm_geometry("+%d+%d" % (x, y))
                                    lbl = tk.Label(Err, text="Строка не изменена, \nсуществует дубликат.",
                                                   bg=color_main,
                                                   fg=color_text, bd=2,
                                                   font=('Arial', 13))
                                    lbl.grid(column=1, row=1)

                                    def deln():
                                        """
                                        Функция закрытия окона с ошибкой
                                        Автор: Выдренкова Екатерина
                                        Входные параметры: нет
                                        Выходные параметры: нет
                                        """

                                        Err.destroy()

                                    btn = tk.Button(Err, text="Ок", bg=color_button, fg=color_text, bd=2,
                                                    font=('Arial', 13), command=deln)
                                    btn.grid(column=1, row=2)
                                    Err.mainloop()
                        else:
                            Err = Toplevel(mag)
                            Err.geometry("290x60")
                            Err.config(bg="#D1B8F4")
                            x = 400
                            y = 200
                            Err.wm_geometry("+%d+%d" % (x, y))
                            lbl = tk.Label(Err, text="Вы ввели неверные данные! \nПовторите попытку.", bg=color_button,
                                           fg=color_main, bd=2,
                                           font=("Times", 18, "italic"))
                            lbl.grid(column=1, row=1)

                    btn2 = tk.Button(mag, text="Изменить", bg=color_button, fg=color_text, font=('Arial', 13), bd=1,
                                     width=15, height=2,
                                     command=get1)
                    btn2.place(x=50, y=175)

                    if (en.get() == "Номер пола"):
                        cr = ttk.Combobox(mag, state="readonly", width=18, font=('Arial', 13),
                                          values=("1", "2"))
                        cr.place(x=29, y=144)
                        cr.get()
                    else:
                        if (en.get() == "Номер спорта"):
                            cr = ttk.Combobox(mag, state="readonly", width=18, font=('Arial', 13),
                                              values=("1", "2", "3", "4", "5", "6"))
                            cr.place(x=29, y=144)
                        else:
                            cr = tk.Entry(mag, bg=color_dop, font=('Arial', 13), width=20)
                            cr.place(x=30, y=145)

                mag = Toplevel(root)
                mag.geometry("250x250")
                x = 200
                y = 200
                mag.wm_geometry("+%d+%d" % (x, y))
                mag.config(bg=color_main)

                lb = tk.Label(mag, text="Параметр:", bg=color_button, fg=color_text, font=('Arial', 13), bd=1,
                              relief=tk.SUNKEN, width=20, height=1)
                lb.place(x=35, y=20)

                en = ttk.Combobox(mag, state="readonly", width=20, font=('Arial', 13), values=(
                    "Номер", "Фамилия", "Имя", "Возраст", "Номер пола", "Телефон", "Номер спорта",
                    "Посещаемость"))
                en.place(x=25, y=55)

                btn3 = tk.Button(mag, text="Выбрать", bg=color_button, fg=color_text, font=('Arial', 13), bd=1, width=15,
                                 height=2, command=take)
                btn3.place(x=50, y=85)

            root = tk.Toplevel()
            root.grid_rowconfigure(0, weight=1)
            root.columnconfigure(0, weight=1)
            root.title("Пользователь")
            w, h = root.winfo_screenwidth() - 100, root.winfo_screenheight() - 59
            root.geometry("1200x600+10+10")

            mainframe = tk.Frame(root)
            mainframe.place(x=10, y=0)
            labelframe = tk.Frame(mainframe, bg=color_dop, width=w, height=125)
            baseframe = tk.Frame(mainframe, bg=color_dop, width=w - 10, height=h - 125)

            photo = tk.PhotoImage(file="data/refresh.png")
            btn_update = tk.Button(labelframe, text="Обновить", image=photo, fg=color_text, font=('Arial', 13), bd=1,
                                   command=update_button)
            btn_update.place(x=18, y=7)
            lb = tk.Label(labelframe, text="Обновить", bg=color_dop, font=('Arial', 13))
            lb.place(x=7, y=60)

            photo2 = tk.PhotoImage(file="data/add.png")
            add_row_button = tk.Button(labelframe, text="Добавить", image=photo2, fg=color_text, font=('Arial', 13),
                                       bd=1, command=Add_newline)
            add_row_button.place(x=120, y=7)
            lb2 = tk.Label(labelframe, text="Добавить", bg=color_dop, font=('Arial', 13))
            lb2.place(x=110, y=60)

            lb3 = tk.Label(labelframe, text="Экспорт:", bg=color_dop, font=('Arial', 13))
            lb3.place(x=210, y=20)
            photo3 = tk.PhotoImage(file="data/load.png")
            btn_export_to_excel = tk.Button(labelframe, text=" .xlsx", image=photo3, fg=color_text,
                                            font=('Arial', 13), bd=1, command=export_to_excel)
            btn_export_to_excel.place(x=290, y=4)
            lb4 = tk.Label(labelframe, text=".xlsx", bg=color_dop, font=('Arial', 13))
            lb4.place(x=300, y=60)

            photo4 = tk.PhotoImage(file="data/load2.png")
            btn_export_to_txt = tk.Button(labelframe, text=".txt", image=photo4, fg=color_text,
                                          font=('Arial', 13), bd=1, command=export_to_txt)
            btn_export_to_txt.place(x=350, y=4)
            lb5 = tk.Label(labelframe, text=".txt", bg=color_dop, font=('Arial', 12))
            lb5.place(x=360, y=60)

            lb6 = tk.Label(labelframe, text="Отчёты:", bg=color_dop, font=('Arial', 12))
            lb6.place(x=460, y=20)
            photo5 = tk.PhotoImage(file="data/char.png")
            otch1 = tk.Button(labelframe, text="Графическик", image=photo5, fg=color_text, font=('Arial', 13),
                              bd=1, command=report)
            otch1.place(x=545, y=4)
            lb7 = tk.Label(labelframe, text="Графические", bg=color_dop, font=('Arial', 12))
            lb7.place(x=505, y=60)

            photo6 = tk.PhotoImage(file="data/text.png")
            otch2 = tk.Button(labelframe, text="Текстовые", image=photo6, fg=color_text, font=('Arial', 13),
                              bd=1, command=report_text)
            otch2.place(x=625, y=4)
            lb8 = tk.Label(labelframe, text="Текстовые", bg=color_dop, font=('Arial', 12))
            lb8.place(x=610, y=60)

            photo7 = tk.PhotoImage(file="data/back.png")
            Close = tk.Button(labelframe, text="Назад", image=photo7, fg=color_text, font=('Arial', 13), bd=1,
                              command=click_close)
            Close.place(x=1020, y=4)
            lb9 = tk.Label(labelframe, text="Назад", bg=color_dop, font=('Arial', 12))
            lb9.place(x=1020, y=60)

            def filter0():
                """
                Функция фильтрации основной таблицы
                Автор: Выдренкова Екатерина, Ляпунова Софья
                Входные параметры: нет
                Выходные параметры: нет
                """
                FilterMenu = Toplevel(labelframe)
                FilterMenu.geometry("505x325")
                FilterMenu.config(bg=color_main)
                x = 400
                y = 200
                FilterMenu.wm_geometry("+%d+%d" % (x, y))

                lb = tk.Label(FilterMenu, text="Посещаемость больше, чем:", bg=color_button, fg=color_text,
                              font=('Arial', 13), bd=1,
                              relief=tk.SUNKEN, width=30, height=1)
                lb.place(x=20, y=15)

                lb = tk.Label(FilterMenu, text="Посещаемость меньше, чем:", bg=color_button, fg=color_text,
                              font=('Arial', 13), bd=1,
                              relief=tk.SUNKEN, width=30, height=1)
                lb.place(x=20, y=75)

                lb = tk.Label(FilterMenu, text="Возраст больше, чем:", bg=color_button, fg=color_text, font=('Arial', 13),
                              bd=1,
                              relief=tk.SUNKEN, width=30, height=1)
                lb.place(x=20, y=135)

                lb = tk.Label(FilterMenu, text="Возраст меньше, чем:", bg=color_button, fg=color_text, font=('Arial', 13),
                              bd=1,
                              relief=tk.SUNKEN, width=30, height=1)
                lb.place(x=20, y=195)

                cr1 = tk.Entry(FilterMenu, bg=color_dop, font=('Arial', 13), width=30)
                cr1.place(x=20, y=45)

                cr2 = tk.Entry(FilterMenu, bg=color_dop, font=('Arial', 13), width=30)
                cr2.place(x=20, y=105)

                cr3 = tk.Entry(FilterMenu, bg=color_dop, font=('Arial', 13), width=30)
                cr3.place(x=20, y=165)

                cr4 = tk.Entry(FilterMenu, bg=color_dop, font=('Arial', 13), width=30)
                cr4.place(x=20, y=225)

                def filter1():
                    """
                    Функция фильтрации по посещаемости >
                    Автор: Ляпунова Софья
                    Входные параметры: нет
                    Выходные параметры: нет
                    """
                    base.table_n1 = newtable
                    k = int(cr1.get())
                    base.table_n1 = base.table_n1[base.table_n1["Посещаемость"] > k]
                    root.destroy()
                    Show_clients()

                def filter2():
                    """
                    Функция фильтрации по посещаемости <
                    Автор: Ляпунова Софья
                    Входные параметры: нет
                    Выходные параметры: нет
                    """
                    base.table_n1 = newtable
                    k = int(cr2.get())
                    base.table_n1 = base.table_n1[base.table_n1["Посещаемость"] < k]
                    root.destroy()
                    Show_clients()

                def filter3():
                    """
                    Функция фильтрации по возрасту >
                    Автор: Выдренкова Екаетерина
                    Входные параметры: нет
                    Выходные параметры: нет
                    """
                    base.table_n1 = newtable
                    k = int(cr3.get())
                    base.table_n1 = base.table_n1[base.table_n1["Возраст"] > k]
                    root.destroy()
                    Show_clients()

                def filter4():
                    """
                    Функция фильтрации по номеру выхода (меньше чем)
                    Автор: Выдренкова Екаетерина
                    Входные параметры: нет
                    Выходные параметры: нет
                    """
                    base.table_n1 = newtable
                    k = int(cr4.get())
                    base.table_n1 = base.table_n1[base.table_n1["Возраст"] < k]
                    root.destroy()
                    Show_clients()

                def otmena():
                    """
                    Функция фильтрации по времени
                    Автор: Ляпунова Софья
                    Входные параметры: нет
                    Выходные параметры: нет
                    """
                    base.table_n1 = newtable
                    root.destroy()
                    Show_clients()

                btn_update0 = tk.Button(FilterMenu, text="Отменить фильтры", bg=color_button, fg=color_text,
                                        font=('Arial', 13), bd=1,
                                        width=20, height=1, command=otmena)
                btn_update0.place(x=20, y=280)

                btn_update1 = tk.Button(FilterMenu, text="Обновить", bg=color_button, fg=color_text, font=('Arial', 13),
                                        bd=1,
                                        width=15, height=1, command=filter1)
                btn_update1.place(x=320, y=35)

                btn_update2 = tk.Button(FilterMenu, text="Обновить", bg=color_button, fg=color_text, font=('Arial', 13),
                                        bd=1,
                                        width=15, height=1, command=filter2)
                btn_update2.place(x=320, y=95)

                btn_update3 = tk.Button(FilterMenu, text="Обновить", bg=color_button, fg=color_text, font=('Arial', 13),
                                        bd=1,
                                        width=15, height=1, command=filter3)
                btn_update3.place(x=320, y=155)

                btn_update4 = tk.Button(FilterMenu, text="Обновить", bg=color_button, fg=color_text, font=('Arial', 13),
                                        bd=1,
                                        width=15, height=1, command=filter4)
                btn_update4.place(x=320, y=215)

            def sort():
                """
                Функция сортировки основной таблицы
                Автор: Ляпунова Софья, Выдренкова Екатерина
                Входные параметры: нет
                Выходные параметры: нет
                """
                SortMenu = Toplevel(labelframe)
                SortMenu.geometry("500x400")
                SortMenu.config(bg=color_main)
                x = 400
                y = 200
                SortMenu.wm_geometry("+%d+%d" % (x, y))

                def Surname_sort():
                    """
                    Функция сортировки по фамилии
                    Автор: Ляпунова Софья
                    Входные параметры: нет
                    Выходные параметры: нет
                    """
                    base.table_n1 = base.table_n1.sort_values(by='Фамилия')

                def Number_sort():
                    """
                    Функция сортировки номеру
                    Автор: Выдренкова Екатерина
                    Входные параметры: нет
                    Выходные параметры: нет
                    """
                    base.table_n1 = base.table_n1.sort_values(by='Номер')

                def Name_sort():
                    """
                    Функция сортировки по имени
                    Автор: Ляпунова Софья
                    Входные параметры: нет
                    Выходные параметры: нет
                    """
                    base.table_n1 = base.table_n1.sort_values(by='Имя')

                def Gender_sort():
                    """
                    Функция сортировки по номеру пола
                    Автор: Выдренкова Екатерина
                    Входные параметры: нет
                    Выходные параметры: нет
                    """
                    base.table_n1 = base.table_n1.sort_values(by='Номер пола')

                def Sport_sort():
                    """
                    Функция сортировки по номеру спорта
                    Автор: Ляпунова Софья
                    Входные параметры: нет
                    Выходные параметры: нет
                    """
                    base.table_n1 = base.table_n1.sort_values(by='Номер спорта')

                def Attendance_sort():
                    """
                    Функция сортировки по посещаемости
                    Автор: Выдренкова Екатерина
                    Входные параметры: нет
                    Выходные параметры: нет
                    """
                    base.table_n1 = base.table_n1.sort_values(by='Посещаемость')

                def Age_sort():
                    """
                    Функция сортировки по возрасту
                    Автор: Ляпунова Софья
                    Входные параметры: нет
                    Выходные параметры: нет
                    """
                    base.table_n1 = base.table_n1.sort_values(by='Возраст')

                def update():
                    """
                    Функция обновления таблицы
                    Автор: Выдренкова Екатерина, Ляпунова Софья
                    Входные параметры: нет
                    Выходные параметры: нет
                    """
                    root.destroy()
                    Show_clients()


                sort_kod = tk.Button(SortMenu, text="По фамилии", bg=color_button, fg=color_text,
                                     font=('Arial', 13), bd=1,
                                     width=20, height=2, command=Surname_sort)
                sort_kod.place(x=50, y=20)

                sort_flight = tk.Button(SortMenu, text="По номеру", bg=color_button, fg=color_text, font=('Arial', 13),
                                        bd=1,
                                        width=20, height=2, command=Number_sort)
                sort_flight.place(x=50, y=85)

                sort_plane = tk.Button(SortMenu, text="По имени", bg=color_button, fg=color_text, font=('Arial', 13),
                                       bd=1,
                                       width=20, height=2, command=Name_sort)
                sort_plane.place(x=260, y=20)

                sort_otpr = tk.Button(SortMenu, text="По гендеру", bg=color_button, fg=color_text, font=('Arial', 13),
                                      bd=1,
                                      width=20, height=2, command=Gender_sort)
                sort_otpr.place(x=50, y=145)

                sort_nazn = tk.Button(SortMenu, text="По номеру спорта", bg=color_button, fg=color_text,
                                      font=('Arial', 13),
                                      bd=1,
                                      width=20, height=2, command=Sport_sort)
                sort_nazn.place(x=260, y=85)

                sort_terminal = tk.Button(SortMenu, text="По посещаемости", bg=color_button, fg=color_text,
                                          font=('Arial', 13), bd=1,
                                          width=20, height=2, command=Attendance_sort)
                sort_terminal.place(x=50, y=205)

                sort_gate = tk.Button(SortMenu, text="По возрасту", bg=color_button, fg=color_text, font=('Arial', 13),
                                      bd=1,
                                      width=20, height=2, command=Age_sort)
                sort_gate.place(x=260, y=145)


                btn_update = tk.Button(SortMenu, text="Обновить", bg=color_button, fg=color_text, font=('Arial', 15),
                                       bd=2,
                                       width=20, height=2, command=update)
                btn_update.place(x=135, y=330)

            photo8 = tk.PhotoImage(file="data/sort.png")
            sortirovka = tk.Button(labelframe, text="Сортировать", image=photo8, fg=color_text, font=('Arial', 13),
                                   bd=1, command=sort)
            sortirovka.place(x=770, y=4)
            lb9 = tk.Label(labelframe, text="Сортировка", bg=color_dop, font=('Arial', 12))
            lb9.place(x=750, y=60)

            photo9 = tk.PhotoImage(file="data/filt.png")
            filtr = tk.Button(labelframe, text="Фильтр", image=photo9, fg=color_text, font=('Arial', 13), bd=1,
                              command=filter0)
            filtr.place(x=855, y=4)
            lb10 = tk.Label(labelframe, text="Фильтр", bg=color_dop, font=('Arial', 12))
            lb10.place(x=850, y=60)

            labelframe.grid()
            baseframe.grid(sticky='nws')
            baseframe.grid_rowconfigure(0, weight=1)
            baseframe.grid_columnconfigure(0, weight=1)
            baseframe.grid_propagate(False)
            cv = tk.Canvas(baseframe, bg="black")
            cv.grid(row=0, column=0, sticky="news")
            scrollframe = tk.Frame(cv, bg=color_main)
            k = base.table_n1
            scrollbar = tk.Scrollbar(baseframe, orient="vertical", command=cv.yview)
            cv.configure(yscrollcommand=scrollbar.set)
            cv.create_window((0, 0), window=scrollframe, width=w - 10, anchor='nw')

            # заголовок в таблице Эксель
            xt = 2
            yt = 105
            for i in list(k):
                cellname = tk.Label(labelframe, text=i, bg=color_button, fg=color_text, bd=1, relief=tk.SUNKEN, width=18)
                cellname.place(x=xt, y=yt)
                xt += 132

            # данные в таблице Эксель
            rw = 1
            cl = 0
            for i in k:
                for p in k[i]:
                    lb = tk.Label(scrollframe, text=p, bg=color_dop, fg=color_text, font=('Arial', 10), bd=1,
                                  relief=tk.SUNKEN, width=16)
                    lb.grid(row=rw, column=cl, pady=2, sticky="W" + "S")
                    rw += 1
                cl += 1
                rw = 1

            # кнопки удалить справа у экрана
            xt = 1080
            yt = 0
            j = 0
            while (j < 7):
                for i in range(base.table_n1.index.argmax() + 1):
                    mod_button = tk.Button(scrollframe, text="⌫", bg=color_dop, fg="black", font=('Arial', 8), bd=1,
                                           relief=tk.SUNKEN, command=lambda x=i: Edit_line(x))
                    mod_button.place(x=xt, y=yt)
                    xt += 24
                    del_button = tk.Button(scrollframe, text="✂", bg=color_dop, fg="black", font=('Arial', 8), bd=1,
                                           relief=tk.SUNKEN, command=lambda x=i: Delete_line(x))
                    del_button.place(x=xt, y=yt)
                    yt += 24
                    xt = 1080
                j += 1

            scrollframe.update_idletasks()
            scrollbar.grid(row=0, column=2, sticky="ns")
            cv.config(scrollregion=cv.bbox("all"))
            baseframe.config(width=w - 10, height=h - 160)
            root.mainloop()

        Show_clients()

    def click2():
        """
        Функция открытия таблицы с видами спорта
        Автор: Ляпунова Софья
        Входные параметры: нет
        Выходные параметры: нет
        """
        root3 = Toplevel(root2)
        root3.geometry("370x310")
        root3.config(bg=color_main)
        x = 450
        y = 10
        root3.wm_geometry("+%d+%d" % (x, y))

        def click_8():
            """
            Функция закрытия окна
            Автор: Ляпунова Софья
            Входные параметры: нет
            Выходные параметры: нет
            """

            root3.destroy()

        mainframe = tk.Frame(root3)
        mainframe.place(x=10, y=0)
        w, h = 350, root3.winfo_screenheight() - 390
        labelframe = tk.Frame(mainframe, bg=color_dop, width=w, height=125)
        baseframe = tk.Frame(mainframe, bg=color_dop, width=w - 10, height=h - 125)
        labelframe.grid()
        baseframe.grid(sticky='nws')
        baseframe.grid_rowconfigure(0, weight=1)
        baseframe.grid_columnconfigure(0, weight=1)
        baseframe.grid_propagate(False)
        cv = tk.Canvas(baseframe, bg=color_main)
        cv.grid(row=0, column=0, sticky="news")
        scrollframe = tk.Frame(cv, bg=color_main)

        Close = tk.Button(labelframe, text="Назад", bg=color_button, fg=color_text, font=('Arial', 13), bd=1,
                          width=15, height=2, command=click_8)
        Close.place(x=170, y=25)

        k = base.table_n2
        scrollbar = tk.Scrollbar(baseframe, orient="vertical", command=cv.yview)
        cv.configure(yscrollcommand=scrollbar.set)
        cv.create_window((0, 0), window=scrollframe, width=w - 10, anchor='nw')

        xt = 1
        yt = 103
        for i in list(k):
            cellname = tk.Label(labelframe, text=i, bg=color_button, fg=color_text, bd=1, relief=tk.SUNKEN, width=25)
            cellname.place(x=xt, y=yt)
            xt += 136

        rw = 1
        cl = 0
        for i in k:
            for p in k[i]:
                lb = tk.Label(scrollframe, text=p, bg=color_dop, fg=color_text, font=('Arial', 10), bd=1,
                              relief=tk.SUNKEN, width=19)
                lb.grid(row=rw, column=cl, pady=3, sticky="W" + "S")
                rw += 1
            cl += 1
            rw = 1

        xt = 1240
        yt = 4
        scrollframe.update_idletasks()
        scrollbar.grid(row=0, column=2, sticky="ns")
        cv.config(scrollregion=cv.bbox("all"))
        baseframe.config(width=w - 10, height=h - 160)
        root3.mainloop()

    def click3():
        """
        Функция открытия таблицы с гендерами
        Автор: Выдренкова Екатерина
        Входные параметры: нет
        Выходные параметры: нет
        """

        root3 = Toplevel(root2)
        root3.geometry("330x200")
        root3.config(bg=color_main)
        x = 450
        y = 10
        root3.wm_geometry("+%d+%d" % (x, y))

        def click_8():
            """
            Функция закрытия окна
            Автор: Выдренкова Екатерина
            Входные параметры: нет
            Выходные параметры: нет
            """
            root3.destroy()

        mainframe = tk.Frame(root3)
        mainframe.place(x=10, y=0)
        w, h = 310, root3.winfo_screenheight() - 500
        labelframe = tk.Frame(mainframe, bg=color_dop, width=w, height=125)
        baseframe = tk.Frame(mainframe, bg=color_dop, width=w - 10, height=h - 125)
        labelframe.grid()
        baseframe.grid(sticky='nws')
        baseframe.grid_rowconfigure(0, weight=1)
        baseframe.grid_columnconfigure(0, weight=1)
        baseframe.grid_propagate(False)
        cv = tk.Canvas(baseframe, bg=color_main)
        cv.grid(row=0, column=0, sticky="news")
        scrollframe = tk.Frame(cv, bg=color_main)

        Close = tk.Button(labelframe, text="Назад", bg=color_button, fg=color_text, font=('Arial', 13), bd=1,
                          width=15, height=2, command=click_8)
        Close.place(x=150, y=25)

        k = base.table_n3
        scrollbar = tk.Scrollbar(baseframe, orient="vertical", command=cv.yview)
        cv.configure(yscrollcommand=scrollbar.set)
        cv.create_window((0, 0), window=scrollframe, width=w - 10, anchor='nw')
        xt = 1
        yt = 103
        for i in list(k):
            cellname = tk.Label(labelframe, text=i, bg=color_button, fg=color_text, bd=1, relief=tk.SUNKEN, width=21)
            cellname.place(x=xt, y=yt)
            xt += 136

        rw = 1
        cl = 0
        for i in k:
            for p in k[i]:
                lb = tk.Label(scrollframe, text=p, bg=color_dop, fg=color_text, font=('Arial', 10), bd=1,
                              relief=tk.SUNKEN, width=17)
                lb.grid(row=rw, column=cl, pady=3, sticky="W" + "S")
                rw += 1
            cl += 1
            rw = 1

        xt = 1240
        yt = 4

        scrollframe.update_idletasks()
        scrollbar.grid(row=0, column=3, sticky="ns")
        cv.config(scrollregion=cv.bbox("all"))
        baseframe.config(width=w - 10, height=h - 160)
        root3.mainloop()

    def click6():
        """
        Функция открытия окна смены интерфейса
        Автор: Выдренкова Екатерина, Ляпунова Софья
        Входные параметры: нет
        Выходные параметры: нет
        """

        root3 = Toplevel(root2)
        root3.geometry("450x400")
        root3.config(bg=color_main)
        x = 450
        y = 10
        root3.wm_geometry("+%d+%d" % (x, y))

        with open('library/colors.py', 'r', encoding='utf-8') as f:
            array = f.readlines()

        zapas_main = color_main
        zapas_dop = color_dop
        zapas_knop = color_button
        zapas_text = color_text

        def func1():
            """
            Функция смены цвета фона
            Автор: Ляпунова Софья
            Входные параметры: нет
            Выходные параметры: нет
            """
            color_main = colorchooser.askcolor()[1]
            if color_main == None:
                color_main = zapas_main
            with open('library/colors.py', 'w', encoding='utf-8') as f:
                array[0] = 'color_main = "' + color_main + '"\n'
                f.writelines(array)

        def func2():
            """
            Функция смены дополнительного цвета
            Автор: Выдренкова Екатрерина
            Входные параметры: нет
            Выходные параметры: нет
            """
            color_dop = colorchooser.askcolor()[1]
            if color_dop == None:
                color_dop = zapas_dop
            with open('library/colors.py', 'w', encoding='utf-8') as f:
                array[1] = 'color_dop = "' + color_dop + '"\n'
                f.writelines(array)

        def func3():
            """
            Функция смены цвета кнопок
            Автор: Ляпунова Софья
            Входные параметры: нет
            Выходные параметры: нет
            """

            color_button = colorchooser.askcolor()[1]
            if color_button == None:
                color_button = zapas_knop
            with open('library/colors.py', 'w', encoding='utf-8') as f:
                array[2] = 'color_button = "' + color_button + '"\n'
                f.writelines(array)

        def func4():
            """
            Функция смены цвета текста
            Автор: Ляпунова Софья
            Входные параметры: нет
            Выходные параметры: нет
            """
            color_text = colorchooser.askcolor()[1]
            if color_text == None:
                color_text = zapas_text
            with open('library/colors.py', 'w', encoding='utf-8') as f:
                array[3] = 'color_text = "' + color_text + '"\n'
                f.writelines(array)

        lbls = tk.Label(root3, text="Изменение цветовой палитры", fg=color_text, bg=color_main,
                        bd=2, font=("Arial", 18), height=4, width=42)
        lbls.place(x=-60, y=-10)

        lbls = tk.Label(root3, text="Цвет фона:", fg=color_text, bg=color_main,
                        bd=2, font=("Arial", 15))
        lbls.place(x=15, y=90)

        btn1 = tk.Button(root3, text="Изменить", bg=color_button, fg=color_text, bd=2,
                         font=("Arial", 12), height=1, width=15,
                         command=func1)
        btn1.place(x=275, y=90)

        lbls = tk.Label(root3, text="Второй цвет фона:", fg=color_text, bg=color_main,
                        bd=2, font=("Arial", 15))
        lbls.place(x=15, y=130)

        btn2 = tk.Button(root3, text="Изменить", bg=color_button, fg=color_text, bd=2,
                         font=("Arial", 12), height=1, width=15,
                         command=func2)
        btn2.place(x=275, y=130)

        lbls = tk.Label(root3, text="Цвет кнопок:", fg=color_text, bg=color_main,
                        bd=2, font=("Arial", 15))
        lbls.place(x=15, y=170)

        btn3 = tk.Button(root3, text="Изменить", bg=color_button, fg=color_text, bd=2,
                         font=("Arial", 12), height=1, width=15,
                         command=func3)
        btn3.place(x=275, y=170)

        lbls = tk.Label(root3, text="Цвет текста:", fg=color_text, bg=color_main,
                        bd=2, font=("Arial", 15))
        lbls.place(x=15, y=210)

        btn4 = tk.Button(root3, text="Изменить", bg=color_button, fg=color_text, bd=2,
                         font=("Arial", 12), height=1, width=15,
                         command=func4)
        btn4.place(x=275, y=210)

        def click_cl():
            """
            Функция закрытия окна
            Автор: Выдренкова Екатерина
            Входные параметры: нет
            Выходные параметры: нет
            """
            root3.destroy()

        btn0 = tk.Button(root3, text="Назад", bg=color_button, fg=color_text, bd=2,
                         font=("Arial", 15), height=2, width=15,
                         command=click_cl)
        btn0.place(x=250, y=320)

        lbls = tk.Label(root3, text="Для обновления интерфейса", fg=color_text,
                        bg=color_main,
                        bd=2, font=("Arial", 10))
        lbls.place(x=30, y=330)
        lbls = tk.Label(root3, text="перезапустите программу.", fg=color_text, bg=color_main,
                        bd=2, font=("Arial", 10))
        lbls.place(x=30, y=350)

    def click5():
        """
        Функция закрытия окна
        Автор: Ляпунова Софья
        Входные параметры: нет
        Выходные параметры: нет
        """

        root2.destroy()

    music_button = tk.Button(root2, text="Включить музыку", bg=color_button, fg=color_text, bd=2,
                             font=("Arial", 15), height=2, width=19, command=play)
    music_button.place(x=70, y=290)

    music_button = tk.Button(root2, text="Остановить музыку", bg=color_button, fg=color_text, bd=2,
                             font=("Arial", 15), height=2, width=19, command=stop)
    music_button.place(x=300, y=290)

    lbls = tk.Label(root2, text="База данных спортивной школы", fg=color_text, bg=color_main,
                    bd=2, font=("Arial", 18), height=4, width=42)
    lbls.place(x=10, y=-20)

    btn = tk.Button(root2, text="Клиенты", bg=color_button, fg=color_text, bd=2,
                    font=("Arial", 15), height=2, width=40,
                    command=click)
    btn.place(x=70, y=80)

    btn2 = tk.Button(root2, text="Виды спорта", bg=color_button, fg=color_text, bd=2,
                     font=("Arial", 15), height=2, width=40,
                     command=click2)
    btn2.place(x=70, y=150)

    btn3 = tk.Button(root2, text="Гендеры", bg=color_button, fg=color_text, bd=2,
                     font=("Arial", 15), height=2, width=40,
                     command=click3)
    btn3.place(x=70, y=220)

    btn5 = tk.Button(root2, text="Выход", bg=color_button, fg=color_text, bd=2,
                     font=("Arial", 15), height=2, width=15,
                     command=click5)
    btn5.place(x=410, y=430)

    btn6 = tk.Button(root2, text="Смена интерфейса", bg=color_button, fg=color_text, bd=2,
                     font=("Arial", 15), height=2, width=20,
                     command=click6)
    btn6.place(x=10, y=430)

    root2.mainloop()

    return 0
