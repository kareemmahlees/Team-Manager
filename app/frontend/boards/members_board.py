from flet import UserControl, Text, ListTile, Column, Card, Icon, icons
from ..link.members import Members


class MembersBoard(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        members = Members().get_all_members().json()
        return Column(
            controls=[
                Card(
                    content=ListTile(
                        leading=Icon(icons.PERSON),
                        title=Text(member["username"]),
                        subtitle=Text(
                            member["id"]
                            + "\n"
                            + member["role"]
                            + "\n"
                            + member["phone"]
                            + "\n"
                            + member["gender"]
                        ),
                    ),
                    width=500,
                    height=123,
                )
                for member in members
            ],
            expand=True,
        )

        # return Column(controls=[Text("Hello World")])
