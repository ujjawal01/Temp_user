from django.db import models
from useraccount.models import ORMUser
from django.db import models
from django.db.models import Manager

# Create your models here.
class ORMProject(models.Model):
    objects = Manager()

    name = models.CharField(max_length=50)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    
    user= models.ForeignKey(ORMUser,on_delete = models.CASCADE)
    
    class Meta:
       verbose_name = 'ORMProject'
       verbose_name_plural = 'ORMProjects'

    def __str__(self):
       return self.name