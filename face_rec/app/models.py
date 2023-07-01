from django.db import models
from django.contrib.auth.models import AbstractUser


# # Create your models here.
# class CustomUser(AbstractUser):
#     USER=(
#         ('1', 'HOD'),
#         ('2', 'STUDENT'),
#     )


#     user_type = models.CharField(choices=USER, max_length=60,default=1)
    




# class Student(models.Model):
#     admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
#     profilePicture= models.ImageField(upload_to='media')
#     gender = models.CharField(max_length=100)
    


#     def __str__(self):
#         return self.admin.first_name + " "+ self.admin.last_name