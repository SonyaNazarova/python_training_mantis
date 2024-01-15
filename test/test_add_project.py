import random
from model.project import Project
import string

def test_add_project(app, json_projects):
    old_projects = app.project.get_project_list()
    project = json_projects
    if app.project.project_name_is_already_exist(project, old_projects):
        project.name = project.name + random.choice(string.ascii_letters)
    app.project.create(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


