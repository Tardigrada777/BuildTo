<<<<<<< HEAD
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

=======
#BuildTo_v0.33_Core
# -*- coding: utf-8 -*-
import xlrd
import statistics
import math

def fresh_tuesday(x):
    CS = x[2]
    usingWeek = x[3]
    usingFr = x[4]
    usingSun = x[5]
    stock = x[6]
    USEFRID = (usingWeek*4)+usingFr+(usingSun*2)
    FRID = ((USEFRID-STOCK)/CS)
    TUED = usingWeek*3
    BuildTo = ('Заказ на Пт --> Вт: ', round(FRID), round(TUED))
    return BuildTo

def TUESDAY_BUILDTO(x):
    reserve = 1
    cs = x[2]
    usingWeek = x[3]
    usingFr = x[4]
    usingSun = x[5]
    STOCK = x[6]
    USEFRID = (usingWeek * 4) + usingFr + (usingSun * 2)
    RESERVE = reserve * (statistics.mean([usingSun, usingFr, usingWeek]) / cs)
    MEAN = statistics.mean([usingSun, usingFr, usingWeek])
    if (USEFRID - STOCK) < 0:
        if MEAN >= abs(USEFRID - STOCK):
            FRIDR = math.ceil(RESERVE)
        else:
            FRIDR = 0
        FRID = FRIDR
        TAILS = FRID
        USETUED = (usingWeek * 3) - TAILS
        TUED = (USETUED / cs) + (usingWeek * reserve) / cs
    elif (USEFRID - STOCK) == 0:
        FRID = RESERVE
        USETUED = usingWeek * 3
        TUED = ((USETUED - FRID) / cs) + ((usingWeek * reserve) / cs)
    else:
        FRID = ((USEFRID - STOCK) / cs) + RESERVE
        TAILS = FRID
        USETUED = usingWeek * 3
        TUED = ((USETUED - TAILS) / cs) + ((usingWeek * reserve) / cs)
    buildTo = ('Заказ на Пт и Вт', round(FRID), round(TUED), ' ')
    return buildTo

def MONDAY_BUILDTO(x):
    reserve = 1
    cs = x[2]
    usingWeek = x[3]
    usingFr = x[4]
    usingSun = x[5]
    STOCK = x[6]
    USEFRID = (usingWeek*5)+usingFr+(usingSun*2)
    RESERVE = reserve*(statistics.mean([usingSun,usingFr,usingWeek])/cs)
    MEAN = statistics.mean([usingSun,usingFr,usingWeek])
    if (USEFRID-STOCK)<0:
        if MEAN >= abs(USEFRID-STOCK):
            FRIDR = math.ceil(RESERVE)
        else:
            FRIDR = 0
        FRID = FRIDR
        TAILS = FRID
        USETUED = (usingWeek * 3)- TAILS
        TUED = (USETUED / cs) + (usingWeek * reserve) / cs
    elif (USEFRID-STOCK)==0:
        FRID = RESERVE
        USETUED = usingWeek * 3
        TUED = ((USETUED - FRID) / cs) + ((usingWeek * reserve) / cs)
    else:
        FRID = ((USEFRID-STOCK)/cs)+RESERVE
        TAILS = FRID
        USETUED = usingWeek*3
        TUED = ((USETUED - TAILS)/cs)+((usingWeek * reserve) / cs)
    buildTo = ('Заказ на Пт и Вт', round(FRID), round(TUED), ' ')
    return buildTo

def WEDNESDAY_BUILDTO(x):
    reserve = 1
    cs = x[2]
    usingWeek = x[3]
    usingFr = x[4]
    usingSun = x[5]
    STOCK = x[6]
    USEFRID = (usingWeek * 3) + usingFr + (usingSun * 2)
    RESERVE = reserve * (statistics.mean([usingSun, usingFr, usingWeek]) / cs)
    MEAN = statistics.mean([usingSun, usingFr, usingWeek])
    if MEAN < cs / 2:
        FRIDR = 0
    else:
        FRIDR = RESERVE
    if (USEFRID - STOCK) < 0:
        FRID = FRIDR
        TAILS = USEFRID - STOCK
        USETUED = (usingWeek * 3) - TAILS
        if (usingWeek * reserve) > cs/2:
            TUED = (USETUED / cs) + ((usingWeek * reserve) / cs)
        else:
            TUED = (USETUED / cs)
    elif (USEFRID - STOCK) == 0:
        FRID = RESERVE
        USETUED = usingWeek * 3
        TUED = ((USETUED - FRID) / cs) + ((usingWeek * reserve) / cs)
    else:
        FRID = ((USEFRID - STOCK) / cs) + RESERVE
        TAILS = FRID - RESERVE
        USETUED = usingWeek * 3
        TUED = ((USETUED - TAILS) / cs) + ((usingWeek * reserve) / cs)
    buildTo = ('Заказ на Пт ', round(FRID), 'Заказ на Вт ', round(TUED))
    return buildTo

print('Выберите день расчёта заказа ')
USER = input()
if str(USER) == 'Понедельник':
    i = 206
    NOS = 195
    while NOS < i:
        xl = xlrd.open_workbook(r'data.xls')
        s = xl.sheet_by_index(0)
        rl = s.row_values(NOS)
        name = rl[1]
        NOS += 1
        f = open('BuildTo.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(MONDAY_BUILDTO(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', MONDAY_BUILDTO(rl))
elif str(USER) == 'Вторник':
    i = 195
    NOS = 2
    while NOS < i:
        xl = xlrd.open_workbook(r'data.xls')
        s = xl.sheet_by_index(0)
        rl = s.row_values(NOS)
        name = rl[1]
        NOS += 1
        f = open('BuildTo.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(TUESDAY_BUILDTO(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', TUESDAY_BUILDTO(rl))
    print('Расчёт заказа завершен успешно:', i+1, 'наименований')
elif str(USER) == 'Среда':
    print(WEDNESDAY_BUILDTO(rl))
elif str(USER) == 'fresh_tuesday':
    i = 207
    NOS = 195
    while NOS < i:
        xl = xlrd.open_workbook(r'data.xls')
        s = xl.sheet_by_index(0)
        rl = s.row_values(NOS)
        name = rl[1]
        NOS += 1
        f = open('BuildTo.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(MONDAY_BUILDTO(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', MONDAY_BUILDTO(rl))
else:
    print('Please Choose Mn, Tu or Wed')
>>>>>>> master
