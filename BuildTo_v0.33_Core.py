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
    reserve = 1  # Переменная, определяющая запас в сутках
    #Получаю данные из списка
    CS = x[2] #Кейсовость наименования
    usingWeek = x[3] #Использование в будние дни
    usingFr = x[4] #Использование в Пятницу
    usingSun = x[5] #Использование в Выходные дни
    STOCK = x[6] #Остатки на складе
    # Рассчитываю общие значения для формулы
    USEFRID = (usingWeek*4)+usingFr+(usingSun*2) #Суммарное использование для заказа на Пятницу
    # Расчёт значения запаса исходя из среднего использования и коэффициента (в сутках)
    RESERVE = reserve*(statistics.mean([usingSun,usingFr,usingWeek])/CS)
    # Расчёт количества кейсов наимнования для заказа на Пятницу
    FRID = ((USEFRID-STOCK)/CS)+RESERVE
    # Расчёт остатков на начало дня Вторника
    TAILS = FRID - RESERVE
    # Расчёт использования на второй период
    USETUED = usingWeek*3
    TUED = ((USETUED - TAILS)/CS)+((usingWeek*reserve)/CS)
    buildTo = ('Заказ на Пт -- Вт --->', round(FRID), '---> ', round(TUED))
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

print('Chose your Day ')
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
    print(TUESDAY_BUILDTO(rl))
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
