# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fiblist = [1, 1]
    while len(fiblist) <= m:
        fiblist.append(fiblist[len(fiblist) - 2] + fiblist[len(fiblist) - 1])
    print(fiblist[n:m])
    pass


fibonacci(100, 110)


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for num in range(len(origin_list)):

        i = 0
        while i < len(origin_list) - 1:
            if origin_list[i] > origin_list[i + 1]:
                origin_list.append(origin_list.pop(i))
            else:
                i += 1
    print(origin_list)
    pass


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

test = ['mike', 'jorn', 'den', 0, '']


def cap(x):
    return x.capitalize()
    pass


def new_filter(original_func, original_list):
    new_list = []
    for el in original_list:
        if el:
            new_list.append(original_func(el))

    return new_list


print(new_filter(cap, test))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

A1 = (1, 3)
A2 = (2, 5)
A3 = (5, -2)
A4 = (6, 0)


def isparalellogramm(A, B, C, D):
    if B[0] - A[0] == D[0] - C[0] and B[1] - A[1] == D[1] - C[1]:
        print('Точки - вершины')
    else:
        'Это не вершины'


isparalellogramm(A1, A2, A3, A4)
