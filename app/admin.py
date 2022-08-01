from datetime import datetime
import questionary
from database import conn, cr
from rich.console import Console
from rich.table import Table
import utils

console = Console()


class Admin:
    """
    Class For Handling Team Admin privileges
    """

    def __init__(self) -> None:
        pass

    def list_members(self):
        cr.execute(""" SELECT * FROM users""")
        memebers = cr.fetchall()
        table = Table(title="Members", show_header=True, show_lines=True)
        table.add_column(header="username")
        table.add_column(header="password")
        table.add_column(header="role", style="magenta")
        for memeber in memebers:
            table.add_row(memeber["username"], memeber["password"], memeber["role"])
        console.print(table)

    def add_member(self):
        username = questionary.text("Add Member Username: ").ask()
        password = questionary.password("Add Member Password: ").ask()
        role = questionary.select(
            "Select The Role Of Member", choices=["Admin", "User"]
        ).ask()
        try:
            cr.execute(
                """ INSERT INTO users(username,password,role,id) VALUES (%s,%s,%s,uuid_generate_v4()) RETURNING *""",
                (username, password, role),
            )
            member = cr.fetchone()
            conn.commit()
            console.print(
                f"[green]Successfully Created Member {member['username']} [/]"
            )
        except:
            console.print(f"[red bold]Error While Creating Member[/]")

    def delete_member(self):
        cr.execute(""" SELECT * FROM users """)
        members = cr.fetchall()
        username = questionary.autocomplete(
            "Enter The Username To Delete",
            choices=[username["username"] for username in members],
        ).ask()
        try:
            cr.execute(
                """ DELETE FROM users WHERE username=%s RETURNING *""", (username,)
            )
            deleted_member = cr.fetchone()
            conn.commit()
            console.print(
                f"[green]Successfuly Deleted Member {deleted_member['username']}"
            )
        except:
            console.print("[red]Error While Deleting Member")

    def list_tasks(self):
        cr.execute(""" SELECT * FROM tasks""")
        table = Table(title="Tasks", show_lines=True)
        table.add_column(header="id")
        table.add_column(header="title")
        table.add_column(header="description")
        table.add_column(header="created_at")
        table.add_column(header="deadline")
        table.add_column(header="created_by")
        table.add_column(header="member")
        for member in cr.fetchall():
            table.add_row(
                str(member["id"]),
                member["title"],
                member["description"],
                str(member["created_at"]),
                str(member["deadline"]),
                member["created_by"],
                member["member_name"],
            )
        console.print(table)

    def assign_task(self, creator):
        title = questionary.text("Task Title: ").ask()
        description = questionary.text("Task Discription: ", multiline=True).ask()
        deadline = questionary.text("Deadline: ", instruction="yyyy-mm-dd").ask()
        created_by = creator
        cr.execute(""" SELECT * FROM users""")
        members = cr.fetchall()
        mem = questionary.autocomplete(
            "Will Be Assigned To: ", choices=[member["username"] for member in members]
        ).ask()
        cr.execute("""SELECT id FROM users WHERE username = %s""", (mem,))
        member = cr.fetchone()
        try:
            cr.execute(
                """ INSERT INTO tasks(title,description,deadline,created_by,member_id,member_name) VALUES (%s,%s,%s,%s,%s,%s)""",
                (title, description, deadline, created_by, member["id"], mem),
            )
            conn.commit()
            console.print(f"[green]Successfuly Assigned Task {title} to {mem}")
        except:
            console.print("[bold red]Error While Assigning Task")

    def update_task(self):
        cr.execute(""" SELECT * FROM tasks""")
        tasks = cr.fetchall()
        task = questionary.rawselect(
            "What Task You Want To Update", choices=[task["title"] for task in tasks]
        ).ask()
        subject = questionary.rawselect(
            "What Subject You Want to Update",
            choices=["title", "description", "deadline", "member_name"],
        ).ask()
        new = questionary.text("Enter The New Value: ").ask()
        cr.execute(
            """ UPDATE tasks SET {}=%s WHERE title=%s""".format(subject), (new, task)
        )
        conn.commit()
        console.print("[green]Successfuly Updated Task")

    def delete_task(self):
        self.list_tasks()
        cr.execute(""" SELECT * FROM tasks""")
        tasks = cr.fetchall()
        task_to_delete = questionary.rawselect(
            "Which Task To Delete", choices=[task["title"] for task in tasks]
        ).ask()
        try:
            cr.execute(""" DELETE FROM tasks WHERE title=%s""", (task_to_delete,))
            conn.commit()
            console.print("[green]Successfuly Deleted Task")
        except:
            console.print("[red bold]Error While Deleting Task[/]")

    def schedule_meeting(self, person_1):
        cr.execute(""" SELECT * FROM users""")
        members = cr.fetchall()
        table = Table(title="Members", show_header=True, show_lines=True)
        table.add_column(header="username")
        table.add_column(header="role", style="magenta")
        for memeber in members:
            table.add_row(memeber["username"], memeber["role"])
        console.print(table)
        tm = questionary.autocomplete(
            "Schedule With Whom", choices=[member["username"] for member in members]
        ).ask()
        start_date: str = questionary.text(
            "Start Date:", instruction="yyyy-mm-dd"
        ).ask()
        start_time: str = questionary.text("Start Time:", instruction="hh:mm:ss").ask()
        end_date: str = questionary.text("End Date:", instruction="yyyy-mm-dd").ask()
        end_time: str = questionary.text("End Time:", instruction="hh:mm:ss").ask()
        utils.schedule(
            person_1,
            tm,
            start=datetime.strptime(
                start_date + " " + start_time, r"%y-%m-%d %H:%M:%S"
            ),
            end=datetime.strptime(end_date + " " + end_time, r"%y-%m-%d %H:%M:%S"),
        )
