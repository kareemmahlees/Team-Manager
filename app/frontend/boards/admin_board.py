import flet
from flet import (
    Page,
    View,
    TextButton,
    icons,
    Column,
    VerticalDivider,
    Row,
    Container,
    padding,
)
from .members_board import MembersBoard
from .settings_board import SettingsBoard
from .tasks_board import TasksBoard


def admin_board(page: Page):
    """
    Dashboard which appears to the admins only

    Args:
        page (Page): page instance
    """
    page.views.clear()

    def on_click_members(e):
        if len(r1.controls) > 2:
            r1.controls.pop(-1)
            r1.controls.append(MembersBoard())
            page.update()
        else:
            r1.controls.append(MembersBoard())
            page.update()

    members_button = TextButton("Members", icon=icons.PERSON, on_click=on_click_members)

    def on_click_tasks(e):
        if len(r1.controls) > 2:
            r1.controls.pop(-1)
            r1.controls.append(TasksBoard())
            page.update()
        else:
            r1.controls.append(TasksBoard())
            page.update()

    tasks_button = TextButton("Tasks", icon=icons.TASK, on_click=on_click_tasks)
    meetings_button = TextButton("Meetings", icon=icons.MEETING_ROOM)

    def on_click_settings(e):
        if len(r1.controls) > 2:
            r1.controls.pop(-1)
            r1.controls.append(SettingsBoard(page))
            page.update()
        else:
            r1.controls.append(SettingsBoard(page))
            page.update()

    settings_button = TextButton(
        "Settings", icon=icons.SETTINGS, on_click=on_click_settings
    )

    left_col = Container(
        Column(
            controls=[
                members_button,
                tasks_button,
                meetings_button,
                settings_button,
            ]
        )
    )
    left_col.padding = padding.only(right=60)

    r1 = Row(controls=[left_col, VerticalDivider()], expand=True)

    page.views.append(View("/admin", controls=[r1]))
    page.update()
