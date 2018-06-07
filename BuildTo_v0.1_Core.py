
# # print(s.nrows) # Вывод количества строк
# # print (s.ncols) # Вывод количества столбцов
# # r1=print(s.row_values(0)) # Вывод всей первой строки. Индекс 0 - начало
# # print(s.col_values(0))  # Вывод всей первого столбца
#
# # # Получает срез значений из 2 столбца из диапазона строк 2-3 (по сути  второй строки таблицы
# # g = s.col_values(2,2)
# # print (g)


#BuildTo_v0.1_Core
import xlrd
import statistics

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
    CS = x[2]
    usingWeek = x[3]
    usingFr = x[4]
    usingSun = x[5]
    STOCK = x[6]
    USEFRID = (usingWeek*5)+usingFr+(usingSun*2)
    RESERVE = reserve*(statistics.mean([usingSun,usingFr,usingWeek])/CS)
    FRID = ((USEFRID-STOCK)/CS)+RESERVE
    TAILS = FRID - RESERVE
    USETUED = usingWeek*3
    TUED = ((USETUED - TAILS)/CS)+((usingWeek*reserve)/CS)
    buildTo = ('Заказ на Пт -- Вт --->', round(FRID), '---> ', round(TUED))
    return buildTo

def WEDNESDAY_BUILDTO(x):
    reserve = 1
    CS = x[2]
    usingWeek = x[3]
    usingFr = x[4]
    usingSun = x[5]
    STOCK = x[6]
    USEFRID = (usingWeek*3)+usingFr+(usingSun*2)
    RESERVE = reserve*(statistics.mean([usingSun,usingFr,usingWeek])/CS)
    FRID = ((USEFRID-STOCK)/CS)+RESERVE
    TAILS = FRID - RESERVE
    USETUED = usingWeek*3
    TUED = ((USETUED - TAILS)/CS)+((usingWeek*reserve)/CS)
    buildTo = ('Заказ на Пт -- Вт --->', round(FRID), '---> ', round(TUED))
    return buildTo

xl = xlrd.open_workbook(r'F:\HTML\Python\WWXLS\data.xls') #Открываем лист для работы
s = xl.sheet_by_index(0) # Выбор листа для работы
rl = s.row_values(2)
print(rl)

print('Choose your Day ')
USER = input()
if USER == 'Понедельник':
    print(MONDAY_BUILDTO(rl))
elif USER == 'Вторник':
    print(TUESDAY_BUILDTO(rl))
elif USER == 'Среда':
    print(WEDNESDAY_BUILDTO(rl))
else:
    print('Please Choose Mn, Tu or Wed')




