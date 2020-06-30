from useraccount.models import ORMSkill,ORMUser
from useraccount.entities import Skill

class SkillRepo(object):

    def _decode_db_skill(self, db_skill):
        return Skill(skill_id=db_skill.id,skill_name=db_skill.skill_name)

    def get_all_skill(self):
        all_db_skill = ORMSkill.objects.all()
        skill_ = []
        for db_skill in all_db_skill:
            skill_.append(self._decode_db_skill(db_skill))
            print(skill_)
            return skill_
    
    def create_new_skill(self, skill):

        db_skill = ORMSkill.objects.create(skill_name=skill.skill_name)
        

        return self._decode_db_skill(db_skill)

    def update_existing_skill(self,skill):

        db_skill = ORMSkill.objects.get(id = skill.id)
        db_skill.name = skill.name
    
        db_skill.save()
        return self._decode_db_skill(db_skill)

    def delete_existing_skill(self, id):
        return ORMSkill.objects.get(id = id).delete()

    def get_skill(self, id):
        #stdlogger.info("Call to get_skill method")
        #stdlogger.debug("Getting the skill from id")
        db_skill = ORMSkill.objects.get(id = id)
        return self._decode_db_skill(db_skill)
    
    def get_skills_by_user(self, id):
        #stdlogger.info("Call to get_skill method")
        #stdlogger.debug("Getting the skill from id")
        user = ORMUser.objects.get(id =id)
        skill_set=user.skills.all()
        skill_=[]
        for skill in skill_set:
            skill_.append(self._decode_db_skill(skill))

        return skill_

    def get_user_add_skill(self,user_id,skill):
        user = ORMUser.objects.get(id =user_id)
        s=ORMSkill.objects.filter(skill_name=skill.skill_name).first()
        return user.skills.add(s)

