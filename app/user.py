import questionary
from database import conn, cr
from rich.table import Table
from rich.console import Console

console = Console()


class User:
    def __init__(self) -> None:
        pass

    def list_tasks(self, member):
        cr.execute(""" SELECT * FROM tasks WHERE member_name=%s""", (member,))
        tasks = cr.fetchall()
        table = Table(
            title="Assigned Tasks",
            show_lines=True,
        )
        table.add_column(header="title")
        table.add_column(header="description")
        table.add_column(header="created at")
        table.add_column(header="deadline")
        table.add_column(header="assigned by")
        for task in tasks:
            table.add_row(
                task["title"],
                task["description"],
                str(task["created_at"]),
                str(task["deadline"]),
                task["created_by"],
            )
        console.print(table)

    def list_todo(self):
        cr.execute(""" SELECT * FROM todo""")
        todos = cr.fetchall()
        table = Table(title="TODOs", show_lines=True)
        table.add_column(header="title")
        table.add_column(header="description")
        table.add_column(header="created at")
        table.add_column(header="status")
        for todo in todos:
            status = todo["status"]
            table.add_row(
                todo["title"],
                todo["description"],
                str(todo["created_at"]),
                "❌" if todo["status"] == 0 else "✔️",
            )
        console.print(table)

    def add_todo(self):
        title = questionary.text("TODO Title :").ask()
        description = questionary.text("TODO Description: ", multiline=True).ask()
        cr.execute(
            """ INSERT INTO todo (title,description) VALUES(%s,%s)""",
            (title, description),
        )
        conn.commit()
        console.print(f"[green]Successfuly Created TODO {title}[/]")

    def check_todo(self):
        self.list_todo()
        cr.execute("""SELECT title FROM todo WHERE status = 0""")
        tasks = cr.fetchall()
        task = questionary.autocomplete(
            "Which Task You Want To Check", choices=[task["title"] for task in tasks]
        ).ask()
        try:
            cr.execute(""" UPDATE todo SET status=1 WHERE title = %s""", (task,))
            conn.commit()
            console.print("[green]Successfuly Checked Todo")
        except:
            console.print("[red bold]Error While Checking Todo")

    def delete_todo(self):
        self.list_todo()
        cr.execute("""SELECT title FROM todo""")
        tasks = cr.fetchall()
        task = questionary.autocomplete(
            "Which Task You Want To Delete", choices=[task["title"] for task in tasks]
        ).ask()
        try:
            cr.execute(""" DELETE FROM todo WHERE title = %s""", (task,))
            conn.commit()
            console.print("[green]Successfuly Deleted Todo")
        except:
            console.print("[red bold]Error While Deleting Todo")
