from flet import Page, TextField, colors


def wrong_creds(page: Page, user_input: TextField, pass_input: TextField):
    def on_focus_userinput(e):
        user_input.error_text = None
        page.update()

    def on_focus_passinput(e):
        pass_input.error_text = None
        page.update()

    user_input.error_text = "Invalid Username Or Password"
    user_input.on_focus = on_focus_userinput
    pass_input.error_text = "Invalid Username Or Password"
    pass_input.on_focus = on_focus_passinput
    page.update()
