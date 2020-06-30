from .entities import User,Skill
from .exceptions import EntityDoesNotExistException
#from .conf import settings
from .models import ORMUser,ORMSkill,ORMDepartment,ORMRole
from initiatives.models import ORMInitiative
from sso.Exceptions import EntityDoesNotExistException
import logging



class UserRepo(object):


    def _decode_db_skill(self, db_skill):
        return Skill ( skill_name = db_skill.skill_name)

    def _decode_db_user(self, db_user):
        skills=[]
        skill_set=db_user.skills.all()

        for db_skill in skill_set:
            skill = self._decode_db_skill(db_skill)
            skills.append(skill)


        initiatives=[]
        initiative_set=db_user.initiatives.all()

        for initiative in initiative_set:
            initiatives.append(initiative.acronym)

        
        # projects=[]

        # n=ORMUser.objects.filter(username=db_user.username).first()
        # project_set = ORMProject.objects.filter(ormuser=n)
        # for db_project in project_set:
        #     project =  _decode_db_project(db_project)
        #     projects.append(project)

        #projects=[]
        #project_set = ORMProject.objects.filter(ormuser_id=db_user.id)
        #p=list(project_qset)

        #Role=[]
        #role=Role
        
        #for project in project_set:
            #projects.append(project.name)

        return User(id=db_user.id,firstname=db_user.firstname, lastname=db_user.lastname,college_name=db_user.college_name, email=db_user.email,role=db_user.role,dept_name=db_user.department.dept_name, username=db_user.username,password=db_user.password,about_me=db_user.about_me,phone=db_user.phone,initiatives=initiatives)

#department not added in parameters intentionally
#department error corrected


    def get_all_users(self):
        all_db_user = ORMUser.objects.all()
        
        users =[]
        for db_user in all_db_user:
            users.append(self._decode_db_user(db_user))
        return users


    #def create_user(self,firstname,lastname,college_name,email,role,department,username,password,about_me,phone,skill=[]):
    def create_user(self,user):

        
        dept = ORMDepartment.objects.filter(dept_name=user.dept_name).first()

        #department_id= x.id

        #stdlogger.error("%s" % (department_id))

        #print(department_id)
        role_ = ORMRole.objects.get(type=user.role)
        
        db_user = ORMUser.objects.create(firstname=user.firstname,lastname=user.lastname,college_name=user.college_name,email=user.email,role=role_,department=dept,username=user.username,password=user.password,phone=user.phone)
        #db_user = ORMUser.objects.create(firstname=user.firstname,lastname=user.lastname,college_name=user.college_name,email=user.email,role=role_,username=user.username,password=user.password,about_me=user.about_me,phone=user.phone)
         
        print (db_user)

        #db_skill = Role.objects.get(skill_name=skill)
        
       # for a in skill:
            #try:
                #orm_skill = Skill.objects.filter(skill_name = a.upper()[0]).first()
            #except IndexError:
             #   raise EntityDoesNotExistException(source='audience', code='not found', message='Enter skill correctly')
            #else:
             #   db_user.skill.add(orm_skill)
              #  db_user.save()
        
        
        return self._decode_db_user(db_user)


    

    def get_user(self, id):
    
        db_user = ORMUser.objects.get(id=id)

        return self._decode_db_user(db_user)


        #except ORMUser.DoesNotExist:
            #raise EntityDoesNotExistException
    
    
    def update_user(self, user):

        orm_user = ORMUser.objects.get(id = user.id)
        dept = ORMDepartment.objects.filter(dept_name=user.dept_name).first()

        orm_user.firstname = user.firstname
        orm_user.lastname = user.lastname
        orm_user.college_name = user.college_name
        orm_user.email = user.email
        orm_user.department = dept
        orm_user.about_me = user.about_me
        orm_user.phone = user.phone
        orm_user.password = user.password
        #orm_user.skill = user.skill

        #orm_user.skill = user.skill
        #orm_user.userimage = user.userimage
        orm_user.username = user.username
        orm_user.save()

        return self._decode_db_user(orm_user)


    def delete_user(self, id):
        orm_user = ORMUser.objects.get(id=id)
        orm_user.delete()
    



        
#print(UserRepo.create_user(1,'ujjwww'))


