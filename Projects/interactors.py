from Projects.repositories import ProjectRepo
from useraccount.entities import User
from useraccount.models import ORMUser
from .models import ORMProject
from .entities import Project

class GetAllProjectInteractor(object):
    """Returns all Project """
    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self):
        return self

    def execute(self):
        return self.project_repo.get_all_project()

class GetProjectInteractor(object): 
    """Returns Project based on id """
    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, id):
        self.id = id
        return self

    def execute(self):
        return self.project_repo.get_project(id = self.id)

class CreateNewProjectInteractor(object):
    """Creates new Project """
    def __init__(self, project_repo):
    #def __init__(self, project_repo, project_validator):

        self.project_repo = project_repo
        #self.project_validator = project_validator

    def set_params(self,name, description, technology, user_id):
        self.name = name
        self.description = description
        self.technology = technology
        self.user_id = user_id
    
        return self



    def execute(self):
        #user=ORMUser.objects.get(username=self.ormuser)
        #user_id=u.id
        project = Project(name =self.name ,description=self.description, technology=self.technology, user_id = self.user_id)
        #self.project_validator.validate_project(project)
        return self.project_repo.create_new_project(project)

class UpdateExistingProjectInteractor(object):
    """Updates Project """
    def __init__(self, project_repo):
    
    #def __init__(self, project_repo, project_validator):

        self.project_repo = project_repo
        #self.project_validator = project_validator

    def set_params(self, id, name, description, technology, user_id):
        self.id = id
        self.name = name
        self.description =description
        self.technology = technology
        self.user_id = user_id

        return self

    def execute(self):
        project = self.project_repo.get_project(id=self.id)
        
        uname = self.name if self.name is not None else project.name
        udescription = self.description if self.description is not None else project.description
        utechnology = self.technology if self.technology is not None else project.technology
        #uormuser= self.ormuser if self.ormuser is not None else project.ormuser
        
        
        updated_project = Project(id =self.id,name =uname,description=udescription, technology=utechnology, user_id=self.user_id)
        #self.project_validator.validate_project(updated_project)
        
        return self.project_repo.update_existing_project(updated_project)

class DeleteExistingProjectInteractor(object):
    """Deletes a Project"""
    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, id):
        self.id = id
        return self

    def execute(self):
        return self.project_repo.delete_existing_project(id = self.id)

class GetAllProjectByUserInteractor(object):
   
    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, user_id):
        self.user_id = user_id
        return self

    def execute(self):
        return self.project_repo.get_all_project_by_user(user_id = self.user_id)



        



