class ProjectSerializer:

    @staticmethod
    def serialize(Project):
        return {
                   'id':Project.id,
                   'name':Project.name,
                   'description':Project.description,
                   'technology':Project.technology
                   
                }

class MultipleProjectSerializer:

    @staticmethod
    def serialize(project):
        return [ProjectSerializer.serialize(project_) for project_ in project]