import flet as ft


def main(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.SYSTEM
    text_hello = ft.Text(value="Hello world!", color=ft.Colors.RED_900)

    # text_button = ft.TextButton("SEND")
    # icon_button = ft.IconButton(icon=ft.Icons.SEND)

    def text_name(e):
        # print(name_input.value)
        name = name_input.value.strip()

        if name:
            text_hello.value = f'Hello {name}'
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



    elevated_button = ft.ElevatedButton('send', on_click=text_name)


    name_input = ft.TextField(label='Введите что-нибудь')



    page.add(text_hello, name_input, elevated_button, thememode_button)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
