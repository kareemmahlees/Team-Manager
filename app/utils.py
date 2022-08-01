import datetime
import requests
from database import conn, cr
from rich.console import Console
from config import settings

console = Console()


def validate_user(username, password):
    cr.execute(
        """SELECT * FROM users WHERE username=%s AND password =%s""",
        (username, password),
    )
    user = cr.fetchone()
    if not user:
        console.print("[bold red]Invalid Username Or Password[/]")
        return False
    else:
        console.print("[green]Loged In Successfuly[/]")
        console.print(f"Welcome {user['role']} {username}")
        return user["role"]


def schedule(p1, p2, start: datetime.datetime, end: datetime.datetime):
    headers = {"Authorization": "Bearer " + settings.access_token}
    body = {
        "summary": f"{p1} / {p2}",
        "description": f"{p1} will meet {p2} at {start}",
        "start": {"dateTime": start.isoformat() + "Z"},
        "end": {"dateTime": end.isoformat() + "Z"},
    }
    res = requests.post(
        r"https://www.googleapis.com/calendar/v3/calendars/kareemmahlees@gmail.com/events",
        headers=headers,
        json=body,
    )
