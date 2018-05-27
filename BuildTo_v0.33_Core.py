#BuildTo_v0.33_Core
# -*- coding: utf-8 -*-

import xlrd
import commands
import random

print ('  ','[1] ','Ввод команды')
print ('  ','[2] ','Help')
print ('  ','[3] ','Рандомайзер')
print ('  ','[4] ','Куда я попал? Выход!')
start = input()
while start != '4':
    if start == '2':
        print('Основные команды:')
        print('  ','[1] Основной заказ: Булки')
        print('  ','[2] Основной заказ: Фризер')
        print('  ','[3] Основной заказ: Кулер')
        print('  ','[4] Основной заказ: Сухой-продукты')
        print('  ','[5] Основной заказ: Сухой-не продукты')
        print('  ','[6] Фреш')
        print('  ', '[7] Меню')
        print('')
        print('Дни:')
        print('  ', '[m] Понедельник')
        print('  ', '[t] Вторник')
        print('  ', '[w] Среда')
        print('')
        print('Структура команды:')
        print('[Основная команда]_[день]')
        print('________________________________________________________________')
        print('')
        print('  ', '[1] ', 'Ввод команды')
        print('  ', '[2] ', 'Help')
        print('  ', '[3] ', 'Рандомайзер')
        print('  ', '[4] ', 'Куда я попал? Выход!')
        start = input()
    elif start == '1':
        USER = input("Введите команду: ")
        if USER == '1_m':
            #Понедельник-булки
            commands.monday_rolls()
        elif USER == '2_m':
            #Понедельник-фризер
            commands.monday_freez()
        elif USER == '3_m':
            #Понедельник-кулер
            commands.monday_cooler()
        elif USER == '4_m':
            #Понедельник-сухой продукты
            commands.monday_prodWarehouse()
        elif USER == '5_m':
            #Понедельник-сухой не продукты
            commands.monday_UnProdWarehouse()
        elif USER == '6_m':
            #Понедельник-фреш
            commands.monday_fresh()
        # -------------------------------------------------------------#
        elif USER == '1_t':
            #Вторник-булки
            commands.tuesday_rolls()
        elif USER == '2_t':
            #Вторник-фризер
            commands.tuesday_freez()
        elif USER == '3_t':
            #Вторник-кулер
            commands.tuesday_cooler()
        elif USER == '4_t':
            #Вторник-сухой продукты
            commands.tuesday_prodWarehouse()
        elif USER == '5_t':
            #Вторник-сухой не продукты
            commands.tuesday_UnProdWarehouse()
        elif USER == '6_t':
            #Вторник-фреш
            commands.tuesday_fresh()
        # -------------------------------------------------------------#
        elif USER == '1_w':
            # Среда-булки
            commands.wednesday_rolls()
        elif USER == '2_w':
            # Среда-фризер
            commands.wednesday_freez()
        elif USER == '3_w':
            # Среда-кулер
            commands.wednesday_cooler()
        elif USER == '4_w':
            # Среда-сухой продукты
            commands.wednesday_prodWarehouse()
        elif USER == '5_w':
            # Среда-сухой не продукты
            commands.wednesday_UnProdWarehouse()
        elif USER == '6_w':
            # Среда-фреш
            commands.wednesday_fresh()
        elif USER == '7':
            print('________________________________________________________________')
            print('')
            print('  ', '[1] ', 'Ввод команды')
            print('  ', '[2] ', 'Help')
            print('  ', '[3] ', 'Рандомайзер')
            print('  ', '[4] ', 'Куда я попал? Выход!')
            start = input()
        else:
            print('Введите верную команду')
    else:
        print('    1  наименование для проверки: -->', random.randrange(1, 196, 1))
        print('    2  наименование для проверки: -->', random.randrange(1, 196, 1))
        print('    3  наименование для проверки: -->', random.randrange(1, 196, 1))
        print('    4  наименование для проверки: -->', random.randrange(1, 196, 1))
        print('    5  наименование для проверки: -->', random.randrange(1, 196, 1))
        print('    2  наименование для проверки: -->', random.randrange(1, 196, 1))
        print('    7  наименование для проверки: -->', random.randrange(1, 196, 1))
        print('    8  наименование для проверки: -->', random.randrange(1, 196, 1))
        print('    9  наименование для проверки: -->', random.randrange(1, 196, 1))
        print('    10 наименование для проверки: -->', random.randrange(1, 196, 1))
        print('________________________________________________________________')
        print('  ', '[1] ', 'Ввод команды')
        print('  ', '[2] ', 'Help')
        print('  ', '[3] ', 'Рандомайзер')
        print('  ', '[4] ', 'Куда я попал? Выход!')
        start = input()

