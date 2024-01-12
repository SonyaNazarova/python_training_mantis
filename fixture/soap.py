from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper():

    def __init__(self,app):
        self.app = app


    def can_login(self,username, password):
        client = Client(self.app.baseUrl + "api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False


    def get_project_list(self,username,password):
        project_list = []
        client = Client("http://localhost/mantisbt-2.26.0/api/soap/mantisconnect.php?wsdl")
        try:
            project = client.service.mc_projects_get_user_accessible(username, password)
            for element in range(len(project)):
                id = project[element].id
                name = project[element].name
                status = project[element].status
                view_status = project[element].view_state
                project_list.append(Project(id=id, name=name))
            return list(project_list)
        except WebFault as ex:
            print(ex)
            return False