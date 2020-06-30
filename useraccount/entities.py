#import gc

class Skill:

    def __init__(self,skill_id=None, skill_name=None):
        self._skill_name = skill_name
        self._skill_id = skill_id

    @property
    def skill_name(self):
        return self._skill_name

    @property
    def skill_id(self):
        return self._skill_id


    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other


class User:

    def __init__(self, firstname, lastname,college_name, email,about_me,phone,username,password,dept_name,role,email_verified=None,is_active=None,skills=None,userimage=None,disable_account=None,id=None,last_login=None,login_count=None,initiatives=None):
        self._id = id
        self._firstname = firstname
        self._lastname = lastname
        self._college_name = college_name
        self._email = email
        self._email_verified = email_verified
        self._role = role
        self._is_active = is_active
        self._dept_name = dept_name
        self._skills = skills
        self._userimage = userimage
        self._username = username
        self._password = password
        self._disable_account = disable_account
        self._last_login = last_login
        self._login_count = login_count
        self._about_me = about_me
        self._phone = phone
        self._initiatives=initiatives
        self._skills = skills


    @property
    def id(self):
        return self._id

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname

    @property
    def college_name(self):
        return self._college_name


    @property
    def email(self):
        return self._email

    @property
    def email_verified(self):
        return self._email_verified

    @property
    def role(self):
        return self._role

    @property
    def is_active(self):
        return self._is_active

    @property
    def dept_name(self):
        return self._dept_name

    @property
    def skills(self):
        return self._skills
    @property
    def password(self):
        return self._password

   # @property
   # def userimage(self):
   #     return self._userimage
   #
    @property
    def username(self):
        return self._username

    @property
    def disable_account(self):
        return self._disable_account

    @property
    def last_login(self):
        return self._last_login

    @property
    def about_me(self):
        return self._about_me

    @property
    def phone(self):
        return self._phone

    @property
    def initiatives(self):
        return self._initiatives


    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other








































