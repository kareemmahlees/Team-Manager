from flet import UserControl, Row, Text, Switch, Page, Column, Container, padding


class SettingsBoard(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page: Page = page

    def build(self):
        dark_mode_switch = Container(
            Switch(
                value=False,
                on_change=self.on_switch_on,
            )
        )
        dark_mode_switch.padding = padding.only(left=40, bottom=500)
        dark_mode_txt = Container(content=Text("Dark Mode", weight="bold"))
        dark_mode_txt.padding = padding.only(left=40, right=200, bottom=500)
        return Column(
            controls=[
                Row(
                    controls=[dark_mode_txt, dark_mode_switch],
                    expand=True,
                )
            ],
            expand=True,
        )

    def on_switch_on(self, e):
        self.page.theme_mode = "dark" if self.page.theme_mode == "light" else "light"
        self.page.update()
