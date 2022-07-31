from rich.console import Console
import questionary
from typer import Typer
import utils
from admin import Admin

console = Console()
app = Typer()

# print(
#     """
#   _______                     __  __
#  |__   __|                   |  \/  |
#     | | ___  __ _ _ __ ___   | \  / | __ _ _ __   __ _  __ _  ___ _ __
#     | |/ _ \/ _` | '_ ` _ \  | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
#     | |  __/ (_| | | | | | | | |  | | (_| | | | | (_| | (_| |  __/ |
#     |_|\___|\__,_|_| |_| |_| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|
#                                                        p __/ |
#                                                        |___/
#                     """
# )
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
            "List Tas'ks": lambda: admin.list_tasks(),
            "Assign Task": lambda: admin.assign_task(username),
            "Update Task": lambda: admin.update_task(),
            "Delete Task": lambda: admin.delete_task(),
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
