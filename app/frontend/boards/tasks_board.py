from flet import (
    UserControl,
    Column,
    Card,
    ListTile,
    Icon,
    icons,
    Text,
    PopupMenuButton,
    PopupMenuItem,
)
from ..link.tasks import Tasks


class TasksBoard(UserControl):
    """
    class for returning cards of tasks
    """

    tasks = Tasks().get_tasks()

    def build(self):
        tasks = Tasks().get_tasks()
        return Column(
            controls=[
                Card(
                    content=ListTile(
                        leading=Icon(icons.TASK),
                        title=Text(task["title"]),
                        subtitle=Text(
                            f"Description : {task['description']}"
                            + "\n"
                            + f"Created at : {task['created_at']}"
                            + "\n"
                            + f"Deadline : {task['deadline']}"
                            + "\n"
                            + f"Created by : {task['created_by']}"
                            + "\n"
                            + f"Member id : {task['member_id']}"
                            + "\n"
                            + f"Task id : {task['id']}"
                            + "\n"
                            + f"Member Name : {task['member_name']}"
                        ),
                        trailing=PopupMenuButton(
                            icon=icons.MORE_VERT,
                            items=[
                                PopupMenuItem(text="Delete"),
                                PopupMenuItem(text="Update"),
                            ],
                        ),
                    ),
                    width=700,
                    height=200,
                )
                for task in tasks.json()
            ]
        )
