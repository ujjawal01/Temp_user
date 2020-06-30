from .models import ORMProject
from .entities import Project

class ProjectRepo:

    def _decode_db_project(self, db_project):
        return Project(id=db_project.id,name=db_project.name,description=db_project.description,technology=db_project.technology,user_id=db_project.user_id)

    def get_all_project(self):
        all_db_project = ORMProject.objects.all()
        projects = []
        for db_project in all_db_project:
            projects.append(self._decode_db_project(db_project))
        print(projects)
        return projects
    
    def create_new_project(self, project):

        db_project = ORMProject.objects.create(name=project.name,technology=project.technology,user_id=project.user_id)
        

        return self._decode_db_project(db_project)

    def update_existing_project(self,project):

        orm_project = ORMProject.objects.get(id = project.id)
        orm_project.name = project.name
        orm_project.description = project.description
        orm_project.technology = project.technology
        orm_project.user_id = project.user_id
        orm_project.save()
        return self._decode_db_project(orm_project)

    def delete_existing_project(self, id):
        return ORMProject.objects.get(id = id).delete()

    def get_project(self, id):
        #stdlogger.info("Call to get_project method")
        #stdlogger.debug("Getting the project from id")
        db_project = ORMProject.objects.get(id = id)
        return self._decode_db_project(db_project)

    def get_all_project_by_user(self, user_id):
        #stdlogger.info("Call to get_project method")
        #stdlogger.debug("Getting the project from id")
        db_projects = ORMProject.objects.filter(user_id = user_id)
        projects =[]
        for db_project in db_projects:
            projects.append(self._decode_db_project(db_project))
        return projects