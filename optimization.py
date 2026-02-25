def optimization(EXW, TR):
    customs_clr = 600
    customs = (EXW + TR)*0.2
    print(type(customs))
    cost_unit = EXW + customs_clr + customs
    return customs


EXW = int(input('Введите EXW: '))
TR = int(input('Введите значение стоимости погонных метров: '))

optimization(EXW,TR)
print(f'CC = {optimization(EXW,TR)}')
