from django.contrib import admin

# Register your models here
from useraccount.models import ORMUser,ORMDepartment,ORMSkill,ORMRole

#admin.site.register(UserProfile)
admin.site.register(ORMUser)
admin.site.register(ORMDepartment)
admin.site.register(ORMSkill)
admin.site.register(ORMRole)





