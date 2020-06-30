from Projects.repositories import ProjectRepo
from Projects.interactors import GetProjectInteractor,GetAllProjectInteractor,GetAllProjectByUserInteractor,DeleteExistingProjectInteractor,UpdateExistingProjectInteractor,CreateNewProjectInteractor
from Projects.views import ProjectView,AllProjectView,AllProjectByUserView


class ProjectRepoFactory(object):
    @staticmethod
    def get():
        return ProjectRepo()

#class ProjectValidatorFactory(object):
 #   @staticmethod
   # def get():
    #    return ProjectValidator()

class GetAllProjectInteractorFactory(object):
    @staticmethod
    def get():
        project_repo = ProjectRepoFactory.get()
        return GetAllProjectInteractor(project_repo)

class GetProjectInteractorFactory(object):
    @staticmethod
    def get():
        project_repo = ProjectRepoFactory.get()
        return GetProjectInteractor(project_repo)

class CreateNewProjectInteractorFactory(object):
    @staticmethod
    def get():
        project_repo = ProjectRepoFactory.get()
        #project_validator = ProjectValidatorFactory.get()
        return CreateNewProjectInteractor(project_repo)
        #return CreateNewProjectInteractor(project_repo, project_validator)


class UpdateExistingProjectInteractorFactory():
    @staticmethod
    def get():
        project_repo = ProjectRepoFactory.get()
        #project_validator = ProjectValidatorFactory.get()
        return UpdateExistingProjectInteractor(project_repo)

class DeleteExistingProjectInteractorFactory(object):
    @staticmethod
    def get():
        project_repo = ProjectRepoFactory.get()
        return DeleteExistingProjectInteractor(project_repo)

class GetAllProjectByUserInteractorFactory(object):
    @staticmethod
    def get():
        project_repo = ProjectRepoFactory.get()
        return GetAllProjectByUserInteractor(project_repo)


class ProjectViewFactory(object):
    @staticmethod
    def create(request, **kwargs):
        return ProjectView(GetProjectInteractorFactory.get(), 
       UpdateExistingProjectInteractorFactory.get(), DeleteExistingProjectInteractorFactory.get())

class AllProjectViewFactory(object):
    @staticmethod
    def create(request, **kwargs):
        return AllProjectView(GetAllProjectInteractorFactory.get())

class AllProjectByUserViewFactory(object):
    @staticmethod
    def create(request, **kwargs):
        return AllProjectByUserView(GetAllProjectByUserInteractorFactory.get(), CreateNewProjectInteractorFactory.get())
