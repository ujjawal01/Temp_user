from Skill.repositories import SkillRepo
from useraccount.entities import Skill,User
#from useraccount.models import ORMSkill,ORMUser


class GetAllSkillInteractor(object):
    """Returns all Skill """
    def __init__(self, skill_repo):
        self.skill_repo = skill_repo

    def set_params(self):
        return self

    def execute(self):
        return self.skill_repo.get_all_skill()

class GetSkillInteractor(object): 
    """Returns Skill based on id """
    def __init__(self, skill_repo):
        self.skill_repo = skill_repo

    def set_params(self, id):
        self.id = id
        return self

    def execute(self):
        return self.skill_repo.get_skill(id = self.id)

class CreateNewSkillInteractor(object):
    """Creates new Skill """
    def __init__(self, skill_repo):
    #def __init__(self, skill_repo, skill_validator):
        self.skill_repo = skill_repo
        #self.skill_validator = skill_validator
        
    def set_params(self,skill_name,user_id):
        self.skill_name = skill_name
        self.user_id = user_id
        return self



    def execute(self):
        

        skill = Skill(skill_name =self.skill_name)
        s=self.skill_repo.create_new_skill(skill)
        self.skill_repo.get_user_add_skill(self.user_id,s)
        

        #self.skill_validator.validate_skill(skill)
        return skill.skill_name
class UpdateExistingSkillInteractor(object):
    """Updates Skill """
    def __init__(self, skill_repo):
    
    #def __init__(self, skill_repo, skill_validator):

        self.skill_repo = skill_repo
        #self.skill_validator = skill_validator

    def set_params(self, id, skill_name):
        self.id = id
        self.skill_name = skill_name

        return self

    def execute(self):
        skill = self.skill_repo.get_skill(id=self.id)
        
        name = self.skill_name if self.skill_name is not None else skill.skill_name
        
        
        updated_skill = Skill(skill_id =self.id,skill_name =name)
        #self.skill_validator.validate_skill(updated_skill)
        
        return self.skill_repo.update_existing_skill(updated_skill)

class DeleteExistingSkillInteractor(object):
    """Deletes a Skill"""
    def __init__(self, skill_repo):
        self.skill_repo = skill_repo

    def set_params(self, id):
        self.id = id
        return self

    def execute(self):
        return self.skill_repo.delete_existing_skill(id = self.id)

class GetAllSkillByUserInteractor(object):
   
    def __init__(self, skill_repo):
        self.skill_repo = skill_repo

    def set_params(self, id):
        self.id = id
        return self

    def execute(self):
        return self.skill_repo.get_skills_by_user(id = self.id)



        



