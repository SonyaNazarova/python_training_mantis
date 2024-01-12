import random
from model.project import Project


def test_del_project(app, json_projects):
    project = json_projects
    app.session.login("administrator", "root")
    if app.project.count() == 0:
       app.project.create(project)
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.del_project_by_id(project.id)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert len(old_projects) == len(new_projects)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)