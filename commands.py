<<<<<<< HEAD
import xlrd
import core

def xls (NOS):
    xl = xlrd.open_workbook(r'data.xls')
    s = xl.sheet_by_index(0)
    rl = s.row_values(NOS)
    return rl

#Понедельник-булки
def monday_rolls ():
    i = 8
    NOS = 2
    while NOS < i:
        rl = xls (NOS)
        name = rl[1]
        f = open(r'Blanks/BuildTo_rolls.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.monday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.monday_buildto(rl))
        NOS += 1
    print('')

#Понедельник-фризер
def monday_freez():
    i = 38
    NOS = 8
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_freez.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.monday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.monday_buildto(rl))
    print('')

#Понедельник-кулер
def monday_cooler():
    i = 60
    NOS = 38
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_cooler.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.monday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.monday_buildto(rl))
    print('')

#Понедельник-сухой-продукты
def monday_prodWarehouse():
    i = 111
    NOS = 60
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_prodWarehouse.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.monday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.monday_buildto(rl))
    print('')

#Понедельник-сухой не продукты
def monday_UnProdWarehouse():
    i = 194
    NOS = 111
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_UnProdWarehouse.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.monday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.monday_buildto(rl))
    print('')

#Понедельник-fresh
def monday_fresh():
    i = 207
    NOS = 194
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_fresh.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.fresh_monday(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.fresh_monday(rl))
    print('')

# -------------------------------------------------------------------------------#

#Вторник-булки
def tuesday_rolls ():
    i = 8
    NOS = 2
    while NOS < i:
        rl = xls (NOS)
        name = rl[1]
        f = open(r'Blanks/BuildTo_rolls.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.tuesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.tuesday_buildto(rl))
        NOS += 1
    print('')

#Вторник-фризер
def tuesday_freez():
    i = 40
    NOS = 8
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_freez.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.tuesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.tuesday_buildto(rl))
    print('')

#Вторник-кулер
def tuesday_cooler():
    i = 62
    NOS = 40
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_cooler.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.tuesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.tuesday_buildto(rl))
    print('')

#Вторник-сухой-продукты
def tuesday_prodWarehouse():
    i = 113
    NOS = 61
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_prodWarehouse.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.tuesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.tuesday_buildto(rl))
    print('')

#Вторник-сухой не продукты
def tuesday_UnProdWarehouse():
    i = 194
    NOS = 111
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_UnProdWarehouse.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.tuesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.tuesday_buildto(rl))
    print('')

#Вторник-fresh
def tuesday_fresh():
    i = 207
    NOS = 194
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_fresh.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.fresh_tuesday(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.fresh_tuesday(rl))
    print('')

# -------------------------------------------------------------------------------#

#Среда-булки
def wednesday_rolls ():
    i = 8
    NOS = 2
    while NOS < i:
        rl = xls (NOS)
        name = rl[1]
        f = open(r'Blanks/BuildTo_rolls.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.wednesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.wednesday_buildto(rl))
        NOS += 1
    print('')

#Среда-фризер
def wednesday_freez():
    i = 38
    NOS = 8
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_freez.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.wednesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.wednesday_buildto(rl))
    print('')

#Среда-кулер
def wednesday_cooler():
    i = 60
    NOS = 38
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_cooler.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.wednesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.wednesday_buildto(rl))
    print('')

#Среда-сухой-продукты
def wednesday_prodWarehouse():
    i = 113
    NOS = 61
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_prodWarehouse.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.wednesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.wednesday_buildto(rl))
    print('')

#Среда-сухой не продукты
def wednesday_UnProdWarehouse():
    i = 194
    NOS = 111
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_UnProdWarehouse.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.wednesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.wednesday_buildto(rl))
    print('')

#Среда-fresh
def wednesday_fresh():
    i = 207
    NOS = 194
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_fresh.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.fresh_wednesday(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.fresh_wednesday(rl))
    print('')
=======
import xlrd
import core

def xls (NOS):
    xl = xlrd.open_workbook(r'data.xls')
    s = xl.sheet_by_index(0)
    rl = s.row_values(NOS)
    return rl

