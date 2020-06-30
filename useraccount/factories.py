from useraccount.repositories import UserRepo
from useraccount.interactors import GetAllUsersInteractor,GetUserAccountInteractor,CreateNewUserInteractor,UpdateUserAccountInteractor,DeleteUserAccountInteractor
from useraccount.views import UserView,AllUsersView

class create_user_repo_factory(object):
    @staticmethod
    def get():
        return UserRepo()

class get_user_account_interactor_factory(object):
    @staticmethod
    def get():
        user_repo = create_user_repo_factory.get()
        return GetUserAccountInteractor(user_repo)


class create_user_account_interactor_factory(object):
    @staticmethod
    def get():
        user_repo = create_user_repo_factory.get() 
        return CreateNewUserInteractor(user_repo)


class update_user_account_interactor_factory(object):
    @staticmethod
    def get():
        user_repo = create_user_repo_factory.get()
        return UpdateUserAccountInteractor(user_repo)

class delete_user_account_interactor_factory(object):
    @staticmethod
    def get():
        user_repo = create_user_repo_factory.get()
        return DeleteUserAccountInteractor(user_repo)

#
   #UserView( CreateUserAccountInteractor( UserRepo() ) )

class GetAllUsersInteractorFactory(object):
    @staticmethod
    def get():
        user_repo = create_user_repo_factory.get()
        return GetAllUsersInteractor(user_repo)

#class CreateNewUserInteractorFactory(object):
 #   @staticmethod
  #  def get():
   #     user_repo = UserRepoFactory.get()
    #    return CreateNewUserInteractor(user_repo)

class AllUsersViewFactory(object):
    @staticmethod
    def create(request, **kwargs):
        return AllUsersView(GetAllUsersInteractorFactory.get(), create_user_account_interactor_factory.get())


class User_view_factory(object):
    @staticmethod
    def create(request, **kwargs):
        return UserView(get_user_account_interactor_factory.get(),create_user_account_interactor_factory.get(),update_user_account_interactor_factory.get(),delete_user_account_interactor_factory.get())




