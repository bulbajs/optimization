import math

BASE_TR_COST = 12000 * 1.4 / 13
MAX_TR_COST = 12000


def linear_meters(length_mm):
    k = math.ceil(length_mm / 1000)
    tr_cost = round(BASE_TR_COST * k, 1)
    if tr_cost > 12000:
        tr_cost = MAX_TR_COST
    return tr_cost

length_mm = float(input('Введите значение длины в мм: '))
result = linear_meters(length_mm)
print(result)


# Отрицательные значения при вводе
# Определение большего значения как длины
# Структура приложения
# Виртуальное окружение
# Подключение расчета транспорта к проекту
