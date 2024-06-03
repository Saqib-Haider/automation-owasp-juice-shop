class LoginPage:
    def __init__(self, page):
        self.page = page
        self.close_banner = page.get_by_label("Close Welcome Banner")
        self.email = page.get_by_label("Text field for the login email")
        self.password = page.get_by_label("Text field for the login password")
        self.login_btn = page.get_by_label("Login", exact=True)

    def dismiss_banner(self):
        self.close_banner.click()

    def enter_email(self, email):
        self.email.fill(email)

    def enter_password(self, password):
        self.password.fill(password)

    def click_login(self):
        self.login_btn.click()

    def login(self, email, password):
        self.dismiss_banner()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()