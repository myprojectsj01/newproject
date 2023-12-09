from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# Overriding the Default Django Auth User and adding One More Field (user_type)
class CustomUser(AbstractUser):
    user_type_data = ((1, "Host"), (2, "Cuser"),)
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
    
class Host(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Cuser(models.Model):
    GENDER=[('Male','Male'),('Female','Female')]
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=200)
    gender=models.CharField(choices=GENDER,default='Select',max_length=50,)
    password=models.CharField(max_length=200)
    image_file=models.ImageField(max_length=100,null=True,blank=' ',upload_to='media')    
    objects = models.Manager()

    def __str__(self):
            return self.name
    


class make_online_webpage(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(Cuser, on_delete = models.CASCADE)
    companyname=models.CharField(max_length=100)
    phoneno=models.CharField(max_length=10)
    landline=models.CharField(max_length=15)
    emailid=models.EmailField()
    webpage=models.URLField(max_length=200)
    businesskey=models.CharField(max_length=500)
    typeoption=models.CharField(max_length=100)
    profimage=models.ImageField(max_length=100,null=True,blank=' ',upload_to='companies/')
    address=models.CharField(max_length=200)
    aregion=models.CharField(max_length=100)
    postalcode=models.CharField(max_length=6)
    objects = models.Manager()

    
# It's like trigger in database. It will run only when Data is Added in CustomUser model

@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will automatically insert data in HOD, Staff or Student
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            Host.objects.create(admin=instance)
        if instance.user_type == 2:
            Cuser.objects.create(admin=instance, address="",email='', password="",gender="")
        

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.host.save()
    if instance.user_type == 2:
        instance.cuser.save()
   