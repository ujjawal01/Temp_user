from .entities import User,Skill
#from .exceptions import EntityDoesNotExistException, InvalidEntityException

class GetAllUserInteractor(object):
    """   Return all users    """
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def set_params(self):
        return self 
 
    def execute(self):
        return self.user_repo.get_all_user()


class GetUserAccountInteractor(object):

    def __init__(self, user_repo):
        #self.user_validator = user_validator
        self.user_repo = user_repo
        

    def set_params(self,id):
        self.id = id
        
        return self

    def execute(self):
        #user = self.user_repo.get_user(id=self.user_id,username=self.username,email=self.email)
        #fetched_user = User(user_id=user.user_id,username=self.username, email=self.email, is_email_verified=False)

        return self.user_repo.get_user(id=self.id)
 
class UpdateUserAccountInteractor(object):

    def __init__(self, user_repo):

        self.user_repo = user_repo
        
        #self ,department,firstname=None,lastname=None,college_name=None,email=None,role=None,username=None,password=None,about_me=None,phone=None,skill=[] 

    #def patch(self ,id,department,firstname=None,lastname=None,college_name=None,email=None,username=None,password=None,about_me=None,phone=None,skill=None):

    def set_params(self,id,firstname,lastname,college_name, email, username,passowrd, dept_name, about_me,phone,**kwargs):
        #self, firstname, lastname,college_name, email,about_me,phone,username,password,department

        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.college_name = college_name
        self.email = email
        self.dept_name = dept_name
        #self.skill = skill
        self.about_me=about_me
        #self.userimage = userimage
        self.username = username
        self.password = passowrd
        self.phone = phone

        return self


    def execute(self):

        user = self.user_repo.get_user(id=self.id)

        updated_firstname = self.firstname if self.firstname is not None else user.firstname
        updated_lastname = self.lastname if self.lastname is not None else user.lastname
        updated_college_name = self.college_name if self.college_name is not None else user.college_name
        updated_email = self.email if self.email is not None else user.email
        updated_dept_name = self.dept_name if self.dept_name is not None else user.dept_name
       # updated_skill = self.skill if self.skill is not None else user.skill
        updated_password = self.password if self.password is not None else user.password
        updated_about_me = self.about_me if self.about_me is not None else user.about_me
        updated_phone = self.phone if self.phone is not None else user.phone
        updated_username = self.username if self.username is not None else user.username


       # if self.skill is not None :
         #   for a in self.skill:
          #      skill_ = Skill(a)
        #        updated_skill.append(skill_) 
    #    def __init__(self,id=None, firstname=None, lastname=None,college_name=None, email=None, email_verified=None,role=None,is_active=None,department_id=None,skill=None,userimage=None,username=None,password=None,disable_account=None,last_login=None,login_count=None,about_me=None,phone=None,project=None,initiatives=None):

        updated_user = User(id=self.id,firstname=updated_firstname,lastname=updated_lastname,college_name=updated_college_name,email=updated_email,username=updated_username,password=updated_password,about_me=updated_about_me,phone=updated_phone,dept_name= updated_dept_name,initiatives=None,skill=None)  
        #confirmation_token interactor will be written here
        return self.user_repo.update_user(updated_user)

class CreateNewUserInteractor(object):
#can add user_validator as second argument of this func
    def __init__(self,user_repo):

        #self.user_validator = user_validator
        self.user_repo = user_repo
        

    def set_params(self,firstname,lastname,college_name,email,role,department,username,password,phone):
        #self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.college_name = college_name
        self.email = email
        self.role = role
        self.dept_name = department
        #self.skill = skill
        self.username = username
        self.password = password
        #self.about_me = about_me
        self.phone = phone
        return self

    def execute(self):

        user = User(firstname=self.firstname,lastname=self.lastname,college_name=self.college_name,email=self.email,role=self.role,dept_name=self.dept_name,username=self.username,password=self.password,about_me=None,phone=self.phone,skills=None)
        #user = User(firstname=self.firstname,lastname=self.lastname,college_name=self.college_name,email=self.email,role=self.role,username=self.username,password=self.password,about_me=self.about_me,phone=self.phone,skill=self.skill)

        return self.user_repo.create_user(user)
        

class DeleteUserAccountInteractor(object):
#can add user_validator as second argument
    def __init__(self, user_repo):
        self.user_repo = user_repo
        

    def set_params(self, id):
        self.id = id
        return self
    

    def execute(self):
       
       
       return self.user_repo.delete_user(id=self.id)


class GetAllUsersInteractor(object):
    """Returns(gets) all Users """
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def set_params(self):
        return self

    def execute(self):
        return self.user_repo.get_all_users()

