import flet as ft
from datetime import datetime


def main(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.SYSTEM

    greeting_history = []
    history_text = ft.Text("История приветствий: ")


    text_hello = ft.Text(value="Hello world!")


    def text_name(e):

        name = name_input.value.strip()
        now = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")

        if name:
            text_hello.value = f'{now} - Привет, {name}!'
            text_hello.color = None
            name_input.value = None

            greeting_history.append(name)
            print(greeting_history)
            history_text.value = 'История приветствий:\n' + '\n'.join(greeting_history)
            
        else:
            text_hello.value = "Введите имя!"
            text_hello.color = ft.Colors.RED

    def thememode(_):
        
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
                

    thememode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)

    def delete_name(e):
        if greeting_history:
            greeting_history.pop()
            history_text.value = 'История приветствий:\n' + '\n'.join(greeting_history)
        else:
            history_text.value = 'История приветствий:\n История пуста!'

    delete_button = ft.ElevatedButton('Delete name', on_click=delete_name, icon=ft.Icons.DELETE_OUTLINE)



    def clear_history(e):
        greeting_history.clear()
        history_text.value = "История приветствий: "


    clear_button =ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)


    elevated_button = ft.ElevatedButton('send', on_click=text_name, icon=ft.Icons.SEND)

    name_input = ft.TextField(label='Введите ваше имя', on_submit=text_name)

    main_object = ft.Row([name_input, elevated_button, thememode_button, clear_button, delete_button])

    page.add(text_hello, main_object, history_text)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
