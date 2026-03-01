# import tkinter as tk
#
# window = tk.Tk()
# # window.title('Оптимизация')
#
# EXW = tk.Label(window, text='ff')
# EXW.pack()
# window.mainloop()

import flet as ft
from optimization import optimization

def main(page: ft.Page):
    page.title = 'OPTIMIZATION'
    exw_field = ft.TextField(label = "EXW", hint_text = "Введите значение")
    tr_field = ft.TextField(label="TR", hint_text="Введите значение")
    custom_rate_field = ft.TextField(label="customs_rate", hint_text="Введите 0.22 или 0.32")
    result = ft.Text(value = '0')
    def calculate(e):
        result.value = exw_field.value
        page.update()

    page.add(
        ft.Text(value = 'Давайте посчитаем', size = 22, weight=ft.FontWeight.W_600, color = '#0F4F11'),
        exw_field,
        tr_field,
        custom_rate_field,
        result,
        ft.Button(content = 'Calculate', on_click = calculate ),
        )




if __name__ == "__main__":
    ft.run(main)