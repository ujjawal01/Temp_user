class Project:

    def __init__(self,name,description,technology, user_id, id=None):
        self._id = id
        self._name = name
        self._description = description
        self._technology = technology

        self._user_id = user_id

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def technology(self):
        return self._technology

    @property
    def user_id(self):
        return self._user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other