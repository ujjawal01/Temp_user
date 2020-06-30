from django.shortcuts import render
from useraccount.decorators import serialize_exceptions
from .serializers import ProjectSerializer,MultipleProjectSerializer

# Create your views here.

class AllProjectView(object):
    def __init__(self, get_all_project_interactor = None):
        self.get_all_project_interactor = get_all_project_interactor
        

    @serialize_exceptions
    def get(self):
        project = self.get_all_project_interactor.set_params().execute()

        body = MultipleProjectSerializer.serialize(project)
        status = 200

        return body,status

class ProjectView(object):
    def __init__(self, get_project_interactor=None, update_existing_project_interactor = None, delete_existing_project_interactor = None):
        
        self.get_project_interactor = get_project_interactor
        self.update_existing_project_interactor = update_existing_project_interactor
        self.delete_existing_project_interactor = delete_existing_project_interactor
    
    @serialize_exceptions
    def get(self, id, user_id):
       
        project = self.get_project_interactor.set_params(id = id).execute()

        body = ProjectSerializer.serialize(project)
        status = 200

        return body,status

    @serialize_exceptions
    def patch(self,id, name =None , description=None, technology=None,user_id=None ):
    
        project = self.update_existing_project_interactor.set_params(id = id, name = name , description=description, technology=technology, user_id=user_id ).execute()

        body = ProjectSerializer.serialize(project)
        status = 200

        return body,status

    def delete(self, id, user_id):
       
        self.delete_existing_project_interactor.set_params(id = id).execute()

        body = None
        status = 204

        return body,status

class AllProjectByUserView(object):
    def __init__(self, get_all_project_by_user_interactor = None, create_new_project_interactor = None):
        self.get_all_project_by_user_interactor = get_all_project_by_user_interactor
        self.create_new_project_interactor = create_new_project_interactor
        
    @serialize_exceptions
    def get(self, user_id):
        project = self.get_all_project_by_user_interactor.set_params(user_id = user_id).execute()

        body = MultipleProjectSerializer.serialize(project)
        status = 200

        return body,status

    @serialize_exceptions
    def post(self, name =None , description=None, technology=None,user_id=None ):
      
        project = self.create_new_project_interactor.set_params( name =name , description=description, technology=technology,user_id=user_id ).execute()
        body = ProjectSerializer.serialize(project)
        status = 201

        return body,status