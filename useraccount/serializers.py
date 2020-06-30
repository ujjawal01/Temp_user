from django.core import serializers

class ExceptionSerializer:

    @staticmethod
    def serialize(exception):
        return {
                   'error': {
                       'source': exception.source,
                       'code': exception.code,
                       'message': str(exception)
                    }
               }

                

class UserSerializer:

    @staticmethod
    def serialize(user):
        return {
                   'id': int(user.id),
                   'firstname':user.firstname,
                   'lastname': user.lastname,
                   'college_name': user.college_name,
                   'email': user.email,
                   'email_verified':user.email_verified,
                   'role':user.role.type,
                   'department':user.dept_name,
                   #'skills': MultipleSkillSerializer.serialize(user.skills),
                   #'userimage':user.userimage,
                   'username':user.username,
                   'about_me' : user.about_me,
                   'phone': user.phone,
                   
                   'initiatives':user.initiatives
                   
                   

                }



class MultipleUserSerializer:

    @staticmethod
    def serialize(user_set):
        return [UserSerializer.serialize(user) for user in user_set]




class DepartmentSerializer:

    @staticmethod
    def serialize(department):

        #for item in department:
         #   item['product'] = model_to_dict(item['product'])
        return {
                   
                   'dept_name':department.dept_name
                   
                }

class SkillSerializer:

    @staticmethod
    def serialize(skill):
        return{
            
            'skill_name': skill.skill_name
        }

class MultipleSkillSerializer:

    @staticmethod
    def serialize(skill):
        return [SkillSerializer.serialize(skill_) for skill_ in skill]

class MultipleSkillNameSerializer:

    @staticmethod
    def serialize(skill):
        return [SkillSerializer.serialize(skill_) for skill_ in skill]


class SkillNameSerializer:

    @staticmethod
    def serialize(skill):
        return{
            
            'skill_name': skill
        }









    