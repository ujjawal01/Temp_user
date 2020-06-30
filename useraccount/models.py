# Create your models here.
from django.contrib.auth.models import User
#from initiatives.models import ORMInitiative
from django.db import models
from django.db.models import Manager
from django.utils import timezone
from initiatives.models import ORMInitiative

Roles_options = (
    ("S", "Student"),
    ("A", "Admin"),
    ("I", "Internal team"),
    ("T", "Teacher"),
    ("O", "Others"),
)

class ORMRole(models.Model):
    objects = Manager()

   
    type = models.CharField( max_length = 20, choices = Roles_options,default = 'S') 

    def __str__(self):
        return self.type



#class Email_verification(models.Model):
 #   objects = Manager()
#    email = models.EmailField(primary_key=True)
 #   token = models.CharField(max_length=1024)
  #  expiry = models.DateTimeField(auto_now_add=False)




class ORMDepartment(models.Model):
    objects = Manager()

   
    dept_name = models.CharField(max_length=40)

    def __str__(self):
        return self.dept_name


class ORMSkill(models.Model):
    objects = Manager()

    #these are predefined skills ,choices can be removed to add more skills
    #to remove choice use first skillname
    # skills =(
    # ('IOT','Internet Of Things'),('ML','Machine Learning'),('AI','Artificial Inteligence')
    # )
    #skill_name = models.CharField(max_length=10)
    skill_name = models.CharField(max_length=50)


    class Meta:
       verbose_name = 'Skill'
       verbose_name_plural = 'Skills'


    def __str__(self):
        return self.skill_name


class ORMUser(models.Model):

    objects = Manager()
    #user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='user') 
    
    
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    college_name = models.CharField(max_length=50)
    email = models.EmailField()
    email_verified = models.BooleanField(default=True) 
    role = models.ForeignKey(ORMRole,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False,blank=True)
    department = models.ForeignKey(ORMDepartment,on_delete=models.CASCADE, blank=True, null=True)
    skills = models.ManyToManyField(ORMSkill,related_name="skill")
    initiatives = models.ManyToManyField(ORMInitiative)
    userimage = models.ImageField(upload_to=None,default='',blank=True)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=30,null=True,default='')
    disable_account = models.BooleanField(default=False)
    last_login = models.DateTimeField(editable=True,default=timezone.now)
    login_count = models.PositiveIntegerField(default=0)
    about_me = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    

    class Meta:
       verbose_name = 'ORMUser'
       verbose_name_plural = 'ORMUsers'

    def __str__(self):
       return self.username

