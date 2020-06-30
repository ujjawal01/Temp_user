"""sso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from django.conf import settings
#from useraccount.views import FrontendRenderView #,Profile_View_Factory

from useraccount.factories import User_view_factory ,AllUsersViewFactory
from Projects.factories import ProjectViewFactory,AllProjectViewFactory, AllProjectByUserViewFactory
from Skill.factories import SkillViewFactory,AllSkillViewFactory,AllSkillByUserViewFactory

from .views import ViewWrapper

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/<int:id>/', ViewWrapper.as_view(view_factory = User_view_factory), name= 'user'),
    path('users/', ViewWrapper.as_view(view_factory = AllUsersViewFactory), name= 'users'),
    #path('user/profile/<int:id>/', ViewWrapper.as_view(view_factory = Profile_View_Factory), name='profile'),
    path('user/<int:user_id>/project/<int:id>/', ViewWrapper.as_view(view_factory = ProjectViewFactory), name= 'project'),
    path('user/<int:user_id>/projects/', ViewWrapper.as_view(view_factory = AllProjectByUserViewFactory), name= 'projects'),
    path('user/<int:id>/skills', ViewWrapper.as_view(view_factory = AllSkillByUserViewFactory), name= 'skill'),
    path('skills/', ViewWrapper.as_view(view_factory = AllSkillViewFactory), name= 'skills'),


    
   
]



