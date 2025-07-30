from django.db import models
from _applib.model_Choice_fields import Genderchoice,TeacherStatus



class Teachermodel(models.Model):
    phone_number = models.CharField (max_length=11,unique=True)  
    FULL_Name = models.CharField(max_length=60) 
    profile_picture= models.CharField(max_length=300)
    gender=models.CharField(max_length=10,choices=Genderchoice.choices,default=Genderchoice.MALE)
    website=models.CharField(max_length=300,null=True,blank=True)
    status = models.CharField( max_length=15,choices=TeacherStatus.choices,default=TeacherStatus. PENDING) 
    password=models.CharField(max_length=300)
    Created_at=models.DateTimeField(auto_now_add=True)
    Updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"FULL_Name: {self.FULL_Name} || phone_number: {self.phone_number} || status : {self.status}"
    
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        db_table = 'Teacher'

# Create your models here.
