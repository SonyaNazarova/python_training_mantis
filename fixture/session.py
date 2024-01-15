class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element("name", "username").click()
        wd.find_element("name", "username").clear()
        wd.find_element("name", "username").send_keys(username)
        wd.find_element("css selector", 'input[type="submit"]').click()
        wd.find_element("name", "password").click()
        wd.find_element("name", "password").clear()
        wd.find_element("name", "password").send_keys(password)
        wd.find_element("css selector", 'input[type="submit"]').click()

    def logout(self):
        wd = self.app.wd
        wd.find_element("xpath", "//div[@id='navbar-container']/div[2]/ul/li[3]/a/span").click()
        wd.find_element("link text", "Выход").click()
        wd.find_element("name", "username").clear()

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element("xpath", "//div[@id='navbar-container']/div[2]/ul/li[3]/a/span").text



    def ensure_logout(self):
        self.app.wd
        if self.is_logged_in():
            self.logout()


    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements("link text", "Все проекты")) > 0


    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username


    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element("xpath", "//div[@id='navbar-container']/div[2]/ul/li[3]/a/span").text

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
