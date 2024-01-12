import random
from model.project import Project
import string

def test_add_project(app, json_projects):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    old_projects = app.soap.get_project_list(username, password)
    project = json_projects
    n = 0
    for old_project in old_projects:
        if project.name == old_project.name:
            n += 1
            continue
    if (n > 0):
        print("Ошибка")
    else:
        app.project.create(project)
        new_projects = app.soap.get_project_list(username, password)
        old_projects.append(project)
        assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


