import pandas as pd
import numpy as np

from tkinter import *
from tkinter import filedialog as fd

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from statsmodels.sandbox.distributions.examples.ex_mvelliptical import fig

import library.base as base

from library.colors import color_main
from library.colors import color_button
from library.colors import color_text


def text1():
    """
    Функция сохранения текстового отчета
    Автор: Выдренкова Екатерина
    Входные параметры: нет
    Выходные параметры: нет
    """

    base.table_n4 = pd.merge(base.table_n2, base.table_n1)
    np.savetxt(r'output\age_sport.txt', base.table_n4[['Вид спорта', 'Фамилия']], fmt='%s', encoding='UTF-8')


def text2():
    """
    Функция сохранения текстового отчета
    Автор: Ляпунова Софья
    Входные параметры: нет
    Выходные параметры: нет
    """

    np.savetxt(r'output\surname_name_phone.txt', base.table_n1[['Фамилия', 'Имя', 'Телефон']], fmt='%s', encoding='UTF-8')


def text3():
    """
    Функция сохранения текстового отчета
    Автор: Выдренкова Екатерина
    Входные параметры: нет
    Выходные параметры: нет
    """
    base.table_n4 = pd.merge(base.table_n3, base.table_n1)
    np.savetxt(r'output\surname_sport_attendance.txt', base.table_n4[['Фамилия', 'Вид спорта', 'Посещаемость']], fmt='%s', encoding='UTF-8')

def text4():
    """
    Функция сохранения текстового отчета
    Автор: Ляпунова Софья
    Входные параметры: нет
    Выходные параметры: нет
    """
    base.table_n4 = pd.merge(base.table_n2, base.table_n1)
    np.savetxt(r'output\surname_sport_phone.txt', base.table_n4[['Фамилия', 'Вид спорта', 'Телефон']], fmt='%s', encoding='UTF-8')


def text5():
    """
    Функция сохранения текстового отчета
    Автор: Выдренкова Екатерина
    Входные параметры: нет
    Выходные параметры: нет
    """
    base.table_n4 = pd.merge(base.table_n3, base.table_n1)
    # print(base.table_n4)
    base.table_n4 = pd.merge(base.table_n4, base.table_n2)
    # print(base.table_n4)
    del base.table_n4['Номер спорта']
    del base.table_n4['Номер пола']
    np.savetxt(r'output\full_text.txt', base.table_n4, fmt='%s', encoding='UTF-8')



def text6():
    """
    Функция сохранения текстового отчета
    Автор: Ляпунова Софья
    Входные параметры: нет
    Выходные параметры: нет
    """
    np.savetxt(r'output\full_index.txt', base.table_n1, fmt='%s', encoding='UTF-8')


def text7():
    """
    Функция сохранения текстового отчета
    Автор: Ляпунова Софья
    Входные параметры: нет
    Выходные параметры: нет
    """
    base.table_n4 = pd.merge(base.table_n3, base.table_n1)
    # print(base.table_n4)
    base.table_n4 = pd.merge(base.table_n4, base.table_n2)
    # print(base.table_n4)
    np.savetxt(r'output\gender_sport.txt', base.table_n4[['Пол', 'Вид спорта']], fmt='%s', encoding='UTF-8')


def export_excel():
    """
    Функция записи таблицы клиентов в эксель
    Автор: Выдренкова Екатерина
    Входные параметры: нет
    Выходные параметры: нет
    """
    writer = pd.ExcelWriter(r'output\table.xlsx', engine='xlsxwriter')
    base.table_n1.to_excel(writer, 'Sheet1')
    writer.save()


