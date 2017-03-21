
import glob
import os.path
import re

migrations = 'Migrations'
files = glob.glob(os.path.join(migrations, '*.sql'))


def search_body():# тело программы
    while True: # открываем цикл
        print('Введите искомую строку:')
        search_world = input()
        all_files_in_serch = search(files, search_world)# запускаем функцию поиска и присваиваем эти значения
        for one_file in files:
            print(os.path.split(one_file))# возвращает список строк, которые получатся, если исходную строку разрезать на части по пробелам
        print('Найдено файлов:', len(all_files_in_serch))# вывод длины списка all_files_in_serch



def search(files, search_world):  # обозначаем функцию поиска с аргументами: файл и искомую строку
    all_files = [] # создаем пустой список
    for file in files:
        for open_file in open(file, 'r'): # для каждого открытого на чтение файла
            if search_world in open_file: # если искомое находится в открытом файле
                all_files.append(file) # добавляем название файла в список
                break
    return all_files



search_body()
