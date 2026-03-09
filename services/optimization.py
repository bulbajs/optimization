def optimization(EXW: int, TR: int, customs_rate: float):
    customs_clr = 600
    koef_risk = 1.1
    mult = 1.35
    customs = (EXW + TR * 0.7) * customs_rate
    CC = EXW + TR + customs_clr + customs
    CC_final = CC * koef_risk
    koef_final = CC_final / EXW
    customer_price = CC_final * mult
    return {
        'CC_final': CC_final,
        'koef_final': koef_final,
        'customer_price': customer_price,
    }

if __name__ == "__main__":
    EXW = int(input('Введите EXW: '))
    TR = int(input('Введите стоимость транспорта: '))
    customs_rate = float(input('Введите ставку 0,22 или 0,32: '))

    result = optimization(EXW, TR, customs_rate)
    print(f'Цена для клиента = {round(result["CC_final"],2)} евро')