def report1(table_n1, table_n3):
    """
    Верстка окна выбора графика
    Автор: Ляпунова Софья, Выдренкова Екатерина
    Входные параметры: главная таблица, таблица с гендерами
    Выходные параметры: нет
    """
    root = Tk()
    root.minsize(500, 400)
    root.maxsize(500, 450)
    root.resizable(False, False)
    root.configure(bg=color_main)



    def Plot(table_n1):
        """
        Окно графиков распределения по возрастам
        Параметры:
        table_n1 - БД
        Автор: Ляпунова Софья
        Входные параметры: главная таблица
        Выходные параметры: нет
        """

        def save_plot():
            """
            Функция сохранения графика с возможностью выбора имени и пути файла
            Автор: Ляпунова Софья
            Входные параметры: нет
            Выходные параметры: нет
            """
            name = fd.asksaveasfilename(filetypes=(("PNG", "*.png"), ("all files", "*.*")))
            fmt = name + ".png"
            fig.savefig(fmt)

        def Pie_Age():
            """
            Строит круговую диаграмму по распределению возрастов
            Автор: Выдренкова Екатерина
            Входные параметры: нет
            Выходные параметры: нет
            """
            ax.cla()
            ax.set_title("Распределение возрастов")
            Types = table_n1['Возраст'].unique()
            TTypes = []
            for Type in Types:
                SEL = (table_n1['Возраст'] == Type)
                TTypes.append(len(table_n1[SEL]))
            ax.grid()
            ax.pie(TTypes, labels=Types, autopct='%1.1f%%', pctdistance=0.9, shadow=False, startangle=90)
            ax.axis('equal')
            graph.draw()
            pplf.update()

        def Scatter_Age():
            """
            Диаграмма рассеивания по возрастам
            Автор: Ляпунова Софья
            Входные параметры: нет
            Выходные параметры: нет
            """
            ax.cla()
            ax.set_title("Рассеивание возрастов")
            ax.set_xlabel('Номер')
            ax.set_ylabel('Возраст')
            # print(base.table_n1['Возраст'])
            ax.scatter(x=base.table_n1['Номер'], y=base.table_n1['Возраст'])
            ax.axis('equal')
            graph.draw()
            pplf.update()

        pplf = Toplevel(master=root)
        pplf.title("Графики")
        pplf.minsize(800, 600)
        pplf.maxsize(800, 600)
        pplf.resizable(False, False)
        pplf.configure(bg=color_main)
        controls1 = Frame(pplf, height=50, width=400, bg=color_main)
        controls1.pack(side=TOP, pady=3)
        PriceText = Label(controls1, bg=color_main, text="Распределение возрастов", font=("Arial", 15), fg=color_text)
        PriceText.pack(side=LEFT, padx=5, pady=3)
        BVTable1 = Button(controls1, text="Круговая\nдиаграмма", font=("Arial", 12), bg=color_button, fg=color_text,
                          width=15, height=2, command=Pie_Age)
        BVTable1.pack(side=LEFT, padx=5, pady=3)

        DispTable1 = Button(controls1, text="Диаграмма\nрассеивания", font=("Arial", 12), bg=color_button, fg=color_text,
                            width=15, height=2, command=Scatter_Age)
        DispTable1.pack(side=LEFT, padx=5, pady=3)

        fig = Figure()
        ax = fig.add_subplot(111)
        ax.grid()
        graph = FigureCanvasTkAgg(fig, master=pplf)
        graph.get_tk_widget().pack(side=TOP, fill=BOTH, pady=7, expand=True)
        Other = Frame(pplf, height=50, width=400, bg=color_main)
        Other.pack(side=TOP, pady=3)
        SaveBut = Button(Other, text="Сохранить", bg=color_button, fg=color_text, width=15, height=1, command=save_plot)
        SaveBut.pack(side=LEFT, padx=5, pady=3)
        StopBut = Button(Other, text="Выход", bg=color_button, fg=color_text, width=15, height=1,
                         command=lambda: pplf.destroy())
        StopBut.pack(side=LEFT, padx=5, pady=3)
        pplf.mainloop()

    def Help_age():
        """
        Вспомогательная функция вызова окна графиков распределения по возрасту
        Автор: Выдренкова Екатерина
        Входные параметры: нет
        Выходные параметры: нет
        """
        Plot(table_n1)

    def Sport_kind_window(table_n1):
        """
        Окно построения графиков распределения по видам спорта
        Параметры:
        table_n1 - БД
        Автор: Ляпунова Софья
        Входные параметры: главная таблица
        Выходные параметры: нет

        """

        def save_plot():
            """
            Функция сохранения графика с возможностью выбора имени и пути файла
            Автор: Ляпунова Софья
            Входные параметры: нет
            Выходные параметры: нет
            """
            name = fd.asksaveasfilename(filetypes=(("PNG", "*.png"), ("all files", "*.*")))
            fmt = name + ".png"
            fig.savefig(fmt)

        def Hist_sport():
            """
            Строит столбчатую диаграмму по видам спорта
            Автор: Ляпунова Софья
            Входные параметры: нет
            Выходные параметры: нет
            """
            ax.cla()
            ax.set_title("Распределение по видам спорта")
            ax.set_ylabel("Количество видов спорта", rotation=90)
            base.table_n4 = pd.merge(base.table_n2, base.table_n1)
            ax.grid(axis='y')
            ax.hist(base.table_n4['Вид спорта'], 50, color='royalblue', histtype='barstacked', )
            graph.draw()
            pplf.update()

        def Pie_sport():
            """
            Строит круговую диаграмму по видам спорта
            Автор: Выдренкова Екатерина
            Входные параметры: нет
            Выходные параметры: нет
            """
            ax.cla()
            ax.set_title("Распределение по видам спорта")
            base.table_n4 = pd.merge(base.table_n2, base.table_n1)
            Types = base.table_n4['Вид спорта'].unique()
            TTypes = []
            for Type in Types:
                SEL = (base.table_n4['Вид спорта'] == Type)
                TTypes.append(len(table_n1[SEL]))
            ax.grid()
            ax.pie(TTypes, labels=Types, autopct='%1.1f%%', shadow=False, startangle=90)
            ax.axis('equal')
            graph.draw()
            pplf.update()

        def Scatter_sport():
            """
            Строит диаграмму рассеивания по видам спорта
            Автор: Ляпунова Софья
            Входные параметры: нет
            Выходные параметры: нет
            """
            ax.cla()
            base.table_n5 = pd.merge(base.table_n3, base.table_n1)
            base.table_n4 = pd.merge(base.table_n5, base.table_n2)
            ax.set_title("Рассеивание по видам спорта")
            ax.set_xlabel('Вид спорта')
            ax.set_ylabel('Возраст')
            ax.scatter(x=base.table_n4['Вид спорта'], y=base.table_n4['Пол'])
            ax.axis('equal')
            graph.draw()
            pplf.update()

        pplf = Toplevel(master=root)
        pplf.title("Графики")
        pplf.minsize(800, 600)
        pplf.maxsize(800, 600)
        pplf.resizable(False, False)
        pplf.configure(bg=color_main)
        controls2 = Frame(pplf, height=50, width=400, bg=color_main)
        controls2.pack(side=TOP, pady=3)
        RateText = Label(controls2, bg=color_main, text="Распределение видов спорта", font=("Arial", 15),
                         fg=color_text)
        RateText.pack(side=LEFT, padx=5, pady=3)
        ColTable2 = Button(controls2, text="Столбчатая\nдиаграмма", font=("Arial", 12), bg=color_button,
                           fg=color_text, width=15, height=2, command=Hist_sport)
        ColTable2.pack(side=LEFT, padx=5, pady=3)
        BVTable2 = Button(controls2, text="Круговая\nдиаграмма", font=("Arial", 12), bg=color_button, fg=color_text,
                          width=15, height=2, command=Pie_sport)
        BVTable2.pack(side=LEFT, padx=5, pady=3)
        DispTable2 = Button(controls2, text="Диаграмма\nрассеивания", font=("Arial", 12), bg=color_button, fg=color_text,
                            width=15, height=2, command=Scatter_sport)
        DispTable2.pack(side=LEFT, padx=5, pady=3)
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.grid()

        graph = FigureCanvasTkAgg(fig, master=pplf)
        graph.get_tk_widget().pack(side=TOP, fill=BOTH, pady=7, expand=True)
        Other = Frame(pplf, height=50, width=400, bg=color_main)
        Other.pack(side=TOP, pady=3)
        SaveBut = Button(Other, text="Сохранить", bg=color_button, fg=color_text, width=15, height=1, command=save_plot)
        SaveBut.pack(side=LEFT, padx=5, pady=3)
        StopBut = Button(Other, text="Выход", bg=color_button, fg=color_text, width=15, height=1,
                         command=lambda: pplf.destroy())
        StopBut.pack(side=LEFT, padx=5, pady=3)
        pplf.mainloop()

    def Help_sport():
        """
        Вспомогательная функция вызова окна графиков распределения виду спорта
        Автор: Выдренкова Екатерина
        Входные параметры: нет
        Выходные параметры: нет
        """
        Sport_kind_window(table_n1)

    def Gender_window(table_n1):
        """
        Окно построения графиков распределения по гендеру
        Параметры:
        table_n1 -  БД
        Автор: Ляпунова Софья
        Входные параметры: главная таблица
        Выходные параметры: нет
        """

        def save_plot():
            """
            Функция сохранения графика с возможностью выбора имени и пути файла.
            Автор: Ляпунова Софья
            Входные параметры: нет
            Выходные параметры: нет
            """
            name = fd.asksaveasfilename(filetypes=(("PNG", "*.png"), ("all files", "*.*")))
            fmt = name + ".png"
            fig.savefig(fmt)

        def Hist_gender():
            """
            Столбчатая диаграмма распределения по гендеру
            Автор: Выдренкова Екатерина
            Входные параметры: нет
            Выходные параметры: нет
            """
            ax.cla()
            base.table_n4 = pd.merge(base.table_n3, base.table_n1)
            ax.set_title("Распредление по гендеру")
            ax.set_ylabel("Количество людей", rotation=90)
            ax.grid(axis='y')
            ax.hist(base.table_n4['Пол'], 50, color='royalblue', histtype='barstacked', )
            graph.draw()
            pplf.update()

        def Pie_gender():
            """
            Круговая диаграмма распределения по гендеру
            Автор: Ляпунова Софья
            Входные параметры: нет
            Выходные параметры: нет
            """
            ax.cla()
            base.table_n4 = pd.merge(base.table_n3, base.table_n1)
            ax.set_title("Распредление по гендеру")
            Types = base.table_n4['Пол'].unique()
            TTypes = []
            for Type in Types:
                SEL = (base.table_n4['Пол'] == Type)
                TTypes.append(len(table_n1[SEL]))
            ax.grid()
            ax.pie(TTypes, labels=Types, autopct='%1.1f%%', shadow=False, startangle=90)
            ax.axis('equal')
            graph.draw()
            pplf.update()



        pplf = Toplevel(master=root)
        pplf.minsize(800, 600)
        pplf.maxsize(800, 600)
        pplf.resizable(False, False)
        pplf.configure(bg=color_main)
        controls1 = Frame(pplf, height=50, width=400, bg=color_main)
        controls1.pack(side=TOP, pady=3)
        PriceText = Label(controls1, bg=color_main, text="Распределение по гендеру", fg=color_text)
        PriceText.pack(side=LEFT, padx=5, pady=3)
        ColTable1 = Button(controls1, text="Столбчатая\nдиаграмма", bg=color_button, fg=color_text, width=15, height=2,
                           command=Hist_gender)
        ColTable1.pack(side=LEFT, padx=5, pady=3)
        BVTable1 = Button(controls1, text="Круговая\nдиаграмма", bg=color_button, fg=color_text, width=15, height=2,
                          command=Pie_gender)
        BVTable1.pack(side=LEFT, padx=5, pady=3)

        fig = Figure()
        ax = fig.add_subplot(111)
        ax.grid()
        graph = FigureCanvasTkAgg(fig, master=pplf)
        graph.get_tk_widget().pack(side=TOP, fill=BOTH, pady=7, expand=True)
        Other = Frame(pplf, height=50, width=400, bg=color_main)
        Other.pack(side=TOP, pady=3)
        SaveBut = Button(Other, text="Сохранить", bg=color_button, fg=color_text, width=15, height=1, command=save_plot)
        SaveBut.pack(side=LEFT, padx=5, pady=3)
        StopBut = Button(Other, text="Выход", bg=color_button, fg=color_text, width=15, height=1,
                         command=lambda: pplf.destroy())
        StopBut.pack(side=LEFT, padx=5, pady=3)
        pplf.mainloop()

    def Help_gender():
        """
        Вспомогательная функция вызова окна графиков по гендеру
        Автор: Выдренкова Екатерина
        Входные параметры: нет
        Выходные параметры: нет
        """
        Gender_window(table_n1)

    def Attendance_window(table_n1):
        """
        Окно построения графиков распределения по посещаемости
        Параметры:
        table_n1 - БД
        Автор: Выдренкова Екатерина
        Входные параметры: главная таблица
        Выходные параметры: нет
        """

        def save_plot():
            """
            Функция сохранения графика с возможностью выбора имени и пути файла.
            Автор: Ляпунова Софья
            Входные параметры: нет
            Выходные параметры: нет
            """
            name = fd.asksaveasfilename(filetypes=(("PNG", "*.png"), ("all files", "*.*")))
            fmt = name + ".png"
            fig.savefig(fmt)

        def Hist_attendance():
            """
            Строит столбчатую диаграмму распределения по посещаемости
            Автор: Выдренкова Екатерина
            Входные параметры: нет
            Выходные параметры: нет
            """
            ax.cla()
            ax.set_title("Посещаемость")
            ax.set_ylabel("Количество людей", rotation=90)
            Types = table_n1['Посещаемость'].unique()
            ax.set_xticklabels(Types, rotation=40, fontsize=8)
            ax.grid(axis='x')
            ax.hist(table_n1['Посещаемость'], 50, color='royalblue', histtype='barstacked', )
            graph.draw()
            pplf.update()

        def Pie_attendance():
            """
            Круговую диаграмма  распределения по посещаемости
            Автор: Ляпунова Софья
            Входные параметры: нет
            Выходные параметры: нет
            """
            ax.cla()
            ax.set_title("Посещаемость")
            Types = table_n1['Посещаемость'].unique()
            TTypes = []
            for Type in Types:
                SEL = (table_n1['Посещаемость'] == Type)
                TTypes.append(len(table_n1[SEL]))
            ax.grid()
            ax.pie(TTypes, labels=Types, autopct='%1.1f%%', shadow=False, startangle=90)
            ax.axis('equal')
            graph.draw()
            pplf.update()

        def Boxgraph_attendance():
            """
            Диаграмма размаха распределения по посещаемости
            Автор: Выдренкова Екатерина
            Входные параметры: нет
            Выходные параметры: нет
            """
            ax.cla()
            ax.set_title("Диаграмма размаха посещаемости")
            ax.boxplot(x=table_n1['Посещаемость'])
            ax.axis('equal')
            graph.draw()
            pplf.update()

        pplf = Toplevel(master=root)
        pplf.minsize(1100, 600)
        pplf.maxsize(1100, 600)
        pplf.resizable(False, False)
        pplf.configure(bg=color_main)
        controls1 = Frame(pplf, height=50, width=400, bg=color_main)
        controls1.pack(side=TOP, pady=3)
        PriceText = Label(controls1, bg=color_main, text="Посещаемость", fg=color_text)
        PriceText.pack(side=LEFT, padx=5, pady=3)
        ColTable1 = Button(controls1, text="Столбчатая\nдиаграмма", bg=color_button, fg=color_text, width=10, height=2,
                           command=Hist_attendance)
        ColTable1.pack(side=LEFT, padx=5, pady=3)
        BVTable1 = Button(controls1, text="Круговая\nдиаграмма", bg=color_button, fg=color_text, width=10, height=2,
                          command=Pie_attendance)
        BVTable1.pack(side=LEFT, padx=5, pady=3)
        DispTable1 = Button(controls1, text="Диаграмма\nБокса и Вискера", bg=color_button, fg=color_text, width=15, height=2, command=Boxgraph_attendance)
        DispTable1.pack(side=LEFT,padx=5,pady=3)
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.grid()
        graph = FigureCanvasTkAgg(fig, master=pplf)
        graph.get_tk_widget().pack(side=TOP, fill=BOTH, pady=7, expand=True)
        Other = Frame(pplf, height=50, width=400, bg=color_main)
        Other.pack(side=TOP, pady=3)
        SaveBut = Button(Other, text="Сохранить", bg=color_button, fg=color_text, width=15, height=1, command=save_plot)
        SaveBut.pack(side=LEFT, padx=5, pady=3)
        StopBut = Button(Other, text="Выход", bg=color_button, fg=color_text, width=15, height=1,
                         command=lambda: pplf.destroy())
        StopBut.pack(side=LEFT, padx=5, pady=3)
        pplf.mainloop()

    def Help_attendance():
        """
        Вспомогательная функция вызова окна графиков распределения по посещаемости
        Автор: Ляпунова Софья
        Входные параметры: нет
        Выходные параметры: нет
        """
        Attendance_window(table_n1)

    """
    Верстка кнопок выбора графика
    """

    Button1 = Button(root, text="Возраст", font=("Arial", 15), bg=color_button, fg=color_text,
                     width=20, command=Help_age)
    Button1.place(x=135, y=50)

    Button2 = Button(root, text="Вид спорта", font=("Arial", 15), bg=color_button, fg=color_text,
                     width=20, command=Help_sport)
    Button2.place(x=135, y=120)

    Button3 = Button(root, text="Гендер", font=("Arial", 15), bg=color_button, fg=color_text,
                     width=20, command=Help_gender)
    Button3.place(x=135, y=190)

    Button4 = Button(root, text="Посещаемость", font=("Arial", 15), bg=color_button, fg=color_text,
                     width=20, command=Help_attendance)
    Button4.place(x=135, y=260)

    root.mainloop()