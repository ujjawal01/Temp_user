from .serializers import UserSerializer,MultipleUserSerializer
from .decorators import serialize_exceptions
from django.shortcuts import render
from django.views.generic import View
#from .factories import create_user_profile_interactor,get_user_profile_interactor,update_user_profile_interactor


#def home(request):
   # return(render(request,'basis.html'))

class UserView(object):

    def __init__(self,get_user_account_interactor=None,create_user_account_interactor=None,update_user_account_interactor=None,delete_user_account_interactor=None):
        self.get_user_account_interactor = get_user_account_interactor
        self.create_user_account_interactor = create_user_account_interactor
        self.update_user_account_interactor = update_user_account_interactor
        self.delete_user_account_interactor = delete_user_account_interactor
    

    #Retrieve user viewfunction
    @serialize_exceptions
    def get(self,id):
        user = self.get_user_account_interactor.set_params(id = id).execute()

        body = UserSerializer.serialize(user)
        status = 200

        return body, status
 
    @serialize_exceptions
    def patch(self,id,firstname=None,lastname=None,college_name=None,email=None,username=None,password=None,about_me=None,phone=None):
        user = self.update_user_account_interactor.set_params(id=id,firstname=firstname,lastname=lastname,college_name=college_name,email=email,username=username,password=password,about_me=about_me,phone=phone).execute()
        body = UserSerializer.serialize(user)
        status = 200
        return body, status
    


    def delete(self, id):
        self.delete_user_account_interactor.set_params(id=id).execute()

        body = None
        status = 204
        return body, status

class AllUsersView(object):
    def __init__(self, get_all_user_interactor = None, create_new_user_interactor = None):
        self.get_all_user_interactor = get_all_user_interactor
        self.create_new_user_interactor = create_new_user_interactor

    @serialize_exceptions
    def get(self):
        user_set = self.get_all_user_interactor.set_params().execute()

        body = MultipleUserSerializer.serialize(user_set)
        status = 200

        return body,status

    @serialize_exceptions
    def post(self,department,firstname=None,lastname=None,college_name=None,email=None,role=None,username=None,password=None,phone=None):

        #skillm =  ast.literal_eval(skill)
       
        user = self.create_new_user_interactor.set_params(firstname=firstname,lastname=lastname,college_name=college_name,email=email,role=role,username=username,password=password,phone=phone,department=department).execute()
        body = UserSerializer.serialize(user)
        status = 201

        return body,status
        