#Понедельник-булки
def monday_rolls ():
    i = 8
    NOS = 2
    while NOS < i:
        rl = xls (NOS)
        name = rl[1]
        f = open(r'Blanks/BuildTo_rolls.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.monday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.monday_buildto(rl))
        NOS += 1
    print('')

#Понедельник-фризер
def monday_freez():
    i = 38
    NOS = 8
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_freez.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.monday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.monday_buildto(rl))
    print('')

#Понедельник-кулер
def monday_cooler():
    i = 60
    NOS = 38
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_cooler.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.monday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.monday_buildto(rl))
    print('')

#Понедельник-сухой-продукты
def monday_prodWarehouse():
    i = 111
    NOS = 60
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_prodWarehouse.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.monday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.monday_buildto(rl))
    print('')

#Понедельник-сухой не продукты
def monday_UnProdWarehouse():
    i = 194
    NOS = 111
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_UnProdWarehouse.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.monday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.monday_buildto(rl))
    print('')

#Понедельник-fresh
def monday_fresh():
    i = 207
    NOS = 194
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_fresh.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.fresh_monday(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.fresh_monday(rl))
    print('')

# -------------------------------------------------------------------------------#

#Вторник-булки
def tuesday_rolls ():
    i = 8
    NOS = 2
    while NOS < i:
        rl = xls (NOS)
        name = rl[1]
        f = open(r'Blanks/BuildTo_rolls.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.tuesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.tuesday_buildto(rl))
        NOS += 1
    print('')

#Вторник-фризер
def tuesday_freez():
    i = 38
    NOS = 8
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_freez.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.tuesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.tuesday_buildto(rl))
    print('')

#Вторник-кулер
def tuesday_cooler():
    i = 60
    NOS = 38
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_cooler.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.tuesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.tuesday_buildto(rl))
    print('')

#Вторник-сухой-продукты
def tuesday_prodWarehouse():
    i = 111
    NOS = 60
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_prodWarehouse.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.tuesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.tuesday_buildto(rl))
    print('')

#Вторник-сухой не продукты
def tuesday_UnProdWarehouse():
    i = 194
    NOS = 111
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_UnProdWarehouse.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.tuesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.tuesday_buildto(rl))
    print('')

#Вторник-fresh
def tuesday_fresh():
    i = 207
    NOS = 194
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_fresh.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.fresh_tuesday(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.fresh_tuesday(rl))
    print('')

# -------------------------------------------------------------------------------#

#Среда-булки
def wednesday_rolls ():
    i = 8
    NOS = 2
    while NOS < i:
        rl = xls (NOS)
        name = rl[1]
        f = open(r'Blanks/BuildTo_rolls.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.wednesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.wednesday_buildto(rl))
        NOS += 1
    print('')

#Среда-фризер
def wednesday_freez():
    i = 38
    NOS = 8
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_freez.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.wednesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.wednesday_buildto(rl))
    print('')

#Среда-кулер
def wednesday_cooler():
    i = 60
    NOS = 38
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_cooler.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.wednesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.wednesday_buildto(rl))
    print('')

#Среда-сухой-продукты
def wednesday_prodWarehouse():
    i = 111
    NOS = 60
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_prodWarehouse.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.wednesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.wednesday_buildto(rl))
    print('')

#Среда-сухой не продукты
def wednesday_UnProdWarehouse():
    i = 194
    NOS = 111
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_UnProdWarehouse.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.wednesday_buildto(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.wednesday_buildto(rl))
    print('')

#Среда-fresh
def wednesday_fresh():
    i = 207
    NOS = 194
    while NOS < i:
        rl = xls(NOS)
        name = rl[1]
        NOS += 1
        f = open(r'Blanks/BuildTo_fresh.csv', 'a')
        l = [1]
        for index in l:
            f.write(str(name) + str(core.fresh_wednesday(rl)) + '\n')
            # f.write('n')
        f.close()
        print(name, '  ', core.fresh_wednesday(rl))
    print('')
>>>>>>> master
