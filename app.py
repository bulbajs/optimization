import flet as ft
from optimization import optimization

def main(page: ft.Page):
    page.title = 'OPTIMIZATION'
    exw_field = ft.TextField(label = "EXW", hint_text = "Введите значение", width = 150)
    tr_field = ft.TextField(label="TR", hint_text="Введите значение")
    customs_rate_field = ft.TextField(label="customs_rate", hint_text="Введите 0.22 или 0.32")
    result = ft.TextField(label = 'Цена для клиента', value = '0')
    dlg = ft.AlertDialog(
        modal= True,
        title=ft.Text('Внимание'),
        content=ft.Text('Введите корректное значение'),
        actions=[],
    )

    def dlg_close(e):
        page.pop_dialog()

    dlg.actions.append(ft.TextButton(content = 'OK', on_click = dlg_close))


    def calculate(e):
        try:
            EXW = int(exw_field.value)
            TR = int(tr_field.value)
            cm_rate = float(customs_rate_field.value)
            res = optimization(EXW, TR, cm_rate)
            a = res['customer_price']
            result.value = f'{a:.2f} евро'
        except ValueError:
                page.show_dialog(dlg)
                return
        page.update()

    page.add(
        ft.Text(value = 'Давайте посчитаем', size = 22, weight=ft.FontWeight.W_600, color = '#0F4F11'),
        exw_field,
        tr_field,
        customs_rate_field,
        result,
        ft.Button(content = 'Calculate', on_click = calculate ),
        )
    page.dialog = dlg



if __name__ == "__main__":
    ft.run(main)