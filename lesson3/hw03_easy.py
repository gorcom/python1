# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    num = 1 if int(str(number).split('.')[1][ndigits]) > 4 else 0
    new_number = (int(str(number * (10 ** ndigits)).split('.')[0]) + num) / 10 ** ndigits
    return new_number


print(my_round(2.1234567, 5))
print(my_round(2.1999327, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) < 6:
        return "Не правильный билет"
    else:
        x1 = [int(i) for i in list(str(ticket_number)[0:3])]
        y1 = [int(i) for i in list(str(ticket_number)[3:6])]
    ticket = 'lucky' if sum(x1) == sum(y1) else 'no lucky'
    return ticket


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
