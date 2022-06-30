
import pandas as pd

import library.base as base

def Del_line(index):
    """
    Автор: Ляпунова Софья, Выдренкова Екатерина
    Входные данные: Индекс удаляемой строки
    Выходные данные: Нет
    """
    revenue1 = int(base.table_n1.iloc[index]["Номер"])
    base.table_n1 = base.table_n1.drop(index, axis = 'rows')
    base.table_n1 = base.table_n1.reset_index(drop = True)
    data = list(base.table_n1["Номер"])



def Add_line(id_, name_,surname_,age_,gender_,phone_,sport_,attendance_):
    """
    Автор: Ляпунова Софья, Выдренкова Екатерина
    Входные данные: Значения новой строки БД
    Выходные значения: 0 - если новая строка, 1 в остальных случаях
    """
    values = [id_, name_, surname_, age_, gender_, phone_, sport_, attendance_]
    index = base.table_n1.index.argmax() + 1
    base.table_n1.loc[index] = values
    if Dublicates(base.table_n1):
        Del_line(index - 1)
        return 1
    else:
        revenue1 = int(base.table_n1.iloc[index]["Номер"])
        index = base.table_n2.index.argmax() + 1
        base.table_n2.loc[index] = [revenue1, revenue1 * 12]
        if Dublicates(base.table_n2):
            base.table_n2 = base.table_n2.drop_duplicates()
        return 0


def Modification(index, column, value):
    """
    Автор: Ляпунова Софья, Выдренкова Екатерина
    Входные данные: Индекс строки, название колонки, значение.
    Выходные данные: 0, если произошла модификация ячейки и 1, если её не случилось по причине появления дубликата
    """
    buffer = base.table_n1.iloc[index][column]
    base.table_n1.at[index, column]= value
    if Dublicates(base.table_n1):
        base.table_n1.at[index, column] = buffer
        return 1
    else:
        base.table_n1.at[index, column] = value
        return 0

def Dublicates(data):
    """
    Входные данные: pandas DataFrame
    Выходны данные: True, если в базе есть дубликаты, False в противном
    """
    data = data[data.duplicated()]
    if data.empty:
        return False
    else:
        return True
