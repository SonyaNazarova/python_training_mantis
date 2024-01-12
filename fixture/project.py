from selenium.webdriver.support.ui import Select
from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element("xpath","//button[@type='submit']").click()
        self.fill_project_form(project)
        wd.find_element("xpath", "//input[@value='Добавить проект']").click()



    def fill_project_form(self, project):
        wd = self.app.wd
        self.field_value("name", project.name)
        self.field_value("description", project.description)
        select_status = Select(wd.find_element("name", 'status'))
        select_status.select_by_visible_text("%s" % project.status)
        category = wd.find_element("name", 'inherit_global')
        category.send_keys("%s" % project.inherit_global)
        select_view_state = Select(wd.find_element("name", 'view_state'))
        select_view_state.select_by_visible_text("%s" % project.view_state)



    def open_project_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-2.26.0/my_view_page.php")
        wd.find_element("xpath", "//div[@id='sidebar']/ul/li[7]/a/i").click()
        wd.find_element("xpath", "//a[contains(text(),'Проекты')]").click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        project = []
        for element in wd.find_elements("tag name", "td"):
            name = element.text
            href = element.get_attribute("href")
            href.startswith("http://localhost/mantisbt-2.26.0/manage_proj_edit_page.php?project_id=")
            id = href[71:]
            project.append(Project(name=name, id=id))
        return project

    def field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element("name", field_name).click()
            wd.find_element("name", field_name).clear()
            wd.find_element("name", field_name).send_keys(text)

    def del_project_by_id(self, id):
        wd = self.app.wd
        self.select_project_by_id(id)
        wd.find_element("xpath", "//form[@id='manage-proj-update-form']/div/div[3]/button[2]").click()
        a = wd.current_url
        if wd.current_url == 'https://localhost/mantisbt-2.26.0/manage_proj_delete.php':
            wd.find_element("css selector","input[value='Удалить проект']").click()

    def select_project_by_id(self, id):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element("xpath", "a[href='mantisbt-2.26.0/manage_proj_edit_page.php?project_id=%s']" % id).click()

    def count(self):
        wd = self.app.wd
        self.open_project_page()
        return len(wd.find_elements("css selector", '.row-1 td a,.row-2 td a'))