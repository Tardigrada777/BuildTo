import statistics
import math

def fresh_monday(x):
    cs = x[2]
    usingWeek = x[3]
    usingFr = x[4]
    usingSun = x[5]
    stock = x[6]
    userfrid = (usingWeek*5)+usingFr+(usingSun*2)
    frid = ((userfrid-stock)/CS)
    tued = usingWeek*3
    BuildTo = ('Заказ на Пт --> Вт: ', round(frid), round(tued))
    return BuildTo

def fresh_tuesday(x):
    CS = x[2]
    usingWeek = x[3]
    usingFr = x[4]
    usingSun = x[5]
    stock = x[6]
    USEFRID = (usingWeek*4)+usingFr+(usingSun*2)
    FRID = ((USEFRID-stock)/CS)
    TUED = usingWeek*3
    BuildTo = ('Заказ на Пт --> Вт: ', round(FRID), round(TUED))
    return BuildTo

def fresh_wednesday(x):
    CS = x[2]
    usingWeek = x[3]
    usingFr = x[4]
    usingSun = x[5]
    stock = x[6]
    USEFRID = (usingWeek*3)+usingFr+(usingSun*2)
    FRID = ((USEFRID-stock)/CS)
    TUED = usingWeek*3
    BuildTo = ('Заказ на Пт --> Вт: ', round(FRID), round(TUED))
    return BuildTo

def tuesday_buildto(x):
    reserve = 1
    cs = x[2]
    usingWeek = x[3]
    usingFr = x[4]
    usingSun = x[5]
    STOCK = x[6]
    USEFRID = (usingWeek * 3) + usingFr + usingSun
    RESERVE = reserve * (statistics.mean([usingSun, usingFr, usingWeek]) / cs)
    USERSUN = usingSun + usingWeek
    MEAN = statistics.mean([usingSun, usingFr, usingWeek])
    if (USEFRID - STOCK) < 0:
        if MEAN >= abs(USEFRID - STOCK):
            FRIDR = math.ceil(RESERVE)
        else:
            FRIDR = 0
        FRID = FRIDR
        TAILS = FRID
        SUND = (USERSUN - TAILS) / cs
        STAILS = SUND - RESERVE
        USETUED = (usingWeek * 3) - STAILS
        TUED = (USETUED / cs) + (usingWeek * reserve) / cs
    elif (USEFRID - STOCK) == 0:
        FRID = RESERVE
        SUND = (USERSUN - FRID) / cs
        USETUED = usingWeek * 3
        TUED = ((USETUED - FRID) / cs) + ((usingWeek * reserve) / cs)
    else:
        FRID = math.ceil(((USEFRID - STOCK) / cs)) + RESERVE
        TAILS = FRID
        SUND = (USERSUN - TAILS) / cs
        USETUED = usingWeek * 3
        TUED = ((USETUED - TAILS) / cs) + ((usingWeek * reserve) / cs)
    buildTo = ('Заказ на пт -- Вс -- Вт', round(FRID), round(SUND), round(TUED), '  ')
    return buildTo

def monday_buildto(x):
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

def wednesday_buildto(x):
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
        FRID = math.ceil(((USEFRID - STOCK)) / cs) + RESERVE
        TAILS = FRID - RESERVE
        USETUED = usingWeek * 3
        TUED = ((USETUED - TAILS) / cs) + ((usingWeek * reserve) / cs)
    buildTo = ('Заказ ', round(FRID), round(TUED), '')
    return buildTo
