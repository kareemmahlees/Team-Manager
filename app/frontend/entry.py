from .link.login import Login
from .boards.admin_board import admin_board
from . import utils
import flet
from flet import (
    Page,
    Text,
    Container,
    padding,
    CircleAvatar,
    icons,
    Icon,
    theme,
    TextField,
    TextButton,
    ElevatedButton,
)


def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = "light"
    page.window_resizable = False
    page.title = "Team Manager"
    page.theme = theme.Theme(color_scheme_seed="blue")
    page.window_height = page.window_height - 100
    page.window_width = page.window_width - 200

    avatar = Container(
        CircleAvatar(content=Icon(icons.PERSON, size=50), width=80, height=80)
    )

    login_txt = Text("Login", size=20)

    username_input = TextField(
        label="Username",
        width=300,
        keyboard_type="email",
    )
    cont_username_input = Container(username_input)
    cont_username_input.padding = padding.all(20)

    password_input = TextField(
        label="Password",
        width=300,
        keyboard_type="visiblePassword",
        can_reveal_password=True,
        password=True,
    )

    password_input.padding = padding.only(top=20)

    sign_up = TextButton(text="Don't Have Account ? Sign up")

    def on_click_login(e):
        log = Login(username_input.value, password_input.value).send_creds()

        if log.status_code == 200 and log.json()["role"] == "Admin":
            page.route = "/admin"
            page.update()
            admin_board(page=page)
        elif log.status_code == 404:
            utils.wrong_creds(
                page=page, user_input=username_input, pass_input=password_input
            )

    login = Container(
        ElevatedButton(text="Login", icon=icons.LOGIN, on_click=on_click_login)
    )
    login.padding = padding.only(top=20)

    page.add(avatar, login_txt, cont_username_input, password_input, sign_up, login)


flet.app(target=main, assets_dir="./assets")
