# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
import hw05_easy

in_dir = './'


def startmenu():
    print('1. Перейти в папку')
    print('2. Просмотреть содержимое текущей папки')
    print('3. Удалить папку')
    print('4. Создать папку')
    print('0. Выход')
    do = int(input('Выберете нужное действие(введите номер пункта): '))
    return do


do = startmenu()


def doit(do):
    if do == 0:
        print('exit')
    elif do == 1:
        print('Список подпапок: ')
        d_list = hw05_easy.dir_in_dir_whith_num(in_dir)
        d_list.update({'0': '../'})
        print('Для перехода на директорию выше введите 0')
        # print(len(d_list))
        # print(d_list)
        if len(d_list) > 0:
            go_to_folder = input('Введите номер папки для перехода в нее : ')
            hw05_easy.go_to_folder(d_list[go_to_folder])
            print(f'Вы перешли в папку {d_list[go_to_folder]}')
            print('Дальнейшие действия: ')
            do = startmenu()
            return int(do)
        else:
            print('Дочерних директорй нет')
            do = startmenu()
            return int(do)

    elif do == 2:
        print('Содержимое текущей директории: ')
        hw05_easy.files_in_dir(in_dir)
        print('')
        print('Дальнейшие действия: ')
        do = startmenu()
        return int(do)
    elif do == 3:
        print('Список подпапок: ')
        d_list = hw05_easy.dir_in_dir_whith_num(in_dir)
        # print(len(d_list))
        # print(d_list)
        if len(d_list) > 0:
            list_folder = input('Введите номер папки для ее удаления : ')
            hw05_easy.rm_dir(d_list[list_folder])
            print(f'Папка {d_list[list_folder]} удалена')
            print('Дальнейшие действия: ')
            do = startmenu()
            return int(do)
        else:
            print('Дочерних директорй нет')
            do = startmenu()
            return int(do)
    elif do == 4:
        print('Список подпапок в этой дериктории: ')
        d_list = hw05_easy.dir_in_dir_whith_num(in_dir)
        print('')
        new_dir_name = input('Введите имя новой директории: ')
        if len(new_dir_name) < 0:
            print('Имя не определено')
            do = startmenu()
            return int(do)
        else:
            hw05_easy.create_dir(new_dir_name)
            print(f'Директория {new_dir_name} создана')
            print('Дальнейшие действия: ')
            do = startmenu()
            return int(do)


while do != 0:
    do = doit(do)

# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из __easy.py
