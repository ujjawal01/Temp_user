from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from useraccount.decorators import serialize_exceptions
from useraccount.serializers import SkillSerializer,MultipleSkillSerializer,SkillNameSerializer

# Create your views here.

class AllSkillView(object):
    def __init__(self, get_all_skill_by_user_interactor = None, create_new_skill_interactor = None):
    #def __init__(self, get_all_skill_interactor = None, create_new_skill_interactor = None):

        self.get_all_skill_by_user_interactor = get_all_skill_by_user_interactor
        self.create_new_skill_interactor = create_new_skill_interactor

    @serialize_exceptions
    def get(self):
        #skill = self.get_all_skill_interactor.set_params().execute()
        skill = self.get_all_skill_by_user_interactor.set_params().execute()

        body = MultipleSkillSerializer.serialize(skill)
        status = 200

        return body,status

    @serialize_exceptions
    def post(self, skill_name =None,user_id=None ):
        #user enters username as user

        # if audience :
        #     audience_list =  ast.literal_eval(audience)
        # else:
        #     audience_list = []
       
        skill = self.create_new_skill_interactor.set_params( skill_name =skill_name,user_id=user_id).execute()
        body = SkillNameSerializer.serialize(skill)
        status = 201

        return body,status
        




class SkillView(object):
    def __init__(self, get_skill_interactor=None, update_existing_skill_interactor = None, delete_existing_skill_interactor = None):
        
        self.get_skill_interactor = get_skill_interactor
        self.update_existing_skill_interactor = update_existing_skill_interactor
        self.delete_existing_skill_interactor = delete_existing_skill_interactor
    
    @serialize_exceptions
    def get(self, id):
       
        skill = self.get_skill_interactor.set_params(id = id).execute()

        body = SkillSerializer.serialize(skill)
        status = 200

        return body,status

    @serialize_exceptions
    def patch(self,id, name =None , description=None, technology=None,user=None ):
        
        
       
        skill = self.update_existing_skill_interactor.set_params(id = id, name = name , description=description, technology=technology,ormuser=user ).execute()

        body = SkillSerializer.serialize(skill)
        status = 200

        return body,status

    def delete(self, id):
       
        self.delete_existing_skill_interactor.set_params(id = id).execute()

        body = None
        status = 204

        return body,status

class AllSkillByUserView(object):
    def __init__(self, get_all_skill_by_user_interactor = None):
        self.get_all_skill_by_user_interactor = get_all_skill_by_user_interactor
        
    @serialize_exceptions
    def get(self, id):
        skill = self.get_all_skill_by_user_interactor.set_params(id=id).execute()

        body = MultipleSkillSerializer.serialize(skill)
        status = 200

        return body,status