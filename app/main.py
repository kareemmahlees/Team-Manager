from rich.console import Console
import questionary
from typer import Typer
import utils
from admin import Admin
from user import User

console = Console()
app = Typer()

print(
    """
████████╗███████╗ █████╗ ███╗   ███╗    ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
   ██║   █████╗  ███████║██╔████╔██║    ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
   ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║    ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
      """
)


console.print("[cyan]Please Login To Your Account[/]")
username = questionary.text("Username:").ask()
password = questionary.password("Password:").ask()
val = utils.validate_user(username, password)
if not val:
    quit()
if val == "Admin":
    while True:
        console.print("✥-----------------✥---------------✥")
        admin = Admin()
        commands = {
            "List Members": lambda: admin.list_members(),
            "Add Team Member": lambda: admin.add_member(),
            "Delete Team Member": lambda: admin.delete_member(),
            "List Task's": lambda: admin.list_tasks(),
            "Assign Task": lambda: admin.assign_task(username),
            "Update Task": lambda: admin.update_task(),
            "Delete Task": lambda: admin.delete_task(),
            "Schedule Meeting": lambda: admin.schedule_meeting(username),
        }
        try:
            command = questionary.select(
                "What Would You Like To Do",
                choices=[choice for choice in commands.keys()],
                use_indicator=True,
            ).ask()
            commands[command]()
        except KeyboardInterrupt:
            quit()
        prmt = questionary.confirm("Do You Want Something Else").ask()
        if not prmt:
            break
    quit()

if val == "User":
    while True:
        console.print("✥-----------------✥---------------✥")
        user = User()
        commands = {
            "List Tasks": lambda: user.list_tasks(username),
            "List TODO": lambda: user.list_todo(),
            "Add TODO": lambda: user.add_todo(),
            "Check TODO": lambda: user.check_todo(),
            "Delete TODO": lambda: user.delete_todo(),
        }
        try:
            command = questionary.select(
                "" "What Would You Like To Do",
                choices=[choice for choice in commands.keys()],
                use_indicator=True,
            ).ask()
            commands[command]()
        except KeyboardInterrupt:
            quit()
        prmt = questionary.confirm("Do You Want Something Else").ask()
        if not prmt:
            break
    quit()
