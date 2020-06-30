from Skill.repositories import SkillRepo
from Skill.interactors import GetSkillInteractor,GetAllSkillInteractor,GetAllSkillByUserInteractor,DeleteExistingSkillInteractor,UpdateExistingSkillInteractor,CreateNewSkillInteractor,GetAllSkillByUserInteractor
from Skill.views import SkillView,AllSkillView,AllSkillByUserView


class SkillRepoFactory(object):
    @staticmethod
    def get():
        return SkillRepo()

#class SkillValidatorFactory(object):
 #   @staticmethod
   # def get():
    #    return SkillValidator()
class GetAllSkillByUserInteractorFactory(object):
    @staticmethod
    def get():
        skill_repo = SkillRepoFactory.get()
        return GetAllSkillByUserInteractor(skill_repo)

class GetAllSkillInteractorFactory(object):
    @staticmethod
    def get():
        skill_repo = SkillRepoFactory.get()
        return GetAllSkillInteractor(skill_repo)

class GetSkillInteractorFactory(object):
    @staticmethod
    def get():
        skill_repo = SkillRepoFactory.get()
        return GetSkillInteractor(skill_repo)

class CreateNewSkillInteractorFactory(object):
    @staticmethod
    def get():
        skill_repo = SkillRepoFactory.get()
        #skill_validator = SkillValidatorFactory.get()
        return CreateNewSkillInteractor(skill_repo)
        #return CreateNewSkillInteractor(skill_repo, skill_validator)


class UpdateExistingSkillInteractorFactory():
    @staticmethod
    def get():
        skill_repo = SkillRepoFactory.get()
        #skill_validator = SkillValidatorFactory.get()
        return UpdateExistingSkillInteractor(skill_repo)

class DeleteExistingSkillInteractorFactory(object):
    @staticmethod
    def get():
        skill_repo = SkillRepoFactory.get()
        return DeleteExistingSkillInteractor(skill_repo)

#class GetAllSkillByUserInteractorFactory(object):
    #@staticmethod
    #def get():
     #   skill_repo = SkillRepoFactory.get()
      #  return GetAllSkillByUserInteractor(skill_repo)


class SkillViewFactory(object):
    @staticmethod
    def create(request, **kwargs):
        return SkillView(GetSkillInteractorFactory.get(), 
       UpdateExistingSkillInteractorFactory.get(), DeleteExistingSkillInteractorFactory.get())

#class AllSkillByUserViewFactory(object):
   # @staticmethod
   # def create(request, **kwargs):
     #   return SkillView(GetSkillInteractorFactory.get(), 
      # UpdateExistingSkillInteractorFactory.get(), DeleteExistingSkillInteractorFactory.get())


class AllSkillViewFactory(object):
    @staticmethod
    def create(request, **kwargs):
        return AllSkillView(GetAllSkillInteractorFactory.get(), CreateNewSkillInteractorFactory.get())

class AllSkillByUserViewFactory(object):
    @staticmethod
    def create(request, **kwargs):
        return AllSkillByUserView(GetAllSkillByUserInteractorFactory.get())
