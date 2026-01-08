import flet as ft
from datetime import datetime


def main(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.SYSTEM


    text_hello = ft.Text(value="Hello world!")


    def text_name(e):

        name = name_input.value.strip()
        now = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")

        if name:
            text_hello.value = f'{now} - Привет, {name}!'
            text_hello.color = None
            
        else:
            text_hello.value = "Введите имя!"
            text_hello.color = ft.Colors.RED

    def thememode(_):
        
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
                

    thememode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)



    elevated_button = ft.ElevatedButton('send', on_click=text_name, icon=ft.Icons.SEND)


    name_input = ft.TextField(label='Введите ваше имя', on_submit=text_name)



    page.add(name_input, elevated_button, text_hello, thememode_button)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
