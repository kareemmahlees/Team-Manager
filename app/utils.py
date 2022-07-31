from passlib.context import CryptContext
from database import conn, cr
from rich.console import Console

console = Console()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(plain_password):
    return pwd_context.hash(plain_password)


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
