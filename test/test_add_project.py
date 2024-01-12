
def test_add_project(app, json_projects):
    app.session.login("administrator","root")
    project = json_projects


